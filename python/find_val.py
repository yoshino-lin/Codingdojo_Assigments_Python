arr = [1,3,4,5,6,8,9,11,12,18,20,25]
val = 11
def fine_it(arr,val):
    while True:
        middle_pint = int(len(arr)/2)
        if len(arr) > 3:
            if arr[middle_pint] > val:
                del arr[middle_pint-1 : len(arr)]
            elif arr[middle_pint] < val:
                del arr[0 : middle_pint]
            else:
                return True
            print(arr)
        else:
            for i in arr:
                if i == val:
                    return True
            return False

print(fine_it(arr,val))
