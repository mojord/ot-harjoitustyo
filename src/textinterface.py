from services.bonecatalogue import Bonecatalogue


class BoneatorTextInterface:
    """Class for running text interface
    """
    def __init__(self):
        self.file = []
        self.catalogue = Bonecatalogue()

    def manual(self):
        """Prints manual
        """
        print("Options: ")
        print("Press 0 to quit, m to see manual.")
        print("1 Show file. 2 Count identifed species.")
        print("3 Count NISP and weight by class. 4 Show identified bones of given species.")
        print("5 Count juvenile specimens. 6 Give species breakdown for class.")
        print("7 Give total and not burned/burned share.")

    def read_file(self):
        """Takes filename input and calls catalogue read method.
        """
        print("Welcome!Please use filenames testaus.csv(simplest), bartsbones.csv or barts2.csv(largest) for trying out this program.")
        file = (input("Hello, please give csv filename: "))
        self.catalogue.read_file(file)

    def do(self):
        """Takes option input and calls relevant catalogue method
        """
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
                self.catalogue.count_nisp_and_weight_by_class()
            elif option == "4":
                species = input("Give species: ")
                print(self.catalogue.give_species(species))
            elif option == "5":
                print(self.catalogue.count_juveniles_by_species())
            elif option == "6":
                classis = input("Give class: ")
                print(self.catalogue.give_species_breakdown_for_class(classis))
            elif option == "7":
                print(self.catalogue.all_burned_and_not())


application = BoneatorTextInterface()
application.do()
