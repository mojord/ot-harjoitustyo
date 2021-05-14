import os
import csv
from bone import Bone


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

                nisp = int(parts[0])
                weight = float(parts[1])
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
                findnr = int(parts[14])
                x = parts[15]
                y = parts[16]
                context = parts[17]
                layer = int(parts[18])

                bones.append(Bone(nisp, weight, classis, species, ossum, element, side, fragment,
                             comment, sizeclass, part, burndegree, iuv, cut, findnr, x, y, context, layer))


        return bones
