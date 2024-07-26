
def bubble_sort(num):
    for i in range(len(num)-1):
        for j in range(len(num)-i-1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
    print(num)


num=[9,7,4,8,3,2,1]
bubble_sort(num)

