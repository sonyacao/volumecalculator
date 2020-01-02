"""
Sonya Cao
COMPSCI 1026
BAUER
10/16/19
Volume Calculator: program prompts computes the volume for cubes, pyramids and ellipsoids
"""
from volume import volume_calc #imports the volume calculating function from the volume file
from summarize import summarize #imports summarize function from the summarize file
from summarize import output_list #imports output list function from the summarize file

def format_input(text_line):  #allows the program to accept both uppercase, lowercase and leading and trailing characters for inputted menu items
    text_line = text_line.lower().strip()
    word_list = text_line.split()
    text_line = " ".join(word_list)
    return text_line

#creating a list for subes, pyramids and ellipsoids
clist = []
plist = []
elist = []

testNumber = int(input("Please enter test number"))

while True:
    shape = input("Please enter a shape or quit")
    shape = format_input(shape)

    #depending on the user input, a volume will be calculated and added to its respective list
    if shape == "cube" or shape == "c":
        clist.append(volume_calc("c"))
    elif shape == "pyramid" or shape == "p":
        plist.append(volume_calc("p"))
    elif shape == "ellipsoid" or shape == "e":
        elist.append(volume_calc("e"))
    elif shape == "quit" or shape == "q": #session will end if user inputs quit or q
        break
    else: #if invalid input is entered, user is prompted to try again
        print("Invalid shape, please try again")

#sorting the lists from least to greatest volume
clist.sort()
plist.sort()
elist.sort()
summarize(clist, plist, elist, testNumber) #summarize will output a file with the results

print("You have reached the end of your session.")

#printing the complete lists of volumes for each shape e
if len(clist) == 0 and len(plist) == 0 and len(elist) == 0:
    print("You did not perform any volume calculations")
else:
    print("The volumes calculated for each shape are:")
    if len(clist) > 0:
        print("Cube: ", str(clist)[1:-1])
    else:
        print("Cube: No shapes entered")

    if len(plist) > 0:
        print("Pyramid: ", str(plist)[1:-1])
    else:
        print("Pyramid: No shapes entered")

    if len(elist) > 0:
        print("Ellipsoid: ", str(elist)[1:-1])
    else:
        print("Ellipsoid: No shapes entered")


