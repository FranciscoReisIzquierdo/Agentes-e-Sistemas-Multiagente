import pickle


class AirplaneData():
    def __init__(self, airplane):
        self.id = airplane.id
        self.type = airplane.type
        self.origin = airplane.origin
        self.destination = airplane.destination
        self.company = airplane.company
        self.state = airplane.state
        self.gare = airplane.gare
        self.runway = airplane.runway


class GareData():
    def __init__(self, gare):
        self.id = gare.id
        self.position = gare.position
        self.type = gare.type
        self.free = gare.free



def AirplaneInfo(airplane):

    if not type(airplane) == str:

        return pickle.dumps(AirplaneData(airplane)).decode('latin1')
    
    else:
        
        return pickle.loads(airplane.encode('latin1'))



def GareInfo(gare):

    if not type(gare) == str:

        return pickle.dumps(GareData(gare)).decode('latin1')
    
    else:
        
        return pickle.loads(gare.encode('latin1'))



def GaresInfo(gares):

    if not type(gares) == str:

        return pickle.dumps([GareInfo(g) for g in gares]).decode('latin1')
    
    else: 

        return [GareInfo(g) for g in pickle.loads(gares.encode('latin1'))]
    


def ReportInfo(info):

    if not type(info) == str:

        return pickle.dumps(info).decode('latin1')
    
    else:

        return pickle.loads(info.encode('latin1'))