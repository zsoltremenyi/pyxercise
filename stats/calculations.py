from math import sqrt


class Calculations:
    def __init__(self, num_list):
        self.num_list = num_list

    def mean(self):
        return sum(self.num_list)/len(self.num_list)

    def standard_dev(self):
        return sqrt(sum([pow(self.mean() - x, 2) for x in self.num_list])/len(self.num_list))