
list1 = [7,5,4,1,9, 0, 3, -2, 21, -6, 13]
sorted_list = sorted(list1)
print(list1)
print(sorted_list)
print(list1 == sorted_list)

def bubblesort(list):
    for i in range (len(list)-1):
        for i in range (len(list)-1):
                        
            first = list[i]
            second = list[i+1]
                
        
            if (first>second):
                swap = first
                list[i] = second
                list[i+1] = swap
            
    return list
        
print(bubblesort(list1))

