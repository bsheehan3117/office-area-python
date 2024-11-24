'''
    CS5001
    Spring 2023
    HW1

    Brendan Sheehan

    This program calculates the area of an office in square meters and
    the cost per square meter from am given length and width in feet.
'''

def main():

    # input office length and width in feet
    length_in_feet = float(input("Enter the length of the office (in feet)"))  
    width_in_feet = float(input("Enter the width of the office (in feet)"))

    # length * width, feet to meters, calculate cost per square meter
    office_area_in_feet = length_in_feet * width_in_feet  
    office_area_in_meters = office_area_in_feet * 0.092903                
    euros_per_square_meter = office_area_in_meters * 21.10             
    
    # print office area in square ft, square meters , and amount per month
    print(f"The area of the office is {office_area_in_feet:.2f} square feet")  
    print(f"...which is {office_area_in_meters:.2f} square meters")
    print(f"......and you will pay €{euros_per_square_meter:.2f} per month")


if __name__ == "__main__":
    main() 
