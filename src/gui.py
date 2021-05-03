
from tkinter import *
from bonecatalogue import *


class GUI:
    """Class for graphic interface.
    """
    def __init__(self, root):
        self._root = root
        self.catalogue = Bonecatalogue()
        self._csv_entry = None
        self._species_entry = None
        self._classis_entry = None

    def start(self):
        headerlabel = Label(master=self._root, text="Welcome to Boneator!",
                            bg="orange", font="HeadingFont 20 bold")
        buttoncolor = "pale green"
        entercolor = "SteelBlue1"
        buttonfont = "CaptionFont 13 bold"

        csv_input_label = Label(
            master=self._root, text=" Enter csv filename, e.g. bones.csv.", font=buttonfont)
        self._csv_entry = Entry(master=self._root)
        csv_enterbutton = Button(master=self._root, text="Click to enter csv filename.",
                                 bg=entercolor, bd=5, command=self.handle_csv_entry, font=buttonfont)

        species_input_label = Label(
            master=self._root, text="Enter species to find specimens.", font=buttonfont)
        self._species_entry = Entry(master=self._root)
        species_enterbutton = Button(master=self._root, text="Click to enter species.",
                                     bg=entercolor, bd=5, command=self.handle_species_entry, font=buttonfont)
        
        classis_input_label = Label(
            master=self._root, text="Enter class to find number of identified species.", font=buttonfont)
        self._classis_entry = Entry(master=self._root)
        classis_enterbutton = Button(master=self._root, text="Click to enter class.",
                                     bg=entercolor, bd=5, command=self.handle_classis_entry, font=buttonfont)

        testerInstructions_label = Label(
            master=self._root, text="NOTE: Please use csv files testaus.csv (simplest), bartsbones.csv or barts2.csv (largest).", font="CaptionFont 15")

        button_quit = Button(master=self._root, text="QUIT", bg="firebrick1",
                             command=self.quit, font="CaptionFont 15 bold")
        button_show_file = Button(master=self._root, text="Show file",
                                  bg=buttoncolor, command=self.handle_show_file_click, font=buttonfont)
        button_count_species = Button(master=self._root, text="Count species",
                                      bg=buttoncolor, command=self.handle_count_species_click, font=buttonfont)
        button_count_nisp_by_class = Button(master=self._root, text="Count nisp by class",
                                            bg=buttoncolor, command=self.handle_count_nisp_by_class_click, font=buttonfont)
        button_count_nisp_and_weight = Button(master=self._root, text="Count nisp and weight",
                                              bg=buttoncolor, command=self.handle_count_nisp_and_weight_click, font=buttonfont)
        button_count_juveniles_by_species = Button(master=self._root, text="Count juveniles by species",
                                                   bg=buttoncolor, command=self.handle_count_juveniles_by_species_click, font=buttonfont)

        csv_input_label.grid(
            row=1, column=0, sticky=(constants.E, constants.W))
        self._csv_entry.grid(row=1, column=1, )
        csv_enterbutton.grid(row=1, column=2)

        species_input_label.grid(
            row=6, column=0, sticky=(constants.E, constants.W))
        self._species_entry.grid(row=6, column=1, )
        species_enterbutton.grid(row=6, column=2)

        classis_input_label.grid(
            row=8, column=0, sticky=(constants.E, constants.W))
        self._classis_entry.grid(row=8, column=1, )
        classis_enterbutton.grid(row=8, column=2)

        testerInstructions_label.grid(row=30, column=0, columnspan=4, pady=15)

        button_quit.grid(row=10, column=2, pady=20)
        button_show_file.grid(row=2, column=0, pady=20)
        button_count_species.grid(row=2, column=1)
        button_count_nisp_by_class.grid(row=2, column=2)
        button_count_nisp_and_weight.grid(row=4, column=0)
        button_count_juveniles_by_species.grid(
            row=4, column=1, pady=15, sticky=(constants.W))


#        self._root.grid_columnconfigure(0, weight=1, minsize=300)


    def quit(self):
        self._root.destroy()

    def handle_csv_entry(self):
        csv_name = self._csv_entry.get()
        self.catalogue.read_file(csv_name)

    def handle_species_entry(self):
        species_name = self._species_entry.get()
        print(self.catalogue.give_species(species_name))

    def handle_classis_entry(self):
        classis_name = self._classis_entry.get()
        print(self.catalogue.give_species_breakdown_for_class(classis_name))

    def handle_show_file_click(self):
        self.catalogue.show_file()

    def handle_count_species_click(self):
        self.catalogue.count_species()

    def handle_count_nisp_by_class_click(self):
        self.catalogue.count_nisp_by_class()

    def handle_count_nisp_and_weight_click(self):
        self.catalogue.count_nisp_and_weight()

    def handle_count_juveniles_by_species_click(self):
        print(self.catalogue.count_juveniles_by_species())



window = Tk()
window.title("Boneator")

gui = GUI(window)
window.geometry("1100x600")
gui.start()

window.mainloop()
