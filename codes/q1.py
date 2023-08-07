import numpy as np
A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])

print("The parametric of AB form is x:",A,"+ k",B-A)
print("The parametric of BC form is x:",B,"+ k",C-B)
print("The parametric of CA form is x:",C,"+ k",A-C)