#SelectSort.py
#选择排序
#roseauhan
print('This is a program about selectsort\nWritten by roseauhan in 21/3/2019\nlanguage is python3\n')
a = [2,4,3,1,5,78,34,12,89]

def selectSort(a):
    for i in range(0, len(a)-1):
        mmin = i
        for j in range(i+1, len(a)):
            if a[mmin] > a[j]:
                mmin = j
        a[mmin],a[i] = a[i],a[mmin]

print('a[before]:')
for i in range(len(a)):
    print(str(a[i])+' ', end='')
	#python 2.x, print 不换行
	#>>> print x, 
	#python 3.x print 不换行
	#>>> print(x, end="")
print('\n\n')


print('a[after]:')
selectSort(a)
for i in range(len(a)):
    print(str(a[i])+' ' ,end='')
