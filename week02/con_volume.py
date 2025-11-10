  
import math

def main():
    #call the cone volume function to compute the volume of the cone
    ex_radius = 2.8
    ex_heigth = 3.2
    ex_vol = cone_volume(ex_radius, ex_heigth)

    #print several lines that describe this program.
    print("This program computes the volume of the right.")
    print("circul cone. For example if the of a")
    print(f"cone is {ex_radius} and heigth is {ex_heigth}")
    print(f"the volume is {ex_vol:.2f}")

    #get the radius and heigth of the cone from the user.
    radius = float(input("Please enter the radius of the cone: "))
    heigth = float(input("Plaese enter the heigth ot the cone: "))

    #Call the cone volume function to compute the volume
    #for the radius and heigth that come from the user.
    vol = cone_volume(radius, heigth)

    #print the radius heigth and vlume for the user to see
    print(f"radius: {radius}")
    print(f"eigth: {heigth}")
    print(f"volume: {vol:.2f}")

def cone_volume(radius, heigth):
    """
    Compute and and return the volume of a right circular cone.
    """
    volume = math.pi * radius**2 * heigth / 3
    return volume
main()