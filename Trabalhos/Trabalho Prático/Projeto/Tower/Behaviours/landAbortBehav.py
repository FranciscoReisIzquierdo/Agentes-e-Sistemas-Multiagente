from spade.behaviour import OneShotBehaviour


class LandAbortBehav(OneShotBehaviour):

    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        self.data = data


    async def run(self):

        #print(f"{self.data.id} aborted landing. Removing from queue")
        index = [i for i in range(len(self.agent.landing_queue)) if self.agent.landing_queue[i].id == self.data.id]
        if len(index) > 0:
            self.agent.landing_queue.pop(index[0])

        self.agent.remove_plane(self.data)
        self.agent.add_abort(self.data)