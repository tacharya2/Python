import cmath
num = 1+2j
num_sq_root = cmath.sqrt(num)
print("The sq.root of {0} is {1:0.3f}+{2:.3f}j".format(num,num_sq_root.real, num_sq_root.imag))