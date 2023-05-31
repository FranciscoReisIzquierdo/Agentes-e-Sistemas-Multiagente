from spade.behaviour import OneShotBehaviour
from spade.message import Message
import asyncio
from config import config
from messages import AirplaneInfo


class TakeoffBehav(OneShotBehaviour):

    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        self.data = data


    async def run(self):

        # Set state to taking_off
        self.agent.state = "taking_off"
        self.agent.runway = self.data.runway
        #print(str(self.agent.jid), "taking off...")

        # Use the runway
        await asyncio.sleep(self.agent.landing_time + self.agent.drive_time + config.weather_state)
        #print(str(self.agent.jid), "takeoff...")

        # Inform tower of takeoff completion
        msg = Message(to=f"tower@{config.host}")
        msg.set_metadata("performative", "takeoff_complete")
        msg.body = AirplaneInfo(self.agent)
        await self.send(msg)

        # Update info
        self.agent.gare   = None
        self.agent.runway = None
        self.agent.state  = "on_air"

        # Stop the agent
        await self.agent.stop()