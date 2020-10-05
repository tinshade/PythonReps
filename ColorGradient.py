import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def colorGrad(c1,c2,mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)
print("\nEnter the hexadecimal value of the colors you want to create a gradient of.\n")
col1= input("Color 1 : ") #blue
col2=input("Color 2 : ") #green
a = input("\nEnter 'x' for horizontal gradient and 'y' for vertical gradient : ")
n=500

fig, ax = plt.subplots(figsize=(8, 5))
if(a=='x'):
	for x in range(n+1):
	    ax.axvline(x, color=colorGrad(col1,col2,x/n), linewidth=4)
elif(a=='y'):
	for x in range(n+1):
	    ax.axhline(x, color=colorGrad(col1,col2,x/n), linewidth=4)
else:
	print("No input detected for gradient type. Displaying Default Horizontal Gradient")
	for x in range(n+1):
	    ax.axvline(x, color=colorGrad(col1,col2,x/n), linewidth=4) 
plt.show()