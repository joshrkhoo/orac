# first line of inputs is 2 integers separated by a space
# followed by r rows and c columns of each character is a string
r = 0
c = 0
input_chars = []

inputFile = open("landin.txt", "r")

r, c = map(int, inputFile.readline().split())

for i in range(r):
    input_chars.append(inputFile.readline().strip())

# print(input_chars)

# find the largest row of residential blocks (dots .)
    # each row need to count the number of residential blocks
        # if the next row is larger then update the count
    # need to get the row and column index of the starting block and ending block
# find the largest column of residential blocks

# when u get a dot, get the row and column index

# print(len(input_chars[0]))

def get_largest_row(input_chars):
    count = 0
    row = ''

    col_start = ''
    col_end = ''
    for r in range(len(input_chars)):
        current_count = 0

        for c in range(len(input_chars[0])):
            if input_chars[r][c] == '.':
                current_count += 1

                if c == len(input_chars[0])-1:
                    if current_count > count:
                        count = current_count

                        # col
                        col_start = str(c+2-count)
                        col_end = str(c+1)
                        row = str(r+1)
                    current_count = 0
                    

            
            if current_count == len(input_chars[0]):
                count = current_count
                print(r, c)

                col_start = str(c+1-count)
                col_end = str(c)
                row = str(r+1)

                break


            if input_chars[r][c] == '#':
                # print(current_count)
                if current_count > count:
                    count = current_count

                    # col
                    col_start = str(c+1-count)
                    col_end = str(c)
                    row = str(r+1)
                current_count = 0
                



    # print(count)
    return (f'{row} {col_start} {row} {col_end}', count)

    

def get_largest_column(input_chars):
    count = 0
    col = ''

    row_start = ''
    row_end = ''
    for c in range(len(input_chars[0])):
        current_count = 0
            # print(count)
        for r in range(len(input_chars)):
            if input_chars[r][c] == '.':
                current_count += 1

                if r == len(input_chars)-1:
                    if current_count > count:
                        count = current_count

                        # col
                        row_start = str(r+2-count)
                        row_end = str(r+1)
                        col = str(c+1)
                    current_count = 0
            
            if current_count == len(input_chars):
                count = current_count

                current_row_start = str(r+1-count)
                current_row_end = str(r)
                row_end = current_row_end
                row_start = current_row_start 
                col = str(c+1)
                break
            

            if input_chars[r][c] == '#':

                # print(current_count)
                if current_count > count:
                    count = current_count
                    row_start = str(r+1-count)
                    row_end = str(r)

                    col = str(c+1)
                current_count = 0

    # print(count)
    return (f'{row_start} {col} {row_end} {col}', count)



# print(get_largest_row(input_chars))
# print(get_largest_column(input_chars))
    

output_col, count_col = get_largest_column(input_chars)
output_row, count_row = get_largest_row(input_chars)

if count_col > count_row:
    answer = output_col
else: 
    answer = output_row

# print(answer)





outputFile = open("landout.txt", "w")
outputFile.write(str(answer) + "\n")
 
# Clean up!
inputFile.close()
