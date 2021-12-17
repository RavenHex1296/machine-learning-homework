import math

class DecisionTree():
    def __init__(self, dataset):
        self.data = dataset
        self.possible_splits = self.get_all_possible_splits()
        self.best_split = self.get_best_split()

    def calculate_entropy(self, p1, p2):
        return -p1 * math.log(p1, math.e) - p2 * math.log(p2, math.e)

    def get_all_unique_x_values(self):
        return [data[0] for data in dataset if data[0] not in x_values]

    def get_all_unique_y_values(self):
        return [data[1] for data in dataset if data[1] not in y_values]

    def get_all_possible_splits(self):
        possible_splits = {}
        x_values = self.get_all_unique_x_values().sort()
        y_values = self.get_all_unique_y_values().sort()

        for n in range(len(x_values)):
            try:
                possible_splits[0].append((x_values[n] + x_values[n + 1]) / 2)
                possible_splits[1].append((y_values[n] + y_values[n + 1]) / 2)

            except:
                continue

        return possible_splits


    def get_best_split():
        for split in self.possible_splits():


