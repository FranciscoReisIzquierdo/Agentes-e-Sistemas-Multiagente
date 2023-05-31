import pickle, time
from spade.behaviour import OneShotBehaviour
from spade.message import Message


class listenTaxi_Behav(OneShotBehaviour):

    async def run(self):

       while True:
            msg = await self.receive(timeout=1000)
            msg = pickle.load(msg)
            print("Message received with content: {}".format(msg.body))
            newPostion = msg.split("|")
            time.sleep(3)
            self.agent.parameters.pos_x = newPostion[0]
            self.agent.parameters.pos_y = newPostion[1]

            message = Message(to="manager@msi")
            message.set_metadata("performative", "TripDone")
            message.body = self.agent.parameters
            serializedMessage = pickle.dumps(message)
            await self.send(serializedMessage)
            print("Make the trip:", msg.body)
            