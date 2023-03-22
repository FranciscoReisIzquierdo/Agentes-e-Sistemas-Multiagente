import random
from spade import agent


from Behaviours.profReview_Behav import ProfReviewBehav
from Behaviours.receiveRequests_Behav import ReceiveRequestBehav


class SellerAgent(agent.Agent):

    products_sold = {}
    products_value = {}
    products =  ['Apple', 'Banana', 'Grapefruit', 'Orange', 'Pear', 'Melon', 'Strawberry']

    async def setup(self):
        print("Agent {}".format(str(self.jid)) + "starting...")

        for i in self.products:
            self.products_sold[i] = 0
            self.products_value[i] = random.randint(1, 10)

        a = ReceiveRequestBehav()
        b = ProfReviewBehav(period=10)

        self.add_behaviour(a)
        self.add_behaviour(b)