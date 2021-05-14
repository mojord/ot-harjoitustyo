import matplotlib.pyplot as plt

class Plotter:
    """Class for creating plots
    """
    def __init__(self):
        self.list = []
        self.dictionary = {}

    def bar_chart_nsp_and_weight(self, dictionary):
        """Creates bar chart for nisp and weight
        """
        labels = []
        heights = []
        for key in dictionary:
            by_nr = key + " nisp"
            by_weight = key + " weight grs"
            labels.append(by_nr)
            labels.append(by_weight)

            number = int(dictionary[key][0])
            weight = float(dictionary[key][1])

            heights.append(number)
            heights.append(weight)

        x_coords = list(range(len(labels)))
        plt.figure(figsize=(15,6))
        plt.bar(x_coords, heights, tick_label = labels, width = 0.8, color = ["orange", "olive"])
        plt.xlabel("classes")
        plt.ylabel("nisp/grs")
        plt.title("Identified classes by nisp and weight")

        plt.show()

    def species_breakdown_bar_chart(self, dictionary):
        """Creates bar chart for species breakdown
        """
        keys = dictionary.keys()
        values = dictionary.values()
        plt.bar(keys, values)
        plt.show()
