import numpy as np

filedata=np.genfromtxt('data.txt',delimiter=",")

print(filedata[filedata>50])
