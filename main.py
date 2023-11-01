
max_value = ''
min_value = '9999'
#open the txt file
f = open('one_hundred.txt')
for line in f:
        if len(line) > 1:
            list_nums = line.split()
            for num in list_nums:
                if num<min_value:
                    min_value = num
                if num>max_value:
                    max_value = num
                    

f = open('one_hundred.txt')
for line in f:
    if len(line) > 1:
        list_nums = line.split()
        for num in list_nums:
            for r in range(int(min_value), int(max_value)):
                if r != num:
                    print(f'{r} is not present')


print(f"{min_value}, {max_value}")


