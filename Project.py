from pyexpat import model
import sys

Type = sys.argv[1]
Brand = sys.argv[2]
Model = sys.argv[3]


if Type == "A":
    if Brand == "A":
        if Model == "A":
            print("You enjoyed your drive in your Merecedes-Maybach S650")
        elif Model == "B":
            print("You enjoyed your drive in your Merecedes-Maybach S560")
    if Brand == "B":
        if Model == "A":
            print("You enjoyed your drive in your Rolls-Royce Phantom")
        elif Model == "B":
            print("You enjoyed your drive in your Rolls-Royce Ghost")
elif Type == "B":
    if Brand == "A":
        if Model == "A":
            print("You enjoyed your seaside drive in your Lamborghini Huracan Evo Spyder")
        elif Model == "B":
            print("You enjoyed your track-day in your Lamborghini Aventador SVJ Roadster")
    if Brand == "B":
        if Model == "A":
            print("You enjoyed the backroads on your drive in your Ferrari F8 Tributo")
        elif Model == "B":
            print("You enjoyed your drive to the beach house in your Ferrari Portofino M")