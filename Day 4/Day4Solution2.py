import string


with open("Day 4/Assignments.txt", 'r') as assignments:
    finalScore = 0
    for line in assignments:
        line = line.replace('-', ' ')
        line = line.replace(',', ' ')
        nums = [eval(i) for i in line.split()]
        
        if (nums[0] <= nums[2] and nums[0] >= nums[3]) or (nums[1] >= nums[2] and nums[1] <= nums[3]) or (nums[2] >= nums[0] and nums[2] <= nums[1]) or (nums[3] >= nums[0] and nums[3] <= nums[1]):
            finalScore +=1
        # if (nums[0] <= nums[2] and nums[1] >= nums[3]) or (nums[0] >= nums[2] and nums[1] <= nums[3]):
        #     finalScore += 1

    print(finalScore)
