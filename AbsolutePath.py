#FIND THE ABSOLUTE PATH OF A FILE WITH PYTHON
import os #To interact with the underlying OS

path = os.path.dirname(os.path.abspath(__file__)) #Storing the path to the current file in "path" variable
print(path) #Printing the absolute path