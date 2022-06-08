from pyexpat import model
import sys
from tkinter import Place
import time

def carselection():
    Type = input("Enter the type of the vehicle(A = Sedan or B = Converible): ")

    if Type == "A" or Type == "a":
        Brand = input("Enter the type of the vehicle(A = Merecedes-Maybach or B = Rolls-Royce): ")
        if Brand == "A" or Brand == "a":
            Model = input("Enter the model of the vehicle(A = S650 or B = S560): ")
            if Model == "A" or Model == "a":
                print("You have selected your Merecedes-Maybach S650")
            elif Model == "B" or Model == "b":
                print("You have selected your Merecedes-Maybach S560")
        if Brand == "B" or Brand == "b":
            Model = input("Enter the model of the vehicle(A = Phantom or B = Ghost): ")
            if Model == "A" or Model == "a":
                print("You have selected your Rolls-Royce Phantom")
            elif Model == "B" or Model == "b":
                print("You have selected your Rolls-Royce Ghost")
    elif Type == "B" or Type == "b":
        Brand = input("Enter the type of the vehicle(A = Lamborghini or B = Ferrari): ")
        if Brand == "A" or Brand == "a":
            Model = input("Enter the model of the vehicle(A = Aventador SVJ Roadster or B = Huracan Evo Spyder): ")
            if Model == "A" or Model == "a":
                print("You have selected your Lamborghini Huracan Evo Spyder")
            elif Model == "B" or Model == "b":
                print("You have selected your Lamborghini Aventador SVJ Roadster")
        if Brand == "B" or Brand == "b":
            Model = input("Enter the model of the vehicle(A = F8 Tributo or B = Portofino M): ")
            if Model == "A"or Model == "a":
                print("You have selected your Ferrari F8 Tributo")
            elif Model == "B" or Model == "b":
                print("You have selected your Ferrari Portofino M")
    else:
        print("Invalid input")
        carselection()
    
    drive()
            

def drive():
    Place = input("Enter the place of the vehicle(A = Downtown LA, B = PCH, C = Beverly Hills Service Center, D = Offroading near Lake Los Angeles, E = Pasadena, G = end): ")
    if Place == "A" or Place == "a":
        print("You saw all of the Downtown LA skyscrapers")
        print("You have completed your trip to Downtown LA")
        time.sleep(5)
        drive()
    elif Place == "B" or Place == "b":
        print("You drove down the PCH")
        print("You have completed your trip to the PCH")
        time.sleep(5)
        drive()
    elif Place == "C" or Place == "c":
        print("You have completed your trip to the Beverly Hills Service Center")
        YN1 = input("Would you like to switch your vehicle(Y = Yes or N = No): ")
        if YN1 == "Y" or YN1 == "y":
            carselection()
        elif YN1 == "N" or YN1 == "n":
            drive()
    elif Place == "D" or Place == "d":
        print("You have fun in the sand")
        print("You have completed your trip to Offroading near Lake Los Angeles")
        time.sleep(5)
        drive()
    elif Place == "E" or Place == "e":
        print("You pass Pasadena City Hall")
        print("You have completed your trip to Pasadena")
        time.sleep(5)
        drive()
    elif Place == "G" or Place == "g":
        print("Thank you for playing!")
        sys.exit()

carselection()
