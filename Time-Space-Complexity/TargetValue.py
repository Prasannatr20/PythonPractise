num = [12, 7, 25, 9, 14]
length= len(num)
target = 25
def search_target(nums, tar):
    count = 0
    for i in nums:
        if i==tar:
            return count
        count+=1
    return -1

print(search_target(num, target))