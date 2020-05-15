# finding factors of a user's number
n = int(input("Enter number for it factors: "))
def find_factors(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end = ", ")
find_factors(n)

