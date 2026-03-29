def containsDuplicate(nums):
    ori=nums
    num1=set(nums)
    if len(ori)!=len(num1):
        return True
    else:
        return False
    

print(containsDuplicate([12,3,12,32,53,3]))

