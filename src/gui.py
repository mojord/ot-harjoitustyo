
from tkinter import *
from services.bonecatalogue import Bonecatalogue

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
        header_label = Label(
            master=self._root, text="Welcome to Boneator!",
            bg="khaki2", font="HeadingFont 15 bold"
            )

        button_color = "OliveDrab2"
        enter_color = "tan1"
        button_font = "CaptionFont 13 bold"

        header_label.grid(row=0, column=0, columnspan=4, padx=15, pady=15)

        csv_input_label = Label(
            master=self._root, text=" Enter csv filename, e.g. bones.csv.", font=button_font
            )
        self._csv_entry = Entry(master=self._root)
        csv_enterbutton = Button(
            master=self._root, text="Click to enter csv filename.",
            bg=enter_color, bd=5, command=self.handle_csv_entry, font=button_font
            )

        species_input_label = Label(
            master=self._root, text="Enter species to find specimens.", font=button_font
            )
        self._species_entry = Entry(master=self._root)
        species_enterbutton = Button(
            master=self._root, text="Click to enter species.",
            bg=enter_color, bd=5, command=self.handle_species_entry, font=button_font
            )
        
        classis_input_label = Label(
            master=self._root, text="Enter class to find number of identified species.", font=button_font
            )
        self._classis_entry = Entry(master=self._root)
        classis_enterbutton = Button(
            master=self._root, text="Click to enter class.",
            bg=enter_color, bd=5, command=self.handle_classis_entry, font=button_font)

        tester_instructions_label = Label(
            master=self._root, text="NOTE: Please use csv files testaus.csv (simplest), bartsbones.csv or barts2.csv (largest).", font="CaptionFont 15")

        button_quit = Button(master=self._root, text="QUIT", bg="firebrick1",
                             command=self.quit, font="CaptionFont 15 bold")
        button_show_file = Button(master=self._root, text="Show file",
                                  bg=button_color, command=self.handle_show_file_click, font=button_font)
        button_count_species = Button(
            master=self._root, text="Count species",
            bg=button_color, command=self.handle_count_species_click, font=button_font
            )       
        button_count_nisp_and_weight_by_class = Button(
            master=self._root, text="Count nisp and weight",
            bg=button_color, command=self.handle_count_nisp_and_weight_by_class_click, font=button_font
            )
        button_count_juveniles_by_species = Button(
            master=self._root, text="Count juveniles by species",
            bg=button_color, command=self.handle_count_juveniles_by_species_click, font=button_font
            )
        button_all_burned_and_not = Button(
            master=self._root, text="Give breakdown of not burned and burned bones",
            bg=button_color, command=self.handle_all_burned_and_not_click, font=button_font
            )

        csv_input_label.grid(
            row=1, column=0)
        self._csv_entry.grid(row=1, column=1, )
        csv_enterbutton.grid(row=1, column=2)

        species_input_label.grid(
            row=6, column=0)
        self._species_entry.grid(row=6, column=1, )
        species_enterbutton.grid(row=6, column=2, pady=20)

        classis_input_label.grid(
            row=8, column=0, padx=20)
        self._classis_entry.grid(row=8, column=1, )
        classis_enterbutton.grid(row=8, column=2)

        tester_instructions_label.grid(row=30, column=0, columnspan=4, pady=15)

        button_quit.grid(row=10, column=2, pady=20)
        button_show_file.grid(row=2, column=0, pady=20)
        button_count_species.grid(row=2, column=1)
        button_count_nisp_and_weight_by_class.grid(row=4, column=0)
        button_count_juveniles_by_species.grid(
            row=4, column=1, pady=15)
        button_all_burned_and_not.grid(row=2, column=2)

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

    def handle_count_nisp_and_weight_by_class_click(self):
        self.catalogue.count_nisp_and_weight_by_class()

    def handle_count_juveniles_by_species_click(self):
        print(self.catalogue.count_juveniles_by_species())
    
    def handle_all_burned_and_not_click(self):
        self.catalogue.all_burned_and_not()



window = Tk()
window.title("BONEATOR - Statistics for osteologists")

gui = GUI(window)
window.geometry("1450x500")
gui.start()

window.mainloop()
