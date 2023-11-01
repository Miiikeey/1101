f = open("one_hundred.txt")

master_list = []
for line in f:
    if len(line) >1:
        list_nums = line.split()
        list_nums = [int(i) for i in list_nums]
        master_list.extend(list_nums)

f.close()
for r in range(100):
    if r not in master_list:
        print(f"{r} is not present")