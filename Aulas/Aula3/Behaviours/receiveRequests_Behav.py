from spade.behaviour import OneShotBehaviour
from spade.message import Message

class ReceiveRequestBehav(OneShotBehaviour):

    async def run(self):
        while True:
            msg = await self.receive(timeout=1000)
            print("Message received with content: {}".format(msg.body))
            l = msg.body.split("|")
            prod = int(l[0])
            qtd = int(l[1])
            self.agent.products_sold[self.agent.products[prod]] += qtd