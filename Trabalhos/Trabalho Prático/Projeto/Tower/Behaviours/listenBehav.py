from spade.behaviour import CyclicBehaviour
from spade.template import Template
from spade.message import Message
from config import config
from messages import AirplaneInfo
from messages import ReportInfo
from Tower.Behaviours.landRequestBehav import LandRequestBehav
from Tower.Behaviours.takeoffRequestBehav import TakeoffRequestBehav
from Tower.Behaviours.landAbortBehav import LandAbortBehav
from Tower.Behaviours.confirmBehav import ConfirmBehav


class ListenBehav(CyclicBehaviour):

    async def run(self):

        msg = await self.receive(timeout=1000)
        type = msg.get_metadata("performative")

        if type == "request_landing":
            data = AirplaneInfo(msg.body)
            temp = Template()
            temp.set_metadata("performative", "gares_list")
            self.agent.add_behaviour(LandRequestBehav(data), temp)

        elif type == "request_takeoff":
            data = AirplaneInfo(msg.body)
            self.agent.add_behaviour(TakeoffRequestBehav(data))

        elif type == "land_abort":
            data = AirplaneInfo(msg.body)
            self.agent.add_behaviour(LandAbortBehav(data))

        elif type == "landing_complete":
            data = AirplaneInfo(msg.body)
            temp = Template()
            temp.set_metadata("performative", "gares_list")
            self.agent.add_behaviour(ConfirmBehav(data, "land"), temp)

        elif type == "takeoff_complete":
            data = AirplaneInfo(msg.body)
            temp = Template()
            temp.set_metadata("performative", "gares_list")
            self.agent.add_behaviour(ConfirmBehav(data, "takeoff"), temp)

        elif type == "request_report":
            msg = Message(to=f"admin@{config.host}")
            msg.set_metadata("performative", "response_report")
            msg.body = ReportInfo((self.agent.planes, self.agent.aborts))
            await self.send(msg)