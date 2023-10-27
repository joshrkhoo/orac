
inputFile = open("wetin.txt", "r")
a = None
input_nums = []
for i, line in enumerate(inputFile.readlines()):
    input_nums.append(int(line.strip()))
 


# print(input_nums)

"""
8 months 
take 10 from each month
add next month
repeat
print remaining megalitres of water after all 8 months

so if its 12 10
12 - 10 = 2
2 + 10 = 12
12 - 10 = 2
answer = 2
"""

released = 10
current_amount = 0


for i in range(len(input_nums)):
    current_amount += input_nums[i]
    if current_amount < released:
        current_amount = 0
    else:
        current_amount -= released

# print(current_amount)    

# Write the output
outputFile = open("wetout.txt", "w")
outputFile.write(str(current_amount) + "\n")
 
# Clean up!
inputFile.close()