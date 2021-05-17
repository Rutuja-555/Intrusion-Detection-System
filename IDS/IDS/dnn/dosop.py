import numpy as np
import matplotlib.pyplot as pp
data=np.genfromtxt('dos.txt',delimiter=',')
print(data)
sum=0
subj=["Accuracy","Precision","Recall","F1 Score"]
for i in data:
	print(i)
pp.plot(data)
pp.title("DOS")
pp.xlabel("Actual Value")
pp.ylabel("predicted Value")
pp.legend(subj)
pp.show()