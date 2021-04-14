#import sqlite3
import os
from reader import *
from plotter import *
#db = sqlite.connect("testi.db")
#db.isolation_level = None

dirname = os.path.dirname(__file__)

class Bonecatalogue:
    
    def __init__(self):
        self.file = []

    def read_file(self, file):
        path = os.path.join(dirname, file)
        reader = FileReader(path)
        self.file = reader.read()
    
    def show_file(self):
        for bone in self.file:
            print(bone)

    def count_species(self):
        specieslist = {}
        for bone in self.file:
            if bone.species != "Indet":
                if bone.species not in specieslist:
                    specieslist[bone.species] = 0
                specieslist[bone.species] += 1
        for key, value in specieslist.items():
            print(f"{key}, {value}")
        print(f"{len(specieslist)} species")
    
    def count_nisp_and_weight(self):
        nispweight = {}
        for bone in self.file:            
            if bone.classis in nispweight:
                nispweight[bone.classis][0] += int(bone.nisp)
                nispweight[bone.classis][1] += float(bone.weight)
            if bone.classis not in nispweight:
                nispweight[bone.classis] = [int(bone.nisp), float(bone.weight)]
        for key, value in nispweight.items():
            print(f"{key}, {value}")

#        plot = Plotter()
#        plot.bar_chart_nsp_and_weight(nispweight)

    
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
 #       plot = Plotter()
 #       plot.classis_bar_chart(nispclasses)

    def give_species(self, species):
        count = 0
        bonelist = []
        for bone in self.file:
            if bone.species == species:
                count += 1
                bonelist.append((bone.ossum, bone.findnr))
        print(f"{species} specimens: {count}, identified bones: {bonelist}")


    

    
