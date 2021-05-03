#import matplotlib.pyplot as plt

class Plotter:
    def __init__(self):
        self.list = []
        self.dictionary = {}

    def classis_bar_chart(self, dictionary):
        keys = dictionary.keys()
        values = dictionary.values()
#        plt.bar(keys, values)
#        plt.show()

    def bar_chart_nsp_and_weight(self, dictionary):
        labels = []
        heights = []
        for key in dictionary:
            by_nr = key + " nisp"
            by_weight = key + " weight"
            labels.append(by_nr)
            labels.append(by_weight)

            number = int(dictionary[key][0])
            weight = float(dictionary[key][1])

            heights.append(number)
            heights.append(weight)

        x_coords = list(range(len(labels)))

#        plt.bar(x_coords, heights, tick_label = labels, width = 0.8, color = ["blue", "green"])
#        plt.xlabel("xtest")
#        plt.ylabel("ytest")
#        plt.title("Identified classes by nisp and weight")


#        plt.show()

    def species_breakdown_bar_chart(self, dictionary):
        keys = dictionary.keys()
        values = dictionary.values()
#        plt.bar(keys, values)
#        plt.show()
