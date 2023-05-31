from spade import agent
from Admin.Behaviours.updateBehav import UpdateBehav
from config import config


class AdminAgent(agent.Agent):

    async def setup(self):
                
        self.add_behaviour(UpdateBehav(period=config.update_time))