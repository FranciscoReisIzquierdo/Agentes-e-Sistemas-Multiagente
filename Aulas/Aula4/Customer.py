from spade import agent
from ..Aula4.Behaviours import requestTransport_Behav
from .Behaviours import listenCustomer_Behav

class CustomerAgent(agent.Agent):

    parameters = None

    async def setup(self):
        print("Agent {}".format(str(self.jid)) + "starting...")
        request = requestTransport_Behav()
        self.add_behaviour(request)

        done = listenCustomer_Behav()
        self.add_behaviour(done)

        