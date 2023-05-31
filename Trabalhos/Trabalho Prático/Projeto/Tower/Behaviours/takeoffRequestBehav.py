from spade.behaviour import OneShotBehaviour
from spade.message import Message
from messages import AirplaneInfo


class TakeoffRequestBehav(OneShotBehaviour):

    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        self.data = data


    async def run(self):

        # Calculate fastest pair (closest runway)
        runway, _ = self.agent.fastest_pair([self.data.gare])

        # Not available
        if runway == None:

            #print(f"No runways available. Adding {self.data.id} to takeoff queue")

            # Add to takeoff queue
            self.data.state = "waiting_takeoff_permission"
            self.agent.takeoff_queue.append(self.data)

        else:
            
            # Reserve runway
            self.agent.runways[runway.id].free = False
            self.data.runway = runway

            #print("Reserved Runway. Allowing takeoff")
            self.data.state = "taking_off"

            # Allow takeoff
            msg = Message(to=f"{self.data.id}")
            msg.set_metadata("performative", "permission_to_takeoff")
            msg.body = AirplaneInfo(self.data)
            await self.send(msg)

        self.agent.add_plane(self.data)