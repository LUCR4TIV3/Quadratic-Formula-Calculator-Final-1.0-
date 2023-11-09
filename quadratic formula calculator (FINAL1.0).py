import math

print("Hello, welcome to my quadratic formula calculator")

redoans = input("Press 'y' to begin: ")
while redoans.lower() != "y":
    redoans = input("Press 'y' to begin: ")

while redoans.lower() == "y":
    A = input("What's your A coefficient: ")
    while True:
        try:
            A = float(A)
            break  
        except ValueError:
            print("Incorrect input. Please enter a valid number for A.")
            A = input("What's your A coefficient: ")

    B = input("What's your B coefficient: ")
    while True:
        try:
            B = float(B)
            break  
        except ValueError:
            print("Incorrect input. Please enter a valid number for B.")
            B = input("What's your B coefficient: ")
        
    C = input("What's your C coefficient: ")
    while True:
        try:
            C = float(C)
            break  
        except ValueError:
            print("Incorrect input. Please enter a valid number for C.")
            C = input("What's your C coefficient: ")

   
    discriminant = B*B - 4*A*C

    
    if discriminant < 0:
        print("The equation has no real roots.")
    else:
       
        x1 = (-B + math.sqrt(discriminant)) / (2*A)
        x2 = (-B - math.sqrt(discriminant)) / (2*A)

       
        if abs(x1) > 18000 or abs(x2) > 18000:
            print("The roots are beyond the limits for this calculator.")
        else:
            print("The roots for this equation are:")
            print(x1)
            print("and")
            print(x2)

    redoans = input("Do you want to calculate another equation? (y/n) ")
    while redoans.lower() != "y" and redoans.lower() != "n":
        redoans = input("Please provide a valid input, y/n: ")

if redoans.lower() == "n":
    print("Okay, thanks for using my quadratic formula calculator")
