from spade.behaviour import OneShotBehaviour
from spade.message import Message
from messages import GaresInfo, GareInfo, AirplaneInfo
from config import config


class LandRequestBehav(OneShotBehaviour):

    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        self.data = data


    async def run(self):

        # Request gares to GareManager
        #print("Tower requesting gares to GareManager")
        msg = Message(to=f"gare_manager@{config.host}")
        msg.set_metadata("performative", "list_gares")
        msg.body = self.data.type
        await self.send(msg)

        # Wait for GareManager response
        msg = await self.receive(timeout=10000)
        gares = GaresInfo(msg.body)
        #print("Tower received gares from GareManager")

        # Calculate fastest pair
        runway, gare = self.agent.fastest_pair(gares)

        # Not available
        if runway == None or gare == None:

            #print("No Runways or Gares available")
            
            if len(self.agent.landing_queue) >= self.agent.max_land_queue_size:

                #print("Landing Queue is full. Refusing landing request")

                self.data.state = "aborting"
                # Send refuse message
                msg = Message(to=f"{self.data.id}")
                msg.set_metadata("performative", "refused_to_land")
                await self.send(msg)

            else:

                #print(f"Adding {self.data.id} to landing queue")

                # Add to landing queue
                self.agent.landing_queue.append(self.data)
                self.data.state = "waiting_land_permission"

                # Send wait message
                msg = Message(to=f"{self.data.id}")
                msg.set_metadata("performative", "wait_to_land")
                await self.send(msg)

        else:
            
            # Reserve runway
            self.agent.runways[runway.id].free = False
            self.data.runway = runway

            # Reserve gare
            gare.free = False
            self.data.gare = gare
            msg = Message(to=f"gare_manager@{config.host}")
            msg.set_metadata("performative", "change_gare")
            msg.body = GareInfo(gare)
            await self.send(msg)

            #print("Reserved Runway. Reserved Gare. Allowing landing request")

            self.data.state = "landing"
            # Allow landing
            msg = Message(to=f"{self.data.id}")
            msg.set_metadata("performative", "permission_to_land")
            msg.body = AirplaneInfo(self.data)
            await self.send(msg)

        self.agent.add_plane(self.data)