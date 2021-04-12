
from reader import *
from bonecatalogue import *

class BoneatorTextInterface:
    def __init__(self):
        self.file = []
        self.catalogue = Bonecatalogue()
    
    def manual(self):
        print("Options: ")
        print("Press 0 to quit, m to see manual.")
        print("1 Show file. 2 Count identifed species.")
        print("3 Count identified species by class. 4 Count NISP by class.")
        print("5 Count NISP and weight by class")

    def read_file(self):
        file = input("Hello, please give csv filename: ")
        self.catalogue.read_file(file)

    def do(self):
        self.read_file()
        self.manual()
        while True:
            print("")
            option = input("What do you want to do? ")
            if option == "0":
                print("Goodbye, see you next time!")
                break
            elif option == "m":
                self.manual()
            elif option == "1":
                self.catalogue.show_file()
            elif option == "2":
                self.catalogue.count_species()
            elif option == "3":
                self.catalogue.count_nisp_by_class()
            elif option == "4":
                species = input("Give species: ")
                self.catalogue.give_species(species)
            elif option == "5":
                self.catalogue.count_nisp_and_weight()

application = BoneatorTextInterface()
application.do()