# a, b = map(int, input().split())
a = int(input())

input_nums = []
for i in range(a):
    input_nums.append(int(input()))

print(a, input_nums)

# Traverse the input numbers in reverse order 
# starting from the last input
    # if not 0 
        # not a cute numbers so output should be 0
    # if 0 
        # increment count
        # go to i-1th index and check if it is a 0 
    #print count


count = 0
for i in range(len(input_nums)-1, -1, -1):
    if input_nums[i] != 0:
        break
    count +=1 

print(count)