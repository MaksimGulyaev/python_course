numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
k=0
sum=0
for i in range (0, len(numbers)):
    if numbers[i] ==None:
        k=i
        i=i+1
    else:
        sum=sum+numbers[i]

Sr=sum/(len(numbers))
numbers[k]=Sr


print("Измененный список:", numbers)
