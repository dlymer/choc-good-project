#choclately goodness controller
from src.model.model import Model

class Controller():

    def __init__(self):
        self.model = Model()

    def renderHelloWorld(self):
        self.conModel = self.model.getHelloWorld()
        return self.conModel

controller = Controller()

