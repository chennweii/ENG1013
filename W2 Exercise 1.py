import math

A = input("Length of side A: ")
B = input("Length of side B: ")
C = input("Length of side C: ")

if not A:
    B, C = int(B), int(C) # Convert B and C to integer to be able to use the power operator **
    missLength = math.sqrt((C**2) - (B**2))
    print(f"Given Side B = {B}, Side C = {C}") 
    print(f"Calculated: Side A = {missLength:.4f}")
    
elif not B:
    A, C = int(A), int(C)
    missLength = math.sqrt((C**2) - (A**2))
    print(f"Given Side A = {A}, Side C = {C}")
    print(f"Calculated: Side B = {missLength:.4f}")

elif not C:
    A, B = int(A), int(B)
    missLength = math.sqrt((A**2) + (B**2))
    print(f"Given Side A = {A}, Side B = {B}")
    print(f"Calculated: Side C = {missLength:.4f}")
else:
    print("All sides are given! Nothing to calculate here.")
