"""
storage_efficiency = 
volume/surface_area
In other words, the storage efficiency of a can is the space inside the can divided by the amount of steel required to make the can. The formulas for the volume and surface area of a cylinder are:

volume = π radius2 height
surface_area = 2π radius (radius + height)

"""

import math

can_dict = {
    "1_picnic": {"radius":6.83, "height":10.16, "cost":0.28}, 
    "1_tall": {"radius":7.78, "height":11.91, "cost":0.43},
    "2": {"radius":8.73, "height":11.59, "cost":0.45},
    "2.5": {"radius":10.32, "height":11.91, "cost":0.61},
    "3_cylinder": {"radius":10.79, "height":17.78, "cost":0.86},
    "5": {"radius":13.02, "height":14.29, "cost":0.83},
    "6Z": {"radius":5.40,"height":8.89, "cost":0.22},
    "8Z_short": {"radius":6.83, "height":7.62, "cost":0.26},
    "10": {"radius":15.72, "height":17.78, "cost":1.53},
    "211": {"radius":6.83, "height":12.38, "cost":0.34},
    "300": {"radius":7.62, "height":11.27, "cost":0.38},
    "303": {"radius":8.10, "height":11.11, "cost":0.42}
}

#height = can_dict[nth_key]["height"]



def compute_storage_efficiency(dictionary):
    for key in dictionary:
        vol = dictionary[key]["volume"]
        SA = dictionary[key]["surface area"]

        efficiency = math.pi * vol ** 2 * SA
        can_dict[key]["storage efficiency"] = efficiency
    return 

def compute_cost_efficiency(dictionary):
    for key in dictionary:
        vol = dictionary[key]["volume"]
        height = dictionary[key]["cost"]

        efficiency = vol/height
        can_dict[key]["cost efficiency"] = efficiency
    return


def compute_volume(dictionary):
    for key in dictionary:
        radius = dictionary[key]["radius"]
        height = dictionary[key]["height"]

        volume = math.pi * radius ** 2 * height
        can_dict[key]["volume"] = volume
    return



def compute_surface_area(dictionary):
    for key in dictionary:
        radius = dictionary[key]["radius"]
        height = dictionary[key]["height"]

        surface_area = 2 * math.pi * radius * (radius + height)
        can_dict[key]["surface area"] = surface_area
    return


def main():
    compute_volume(can_dict)
    compute_surface_area(can_dict)
    compute_storage_efficiency(can_dict)
    compute_cost_efficiency(can_dict)
    cost_efficiency = 0
    which_can = None

    for key in can_dict:
        if "cost efficiency" in can_dict[key]:  # Make sure the key exists
            if cost_efficiency < can_dict[key]["cost efficiency"]:
                cost_efficiency = can_dict[key]["cost efficiency"]
                which_can = key

    print(f"{can_dict[which_can]} is the can with the most cost efficiency at {cost_efficiency:.2f} volume per dollar")

main()