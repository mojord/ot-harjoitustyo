import os
from tools.reader import FileReader
from tools.plotter import Plotter

dirname = os.path.dirname(__file__)


class Bonecatalogue:
    """Class for producing statistics from osteological analysis csv:s.
    """

    def __init__(self):
        self.file = []

    def read_file(self, file):
        """Reads csv into a list of Bone objects.
        Args:
            file: User given csv file.
        """
        path = os.path.join(dirname, file)
        reader = FileReader(path)
        self.file = reader.read()

    def show_file(self):
        """Prints the list of Bone objects.
        """
        for bone in self.file:
            print(bone)

    def count_species(self):
        """Counts and prints species found in list.
        Returns:
            Dictionary of species with counts.
        """
        species_list = {}
        for bone in self.file:
            if bone.species != "Indet":
                if bone.species in species_list:
                    species_list[bone.species] += bone.nisp
                if bone.species not in species_list:
                    species_list[bone.species] = bone.nisp
        for key, value in species_list.items():
            print(f"{key}, {value}")
        print(f"{len(species_list)} species")
        return species_list

    def count_nisp_and_weight_by_class(self):
        """Counts and prints the number and weight of finds in each animal class. Calls Plotter for graph.
        Returns:
            Dictionary of classes with counts and weights.
        """
        nisp_weight = {}
        identified = 0
        indets = 0

        for bone in self.file:
            if bone.classis in nisp_weight:
                nisp_weight[bone.classis][0] += int(bone.nisp)
                nisp_weight[bone.classis][1] += float(bone.weight)
            if bone.classis not in nisp_weight:
                nisp_weight[bone.classis] = [int(bone.nisp), float(bone.weight)]

        for key, value in nisp_weight.items():
            value[1] = round(value[1],2)
            print(f"{key}, {value[0]}, {value[1]} grs")

        indets = nisp_weight["Indet"][0]
        identified = nisp_weight["Mammalia"][0]+nisp_weight["Aves"][0]+nisp_weight["Teleostei"][0]

        print(f"{identified} specimens identified by class, {indets} indetermined")

        plot = Plotter()
        plot.bar_chart_nsp_and_weight(nisp_weight)

        return nisp_weight

    def give_species(self, species):
        """Counts and lists bones for given species.

        Args:
            species: User given species.
        Returns:
            Species, number and list of bones in string format.
        """
        count = 0
        bone_list = []
        for bone in self.file:
            if bone.species == species:
                count += 1
                bone_list.append((bone.ossum, bone.findnr))
        return f"{species} specimens: {count}, identified bones: {bone_list}"

    def count_juveniles_by_species(self):
        """Counts juvenile individuals.
        Returns:
            Dictionary of species, number, and number of teeth and articular faces.
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
        """Counts which species are found in given animal class. Calls Plotter for graph.
        Args:
            classis: User given animal class.
        Returns:
            Species in class.
        """
        species_list = {}
        for bone in self.file:
            if bone.classis == classis:
                if bone.species not in species_list:
                    species_list[bone.species] = 0
                species_list[bone.species] += int(bone.nisp)

        plot = Plotter()
        plot.species_breakdown_bar_chart(species_list)

        return species_list

    def all_burned_and_not(self):
        """Counts nsp and weight for not burned and burned bones.
        Returns:
            Number and weight of all bones.
        """
        nsp = 0
        weight = 0
        burned_nsp = 0
        burned_weight = 0

        for bone in self.file:
            nsp += bone.nisp
            weight += bone.weight
            if bone.burndegree != "":
                burned_nsp += bone.nisp
                burned_weight += bone.weight
        weight = round(weight,2)
        burned_weight = round(burned_weight,2)
        not_burned_weight = weight-burned_weight
        not_burned_weight = round(not_burned_weight,2)

        burned_nsp_percent = (burned_nsp / nsp) * 100
        burned_weight_percent = (burned_weight / weight) * 100

        print(f"ALL NSP: {nsp} ALL WEIGHT: {weight} grs\nNOT BURNED NSP: {nsp-burned_nsp} | PER CENT NSP: {100-burned_nsp_percent:.0f} | NOT BURNED WEIGHT: {not_burned_weight} grs | PER CENT WEIGHT: {100-burned_weight_percent:.0f}\nBURNED NSP: {burned_nsp} | PER CENT NSP: {burned_nsp_percent:.0f} | BURNED WEIGHT: {burned_weight} grs | PER CENT WEIGHT: {burned_weight_percent:.0f}")
        return f"ALL: {nsp}, {weight}, NOT BURNED: {nsp-burned_nsp}, {not_burned_weight}"
