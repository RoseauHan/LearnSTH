'''
selectSort
roseauhan
2019 3 21
'''

def selectSort(input_list):
        if len(input_list) == 0:
                return []
        sorted_list = input_list
        length = len(sorted_list)
        for i in range(length):
                min_index = i
                for j in range(i+1,length):
                        if sorted_list[min_index] > sorted_list[j]:
                                min_index = j
                if min_index == i:
                        continue
                sorted_list[i],sorted_list[min_index] = sorted_list[min_index],sorted_list[i]
        return sorted_list

if __name__ == "__main__":
    input_list = [1,3,4,52,5,73,234,627,32,23,12,3]
    print("Before:",input_list)
    sorted_list = selectSort(input_list)
    print("After: ",sorted_list)
