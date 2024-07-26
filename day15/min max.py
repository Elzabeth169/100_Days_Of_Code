
def min_max(a):
    min= float('inf')
    max= float('-inf')
    for i in a:
        if i<min:
            min=i
        if i>max:
            max=i
    # values = min,max
    return (min,max)

arr=[8,7,6,9,3]
v= min_max(arr)
min , max = v
print("minimum value:" + str(min))
print("maximum value:" + str(max))
