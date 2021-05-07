#import sqlite3
import os
from tools.reader import *
from tools.plotter import Plotter
#db = sqlite.connect("testi.db")
#db.isolation_level = None

dirname = os.path.dirname(__file__)


class Bonecatalogue:
    """Class for producing statistics from osteological analysis csv
    """

    def __init__(self):
        self.file = []

    def read_file(self, file):
        """Reads csv into a list of bone objects
        Args:
            file: given csv file
        """
        path = os.path.join(dirname, file)
        reader = FileReader(path)
        self.file = reader.read()

    def kokeilu(self):
        """A provisional mystery method for testing tests
        Returns:
            Buenos dias string
        """
        return f"buenos dias"

    def show_file(self):
        """Prints the list of bone objects
        """
        for bone in self.file:
            print(bone)

    def count_species(self):
        """Counts and prints species found in list
        """
        specieslist = {}
        for bone in self.file:
            if bone.species != "Indet":
                if bone.species in specieslist:
                    specieslist[bone.species] += bone.nisp
                if bone.species not in specieslist:                
                    specieslist[bone.species] = bone.nisp
        for key, value in specieslist.items():
            print(f"{key}, {value}")
        print(f"{len(specieslist)} species")

    def count_nisp_and_weight(self):
        """Counts and prints the number and weight of finds in each animal class
        """ 
        nispweight = {}
        for bone in self.file:
            if bone.classis in nispweight:
                nispweight[bone.classis][0] += int(bone.nisp)
                nispweight[bone.classis][1] += float(bone.weight)
            if bone.classis not in nispweight:
                nispweight[bone.classis] = [int(bone.nisp), float(bone.weight)]
        for key, value in nispweight.items():
            print(f"{key}, {value}")

        plot = Plotter()
        plot.bar_chart_nsp_and_weight(nispweight)

    def count_nisp_by_class(self):
        nispclasses = {}
        identified = 0
        indets = 0
        for bone in self.file:
            if bone.classis in nispclasses:
                nispclasses[bone.classis] += int(bone.nisp)
            if bone.classis not in nispclasses:
                nispclasses[bone.classis] = int(bone.nisp)
        indets = nispclasses["Indet"]
        for key, value in nispclasses.items():
            print(f"{key}, {value}")
            if key != "Indet":
                identified += int(value)
        print(f"{identified} specimens identified by class, {indets} indetermined")
        plot = Plotter()
        plot.classis_bar_chart(nispclasses)

    def give_species(self, species):
        """Counts and lists bones for given species.
        Returns:
            Species, number and list of bones in string format
        """
        count = 0
        bonelist = []
        for bone in self.file:
            if bone.species == species:
                count += 1
                bonelist.append((bone.ossum, bone.findnr))
        return f"{species} specimens: {count}, identified bones: {bonelist}"

    def count_juveniles_by_species(self):
        juveniles = {}
#        name = ""
        for bone in self.file:
            if bone.iuv == "iuv":
                if bone.species in juveniles:
                    #                if bone.species == "Indet":
                    #                    name = bone.classis
                    #                else:
                    #                    name = bone.species
                    #                if name not in juveniles:
                    #                    juveniles[name][0] = 0
                    #                juveniles[name][0] += 1
                    juveniles[bone.species][0] += int(bone.nisp)
                    if "dens" in bone.ossum:
                        juveniles[bone.species][1] += int(bone.nisp)
                    if "epiph" in bone.element:
                        juveniles[bone.species][2] += int(bone.nisp)
                if bone.species not in juveniles:
                    juveniles[bone.species] = [int(bone.nisp), 0, 0]
                    if "dens" in bone.ossum:
                        juveniles[bone.species][1] = int(bone.nisp)
                    if "epiph" in bone.element:
                        juveniles[bone.species][2] = int(bone.nisp)
        for key in juveniles:
            count = 0
            bonename = key
            no = juveniles[key][0]
            teethno = juveniles[key][1]
            epiphysesno = juveniles[key][2]
            return f"{bonename} {no} specimens of which {teethno} teeth and {epiphysesno} epiphyses or juvenile articular faces"
    
    def give_species_breakdown_for_class(self, classis):
        specieslist = {}            
        for bone in self.file:
            if bone.classis == classis:
                if bone.species not in specieslist:
                    specieslist[bone.species] = 0
                specieslist[bone.species] += int(bone.nisp)
        for key, value in specieslist.items():
            print(f"{key}, {value}")
        
        plot = Plotter()
        plot.species_breakdown_bar_chart(specieslist)

    def all_burned_and_not(self):
        nsp = 0
        weight = 0
        burnednsp = 0
        burnedweight = 0
        
        for bone in self.file:
            nsp += bone.nisp
            weight += bone.weight
            if bone.burndegree != "":
                burnednsp += bone.nisp
                burnedweight += bone.weight
        
        burned_nsp_percent = (burnednsp / nsp) * 100
        burned_weight_percent = (burnedweight / weight) * 100

        return f"ALL NSP: {nsp} ALL WEIGHT: {weight} grs\nNOT BURNED NSP: {nsp-burnednsp} | PER CENT NSP: {100-burned_nsp_percent:.0f} | NOT BURNED WEIGHT: {weight - burnedweight} grs | PER CENT WEIGHT: {100-burned_weight_percent:.0f}\nBURNED NSP: {burnednsp} | PER CENT NSP: {burned_nsp_percent:.0f} | BURNED WEIGHT: {burnedweight} grs | PER CENT WEIGHT: {burned_weight_percent:.0f}"