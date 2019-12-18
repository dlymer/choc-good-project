# chocolately goodness controller
from .application import view
from .application import model


class Controller:

    def __init__(self):
        self.model = model.Model()
        view.init_view(self.model)
