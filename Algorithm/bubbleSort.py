'''
bubbleSort 
冒泡排序
roseauhan
21/3/2019
'''
print("BubbleSort/roseauhan/ 3/21/2019\n")
print("modified on 3/25/2019")

def bubbleSort(input_list):
    if len(input_list) == 0:
        return [];
    sorted_list = input_list
    for i in range(len(sorted_list)-1):
        print ("第%d次排序" % (i + 1))
        for j in range(len(sorted_list)-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j],sorted_list[j+1] = sorted_list[j+1],sorted_list[j]
        print ("排序中:" , sorted_list)
    return sorted_list

input_list = [1,4,2,56,23,79,12,345]
print("Before:", input_list)

sorted_list = bubbleSort(input_list)
print("After: ", sorted_list)
