def selection_sort(list):
    for i in range(len(list)):
        for a in range(len(list)):
            if list[a]>list[i]:
                list[i],list[a] = list[a],list[i]
    print(list)
selection_sort([8,4,5,2,1,6,3,9,7])
