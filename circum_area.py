import math
radii = input("What is the radius of the circle :\t")
radii = float(radii)
const = 2*math.pi*radii
print(f"actual result is {float(const)}")
print(f"The round off circumference is {round(const,2)}\n")

area = math.pi*pow(radii,2)
area = float(area)
print(f"Area of the circle is {area} absolutely")
print(f"Area of circle is {round(area,2)} Approximately")
print(f"Area of circle is whole numeric form {math.ceil(area)}")

