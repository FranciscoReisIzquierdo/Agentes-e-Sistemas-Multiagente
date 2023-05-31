import pickle
from spade.message import Message


async def run(self):
        while True:
            msg = await self.receive(timeout=1000)
            msg = pickle.load(msg)
            print("Message received with content: {}".format(msg.body))
            
            toDo = msg.get_metadata("performative")

            if toDo == "customerRequestTransport":
                if len(self.taxis) > 0:
                    dist = (self.taxis[0].pos_x - msg.body.pos_x)**2 + (self.taxis[0].pos_y - msg.body.pos_y)**2
                    bestTaxi = 0
                    index = -1
                    for taxi in self.taxis [1:]:
                        if taxi.available == True:
                            distAux = (taxi.pos_x - msg.body.pos_x) + (taxi.pos_y - msg.body.pos_y)

                            if distAux < dist :
                                bestTaxi = index
                                dist = distAux
                            
                            index += 1

                    if index == -1:
                        self.agent.requests.append()
                    else:
                        self.taxis[bestTaxi].available = False
                        self.taxis[bestTaxi].pos_x = msg.body.pos_x
                        self.taxis[bestTaxi].pos_y = msg.body.pos_y

                        message = Message(to=f"{self.taxis[bestTaxi].name}")
                        message.set_metadata("performative", "MakeTrip")
                        message.body = f"{msg.body.pos_x}|{msg.body.pos_y}"
                        serializedMessage = pickle.dumps(message)
                        await self.send(serializedMessage)
                        print("Make the trip:", msg.body)
                     


            elif toDo == "subscribeTaxi":
                self.taxis.append(msg.body)

            elif toDo == "TripDone":
                 #Verificar qual é o taxi e meter available a true
                 None