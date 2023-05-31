from spade.behaviour import OneShotBehaviour
from spade.message import Message
from Airplane.Behaviours.requestTakeoffBehav import RequestTakeoffBehav
import asyncio
from config import config
from messages import AirplaneInfo


class LandBehav(OneShotBehaviour):

    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        self.data = data


    async def run(self):

        # Set state to landing
        self.agent.state = "landing"
        self.agent.runway = self.data.runway
        #print(str(self.agent.jid), "landing...")
        
        # Use the runway
        await asyncio.sleep(self.agent.landing_time + self.agent.drive_time + config.weather_state)

        # Set state to parked
        self.agent.state = "parked"
        self.agent.gare = self.data.gare

        # Inform tower of land completion
        msg = Message(to=f"tower@{config.host}")
        msg.set_metadata("performative", "landing_complete")
        msg.body = AirplaneInfo(self.agent)
        await self.send(msg)
        self.agent.runway = None

        #print(str(self.agent.jid), "parked...")

        # Start takeoff behaviour
        self.agent.add_behaviour(RequestTakeoffBehav())