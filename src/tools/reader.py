from bone import Bone

class FileReader():
    """Class for reading csv files into a list of Bone objects.
    """
    def __init__(self, file):
        self.file = file

    def read(self):
        """Reads csv file into Bone objects.
        Returns:
            List of Bone objects.
        """
        bones = []
        try:
            with open(self.file) as fname:
                for row in fname:
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
                    x = parts[15] # pylint: disable=invalid-name
                    y = parts[16] # pylint: disable=invalid-name
                    context = parts[17]
                    layer = int(parts[18])

                    bones.append(Bone(nisp, weight, classis, species, ossum, element, side, fragment, comment, sizeclass, part, burndegree, iuv, cut, findnr, x, y, context, layer))
        except FileNotFoundError:
            raise FileNotFoundError("The specified file was not found. Please check that the file is located in the services directory and its name spelled correctly.")
        
        return bones
