def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(len(arr) - 1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr
        
def insertion_sort(arr):
  for i in range(len(arr)):
    key = arr[i]
    pos = i
    while pos > 0 and arr[pos - 1] > key:
      arr[pos] = arr[pos - 1]
      pos = pos - 1
    arr[pos] = key
  return arr

def selection_sort(arr):        
  for i in range(len(arr)):
    minimum = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[minimum]:
        minimum = j
    arr[minimum], arr[i] = arr[i], arr[minimum]
  return arr

arr1 = [5,6,2,4,8,1]
arr2 = [6,2,6,4,5,5,1,2]
arr3 = [9,8,7,6,5,4,3,2,1]

print("arr before calling bubble_sort(arr):%s" %(arr1))
print("arr after calling bubble_sort(arr): %s" %(bubble_sort(arr1)))
print("arr before calling insertion_sort(arr):%s" %(arr2))
print("arr after calling insertion_sort(arr): %s" %(insertion_sort(arr2)))
print("arr before calling selection_sort(arr):%s" %(arr3))
print("arr after calling selection_sort(arr): %s" %(selection_sort(arr3)))
