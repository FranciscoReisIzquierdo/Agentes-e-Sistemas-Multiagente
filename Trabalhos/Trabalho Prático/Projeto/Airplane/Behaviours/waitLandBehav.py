from spade.behaviour import OneShotBehaviour
from spade.message import Message
from messages import AirplaneInfo
from config import config
import asyncio


class WaitLandBehav(OneShotBehaviour):
    
    async def run(self):

        # Set state to wait
        self.agent.state = "waiting_land_permission"
        #print(str(self.agent.jid), "waiting for landing permission...")

        # Wait for max amount of time
        await asyncio.sleep(self.agent.max_land_wait_time)

        # Check if landed
        if self.agent.state == "waiting_land_permission":
            # Inform tower of leaving
            msg = Message(to=f"tower@{config.host}")
            msg.set_metadata("performative", "land_abort")
            msg.body = AirplaneInfo(self.agent)
            await self.send(msg)
            # Stop the agent
            await self.agent.stop()
