from spade.behaviour import OneShotBehaviour


class ChangeGareBehav(OneShotBehaviour):

    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        self.data = data

    async def run(self):

        # Change gare ocupation state
        self.agent.gares[self.data.id].free = self.data.free
        #print(f"Gare Manager Agent changed state of gare{self.data.id} to {self.data.free}")