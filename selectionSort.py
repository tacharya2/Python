def selectionSort(lst):
    for i in range(len(lst)):
        mins_position = i
        for j in range(i,len(lst)):
            if lst[j]<lst[mins_position]:
                mins_position = j
        temp = lst[i]
        lst[i] = lst[mins_position]
        lst[mins_position] = temp
lst = [3, 1, 9, 10, 15, 18, 21, 30, 18, 5]
selectionSort(lst)
print(lst)