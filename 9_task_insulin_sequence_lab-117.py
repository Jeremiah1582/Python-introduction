import pandas as pd 
import numpy as np 

data=str(open("./data-sets/preproinsulin-seq.txt").read())
data= data.replace(" ","").replace("1","").replace("6", "").replace("//","")

data.close()

print(data)

