from abc import abstractmethod


class InputHandlerDelegate:
    @abstractmethod
    def didTakeInput(self, move):
        doNothing = True

    @abstractmethod
    def setupNewGame(self):
        doNothing = True


class InputHandler:

    @abstractmethod
    def input(self):
        doNothing = True


class OutputHandler:

    @abstractmethod
    def setup(self):
        doNothing = True

    @abstractmethod
    def output(self, move):
        doNothing = True

    @abstractmethod
    def cancelMove(self):
        doNothing = True
