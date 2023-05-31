from spade.behaviour import OneShotBehaviour


class RefusedLandBehav(OneShotBehaviour):
    
    async def run(self):

        # Go to another airport and stop the agent
        self.agent.stop()