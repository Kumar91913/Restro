"""previous_num = 0

for i in range(1,11):
    x_sum = previous_num + 1
    print("currentnum", i, "PreviuosNum ", previous_num, " Sum: ", x_sum)
    previous_num = i"""


previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i

    
