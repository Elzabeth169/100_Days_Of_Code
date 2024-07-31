class Solution:
    def containsDuplicate(self, num):
        n={}
        flag=0
        for i in range(len(num)):
            if num[i] in n:
                n[num[i]]+=1
                flag=1
                break
            else:
                n[num[i]]=1
        if flag==1:
            return "There are duplicates"
        else:
            return "no duplicates"

num=[9,5,4,3,6,7,5,2]
obj=Solution()
s=obj.containsDuplicate(num)
print(s)