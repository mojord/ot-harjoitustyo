import os
from tools.reader import FileReader
from tools.plotter import Plotter

dirname = os.path.dirname(__file__)


class Bonecatalogue:
    """Class for producing statistics from osteological analysis csv:s
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

    def count_nisp_and_weight_by_class(self):
        """Counts and prints the number and weight of finds in each animal class
        """
        nispweight = {}
        identified = 0
        indets = 0

        for bone in self.file:
            if bone.classis in nispweight:
                nispweight[bone.classis][0] += int(bone.nisp)
                nispweight[bone.classis][1] += float(bone.weight)
            if bone.classis not in nispweight:
                nispweight[bone.classis] = [int(bone.nisp), float(bone.weight)]

        for key, value in nispweight.items():
            print(f"{key}, {value[0]}, {round(value[1],2)} grs")

        indets = nispweight["Indet"][0]
        identified = nispweight["Mammalia"][0]+nispweight["Aves"][0]+nispweight["Teleostei"][0]

        print(f"{identified} specimens identified by class, {indets} indetermined")

        plot = Plotter()
        plot.bar_chart_nsp_and_weight(nispweight)

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
        """Counts juvenile individuals.
        Returns:
            Species, number, and number of teeth and articular faces in string format.
        """
        juveniles = {}
        for bone in self.file:
            if bone.iuv == "iuv":
                if bone.species in juveniles:
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
        print("Species: [nsp, number of teeth, number of epiphyses or articular faces]")
        return juveniles

    def give_species_breakdown_for_class(self, classis):
        """Counts which species are found in given animal class.
        Args:
            Animal class.
        Returns:
            Species in class.
        """
        specieslist = {}
        for bone in self.file:
            if bone.classis == classis:
                if bone.species not in specieslist:
                    specieslist[bone.species] = 0
                specieslist[bone.species] += int(bone.nisp)

        plot = Plotter()
        plot.species_breakdown_bar_chart(specieslist)

        return specieslist

    def all_burned_and_not(self):
        """Counts nsp and weight for not burned and burned bones.
        Returns:
            Number and weight of all bones.
        """
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

        print(f"ALL NSP: {nsp} ALL WEIGHT: {weight} grs\nNOT BURNED NSP: {nsp-burnednsp} | PER CENT NSP: {100-burned_nsp_percent:.0f} | NOT BURNED WEIGHT: {weight - burnedweight} grs | PER CENT WEIGHT: {100-burned_weight_percent:.0f}\nBURNED NSP: {burnednsp} | PER CENT NSP: {burned_nsp_percent:.0f} | BURNED WEIGHT: {burnedweight} grs | PER CENT WEIGHT: {burned_weight_percent:.0f}")
        return f"ALL: {nsp}, {weight}, NOT BURNED: {nsp-burnednsp}, {weight-burnedweight}"
