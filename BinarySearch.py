pos = -1
def search(array,n):
    l = 0
    u = len(array) - 1
    while l<=u:
        mid = (l+u) // 2
        if array[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if array[mid]<n:
                l = mid+1
            else:
                u = mid-1
    return False
array = [123, 197, 236, 391, 456, 532, 684, 777, 836, 925, 1147, 1987]
# The data is unsorted. How can we sort and use it for binary search?
#array = array1.sort()
n = int(input("Enter a number to search: "))
if search(array, n):
    print("The number exists at position ", pos+1)
else:
    print("the search number does not exists")