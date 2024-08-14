# Importing whole module
import operations

# importing only particular things
from bioData import name, age

print(operations.sum)
print(operations.mul)

print("Your name is %s and age is %d "%(name,age))