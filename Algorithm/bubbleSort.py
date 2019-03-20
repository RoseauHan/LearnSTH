#bubbleSort 
#冒泡排序
#roseauhan
#21/3/2019
print("冒泡排序/roseauhan/2019:3:21")
a = [1,5,3,2,7,4,86,32]
def bubbleSort(a):
    for i in range(0,len(a)-1):
        for j in range(0,len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
print('a[before]:')

for i in range(len(a)):
    print(str(a[i])+' ',end='')

print('\n\na[after]:')

bubbleSort(a)
for i in range(len(a)):
    print(str(a[i])+' ',end='')



