from spade.behaviour import PeriodicBehaviour

class ProfReviewBehav(PeriodicBehaviour):

    async def run(self):
        profit = 0
        
        for i in self.agent.products_sold:
            profit += (self.agent.products_sold[i] * self.agent.products_value[i])

        print("----------------------------\n")
        print("----------------------------\n")
        print("Agent {}:".format(str(self.agent.jid)) + " Profit = {}".format(profit))
        print("----------------------------\n")
        print("----------------------------\n\n")