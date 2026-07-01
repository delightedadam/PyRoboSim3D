import numpy as np
import copy


#there is an example for how to create an arm and "robotis" is his name 
class robotis:
    def __init__(self, start):
        self.depart = start
        self.axes = ["id", "z", "y", "y", "y", "z", "y"]
        self.vectors = [
            np.array([0,  0, 10]), # V0
            np.array([0, 10, 11]), # v1
            np.array([0,  0, 22]), # V2
            np.array([0,  0, 27]), # V3
            np.array([0, 10,  7]), # V5
            np.array([0, 10,  9]), # V6
            np.array([0, 14,  0]), #the plier 
        ]
        self.couleurs = [
            "black",
            "blue",
            "orange",
            "green",
            "purple",
            "black",
            "blue",
        ]
        self.repos_angles = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.angles = copy.deepcopy(self.repos_angles)
