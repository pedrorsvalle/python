import math

a= float(input(" digite o  do primeiro coeficiente "))
b= float(input(" digite o  do segundo coeficiente"))
c= float(input(" difite o  do terciro coeficiente"))

if(a ==0):
    print("a equação não é do segundo grau")

else:
    delta= float(pow (b,2) - 4*a*c)

if (delta < 0):
    print("não existe raiz real")

elif delta ==0:
    r1== -b/2
    print ("r1, r2")

else:
    r1= -b + math.sqrt(delta) / 2*a
    ra= -b - match.sqrt(delta) / 2*a
    print ("r1" , r1)
    print ("r2",r2)       
                      
