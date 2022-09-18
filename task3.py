# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

arr = []
n = int(input("Введите кол-во чисел в списке "))
for i in range(n):
    arr.append(int(input("Введите число ")))
print(arr)    

arr2 = []
j = 0
count = 0
for j in range(len(arr)): 
    for i in range(len(arr)):
        if arr[j] == arr[i]:
            count = count + 1
        i += 1  
    if count == 1:
        arr2.append(arr[j])
    count = 0                 
    j += 1    
        
print(arr2)        
