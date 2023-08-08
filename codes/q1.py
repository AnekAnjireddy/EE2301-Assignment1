import numpy as np
A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])

D=np.array([(B[0]+C[0])/2, (B[1]+C[1])/2])
E=np.array([(C[0]+A[0])/2, (C[1]+A[1])/2])
F=np.array([(A[0]+B[0])/2, (A[1]+B[1])/2])

print("The parametric of AB form is x:",A,"+ k",D-A)
print("The parametric of BC form is x:",B,"+ k",E-B)
print("The parametric of CA form is x:",C,"+ k",F-C)