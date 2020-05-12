#search for 9
def search(arr,n):
    i = 0
    while i<len(arr):
        if arr[i] == n:
            return True
        i = i+1
    return False

arr = [5, 8, 4, 6, 9, 2]
n = int(input("enter a number to check: "))
if search(arr,n):
    print("It exists")
else:
    print("It does not exists")