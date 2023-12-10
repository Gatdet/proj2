from model import Model

class Controller:
    def __init__(self) -> None:
        """
        creates the model object"""
        self.__model = Model()
    
    def main(self) ->None:
        """
        starts the main function from the model class"""
        self.__model.main()

if __name__ == "__main__":
    cont = Controller()
    cont.main() 