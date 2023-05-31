from spade.behaviour import OneShotBehaviour
from spade.message import Message
from messages import GaresInfo, GareInfo, AirplaneInfo
from config import config


class ConfirmBehav(OneShotBehaviour):

    def __init__(self, data, type, **kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.type = type


    async def run(self):

        # Release runway
        self.agent.runways[self.data.runway.id].free = True

        # Release gare
        if self.type == "takeoff":
            gare = self.data.gare
            gare.free = True
            self.data.gare = gare
            msg = Message(to=f"gare_manager@{config.host}")
            msg.set_metadata("performative", "change_gare")
            msg.body = GareInfo(gare)
            await self.send(msg)
            #print(f"{self.data.id} Takeoff complete confirmed...")
            self.agent.remove_plane(self.data)
        else:
            #print(f"{self.data.id} Landing complete confirmed...")
            self.data.state = "parked"
            self.data.runway = None
            self.agent.add_plane(self.data)

        for plane in self.agent.landing_queue:
            
            # Request gares to GareManager
            msg = Message(to=f"gare_manager@{config.host}")
            msg.set_metadata("performative", "list_gares")
            msg.body = plane.type
            await self.send(msg)

            # Wait for GareManager response
            msg = await self.receive(timeout=10000)
            gares = GaresInfo(msg.body)

            runway, gare = self.agent.fastest_pair(gares)

            if runway and gare and plane in self.agent.landing_queue:

                # Remove plane from landing queue
                self.agent.landing_queue.remove(plane)

                # Reserve runway
                self.agent.runways[runway.id].free = False
                plane.runway = runway
                
                # Reserve gare
                gare.free = False
                plane.gare = gare
                msg = Message(to=f"gare_manager@{config.host}")
                msg.set_metadata("performative", "change_gare")
                msg.body = GareInfo(gare)
                await self.send(msg)

                #print("Reserved Runway. Reserved Gare. Allowing landing request")
                plane.state = "landing"

                # Allow landing
                msg = Message(to=f"{plane.id}")
                msg.set_metadata("performative", "permission_to_land")
                msg.body = AirplaneInfo(plane)
                await self.send(msg)


        for plane in self.agent.takeoff_queue:

            runway, gare = self.agent.fastest_pair([plane.gare])

            if runway and gare and plane in self.agent.takeoff_queue:

                # Remove plane from takeof queue
                self.agent.takeoff_queue.remove(plane)

                # Reserve runway
                self.agent.runways[runway.id].free = False
                plane.runway = runway
                
                # Reserve gare
                gare.free = True
                plane.gare = None
                msg = Message(to=f"gare_manager@{config.host}")
                msg.set_metadata("performative", "change_gare")
                msg.body = GareInfo(gare)
                await self.send(msg)

                #print("Reserved Runway. Reserved Gare. Allowing landing request")
                plane.state = "taking_off"

                # Allow takeoff
                msg = Message(to=f"{plane.id}")
                msg.set_metadata("performative", "permission_to_takeoff")
                msg.body = AirplaneInfo(plane)
                await self.send(msg)






