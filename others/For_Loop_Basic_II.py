def biggie_size(list_in):
    for i in range(len(list_in)):
        if list_in[i]>0:
            list_in[i]="big"
    return list_in
#print(biggie_size([-1, 3, 5, -5]))

def count_positives(list_in):
    num_of_positives = 0
    for i in range(len(list_in)):
        if list_in[i]>0:
            num_of_positives+=1
    list_in[len(list_in)-1] = num_of_positives
    return list_in
#print(count_positives([-1,1,1,1]))
#print(count_positives([1,6,-4,-2,-7,-2]))

def sum_total(list_in):
    sum = 0
    for i in range(len(list_in)):
        sum+=list_in[i]
    return sum
#print(sum_total([1,2,3,4]))
#print(sum_total([6,3,-2]))

def average(list_in):
    return sum_total(list_in)/len(list_in)
#print(average([1,2,3,4]))

def length(list_in):
    return(len(list_in))
#print(length([37,2,1,-9]))
#print(length([]))

def minimum(list_in):
    if len(list_in)>0:
        min = list_in[0]
        for i in range(1,len(list_in)):
            if list_in[i]<min:
                min = list_in[i]
        return min
    elif len(list_in)==0:
        return False
    else:
        print("Erro!")
#print(minimum([37,2,1,-9]))
#print(minimum([]))

def maximum(list_in):
    if len(list_in)>0:
        max = list_in[0]
        for i in range(1,len(list_in)):
            if list_in[i]>max:
                max = list_in[i]
        return max
    elif len(list_in)==0:
        return False
    else:
        print("Erro!")
#print(maximum([37,2,1,-9]))
#print(maximum([]))

def ultimate_analysis(list_in):
    return {'sumTotal': sum_total(list_in), 'average': average(list_in), 'minimum': minimum(list_in), 'maximum': maximum(list_in), 'length': length(list_in)}
#print(ultimate_analysis([37,2,1,-9]))

def reverse_list(list_in):
    for i in range(len(list_in)-1,-1,-1):
        list_in.append(list_in[i])
        del list_in[i]
    return list_in
#print(reverse_list([37,2,1,-9]))
#this is the best way to slove this question
