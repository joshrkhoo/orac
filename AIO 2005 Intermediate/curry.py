c = 0
r = 0
v = 0

inputFile = open("curryin.txt", "r")

c, r, v = map(int, inputFile.readline().split())

#x: the number of mouthfuls containing a scoop of rice with a scoop of vegetables
#y: the number of mouthfuls containing a scoop of curry with a scoop of vegetables
#z: the number of mouthfuls containing a scoop of curry with a scoop of rice


# repeat the following 
# Out of curry, rice and vegetables
    # take a mouthful containing a scoop of the second largest and largest amount given 
        # get largest by using max()
        # get second largest by 
    # increment whatever combination that is
    # if the second largest amount is 2 different items 
        # take a random one 

foodmap = {
    (1, 2): 0,
    (2, 1): 0,
    (0, 1): 2,
    (1, 0): 2,
    (0, 2): 1,
    (2, 0): 1
}
answer = [0, 0, 0]
# i, j = 0, 1
# answer[foodmap[(i, j)]] += 1

items = []
items.append(c)
items.append(r)
items.append(v)

def get_largest(lis):
    largest = 0
    l_index = 0
    for i, num in enumerate(lis):
        if num > largest:
            l_index = i
            largest = num
    return l_index

def get_sec_largest(lis, largest_index):
    sec_largest = 0
    sec_l_index = 0
    for i, num in enumerate(lis):
        if i == largest_index:
            continue
        if num > sec_largest:
            sec_l_index = i
            sec_largest = num
    return sec_l_index
    
def get_zeros(lis):
    count = 0
    for item in lis:
        if item == 0:
            count +=1
    return count


while get_zeros(items) < 2:
    largest_index = get_largest(items)
    sec_largest_index = get_sec_largest(items, largest_index)
    items[largest_index] -=1
    items[sec_largest_index] -=1
    
    answer[foodmap[(largest_index, sec_largest_index)]] += 1

outputFile = open("curryout.txt", "w")
outputFile.write(' '.join(map(str,answer)))
 
# Clean up!
inputFile.close()
outputFile.close()




# r_v = 0 
# c_v = 0 
# c_r = 0
