import math
a = float(input("Enter first coefficient (a): "))
b = float(input("Enter the second coefficient (b):"))
c = float(input("Enter third coefficient (c): "))
delta = math.sqrt(b*b-4*a*c)
if delta>0.0:
    x1 = (-b+delta)/(2*a)
    x2 = (-b-delta)/(2*a)
    print("The roots are[{0:0.3f}, {1:0.3f}]".format(x1,x2))
elif delta == 0:
    x1 = -b/(2*a)
    x2 = x1
    print("The roots are[{0:0.3f}, {1:0.3f}]".format(x1,x2))
else:
    print("The roots are complex")