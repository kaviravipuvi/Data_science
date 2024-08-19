
"""pyhton error on remove function"""
lis=[1,2,3,6,5,4]
for num in lis:
    if num in range(2,4):
        lis.remove(num)
print(lis)

a = [1,2,3,4,5]
b = [11,12,13,14,15]
c = [a, b]
print('list of lists',c)

new_list = [num for num in range(50) if  num > 0 and num % 2 == 0]

print(new_list)

li=[letter.upper() for letter in"kaviyarasan"]
print(li)

arr = [[1,2,3,4], [5,6,7,8]]
arr_lst1 = [num for ele in arr for num in ele]
print(arr_lst1)



arrli=[]
for kav in arr:
    print(kav)
    print(*kav)
    for ew in kav:
        arrli.append(ew)
print(arrli)



arr = [[1,2,3,4], [5,6,7,8]]
print('arr = ', arr, '*arr = ', *arr)