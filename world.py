# Evan Sauers
# CIS-125-82A
# Collaborated with Marisa Gross, Rebekah Orth, and Dr.Neumann
# world.py

# Populate Function, world & height & weight parameters, returns a value
def populate(world,h,w):
    pass

# Display Function, world & height & weight parameters, returns a value
def display(world,h,w):
    pass

# Generation Function, world & height & weight parameters, returns a value
def generation(world,h,w):
    pass
#Add main, set the height and width
def main():
    import random
    height = 80
    width = 22
    world = []
    
    populate(world,height,width)

#Prompt the user to enter a key
    x = input("Enter the Q key to quit.")
    while x != "Q":
    
        display(world,height,width)
    
        generation(world,height,width)
    
        x = input("Enter the Q key to quit.")
        
