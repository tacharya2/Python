x =int(input("Pleae enter a positive number: "))
if x>0:
    if x%2 == 0:
        print("{} is a positive number".format(x))
    else:
        print("The number is odd")
else:
   print("something went wrong")
