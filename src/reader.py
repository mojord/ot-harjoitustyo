 
import csv
from bone import *
#from testbone import *

class FileReader():
    def __init__(self, file):
        self.file = file
    
    def read(self):
        bones = []
        with open(self.file) as f:
            for row in f:
                parts = row.split(";")
                if parts[0] == "nsp":
                    continue
#                numero = parts[0]
#                kuvaus = parts[1]
#                os = parts[2]
#                paaluokka = parts[3]
#                weight = parts[4]
#                bodypart = parts[5]

                        
                nisp = parts[0]
                weight = parts[1]
                classis = parts[2]
                species = parts[3]
                ossum = parts[4]
                element = parts[5]
                side = parts[6]
                fragment = parts[7]
                comment = parts[8]
                sizeclass = parts[9]
                part = parts[10]
                burndegree = parts[11]
                iuv = parts[12]
                cut = parts[13]
                findnr = parts[14]
                x = parts[15]
                y = parts [16]
                context = [17]
                layer = [18]



                bones.append(Bone(nisp, weight, classis, species, ossum, element, side, fragment, comment, sizeclass, part, burndegree, iuv, cut, findnr, x, y, context, layer))

#                bones.append(TestBone(numero, kuvaus, os, paaluokka, weight, bodypart))
        
        return bones

#if __name__ == "__main__":

#    print("toimii")
#    lukija = FileReader("testiluusto.csv")
#    lukija = FileReader("boneatortest.csv")
#    luut = lukija.read()

#    for luu in luut:
#        print(luu)


#        if luu.species != "Indet":
#            print(luu.species)

