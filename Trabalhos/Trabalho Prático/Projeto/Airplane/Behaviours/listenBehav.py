from spade.behaviour import CyclicBehaviour
from messages import AirplaneInfo
from Airplane.Behaviours.landBehav import LandBehav
from Airplane.Behaviours.refusedLandBehav import RefusedLandBehav
from Airplane.Behaviours.waitLandBehav import WaitLandBehav
from Airplane.Behaviours.takeoffBehav import TakeoffBehav

class ListenBehav(CyclicBehaviour):

    async def run(self):

        msg = await self.receive(timeout=1000)
        type = msg.get_metadata("performative")

        if type == "permission_to_land":
            data = AirplaneInfo(msg.body)
            self.agent.add_behaviour(LandBehav(data))
        
        elif type == "refused_to_land":
            self.agent.add_behaviour(RefusedLandBehav())

        elif type == "wait_to_land":
            self.agent.add_behaviour(WaitLandBehav())

        elif type == "permission_to_takeoff":
            data = AirplaneInfo(msg.body)
            self.agent.add_behaviour(TakeoffBehav(data))