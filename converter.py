# Maribel Matos

# This program is intended to be used to convert the mass of an unspecified object into kilograms
#The end-user is initially prompted to input the mass of an object

# this variable initiates the concept of the object's mass and also prompts the user for input for said mass
mass=float(input("Object Mass: "))

#this variable contains the converted weight of the object's mass from the initial measurement into kilograms and also does the calculations to convert it
kgs=mass*9.8

print ("Object weight in kilograms: "+str(kgs)+ "kgs")
