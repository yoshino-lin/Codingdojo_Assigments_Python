def countdown(num):
    countdown_list=[]
    for i in range(num,0,-1):
        countdown_list.append(i)
    return countdown_list

#print(countdown(5))

def print_and_return(list_in):
     print(list_in[0])
     return list_in[1]

#num = print_and_return([1,2])
#print(num)

def first_plus_length(list_in):
    return list_in[0]+len(list_in)

#print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(list_in):
    new_list=[]
    if len(list_in)>1:
        for i in range(len(list_in)):
            if list_in[i]>list_in[1]:
                new_list.append(list_in[i])
        return new_list
    else:
        return False

#print(values_greater_than_second([5,2,3,2,1,4]))
#print(values_greater_than_second([3]))
#print(values_greater_than_second([5,2]))

def length_and_value(length,value):
    list_out=[]
    for i in range(length):
        list_out.append(value)
    return list_out
#print(length_and_value(4,7))
#print(length_and_value(6,2))
