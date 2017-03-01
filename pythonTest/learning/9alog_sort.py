# O(n ^ 2)
def bubble_sort(list_data):
    for i in range(len(list_data)):
        p = len(list_data) - i - 1
        for j in range(p):
            # swap order if necessary
            if list_data[j] > list_data[j+1]:
                list_data[j], list_data[j+1] = list_data[j+1], list_data[j]
    return list_data

print(bubble_sort([4,3,1,2]))
print(bubble_sort([1,4,2,3]))

def quick_sort(list_data, start, end):
    if start < end:
        i = start
        j = end
        p = (start + end)//2
        pivot = list_data[p]

        while i <= j:
            while list_data[i] < pivot:
                i += 1
            while list_data[j] > pivot:
                j -= 1
            if i <= j:
                # swap
                list_data[i], list_data[j] = list_data[j], list_data[i]
                i += 1
                j -= 1
        if start < j:
            quick_sort(list_data, start, j)
        if end > i:
            quick_sort(list_data, i, end)

li = [4,1,2,3,5,77 , 1, 2, 99, 3]
quick_sort(li, 0, len(li)-1)
print(li)
