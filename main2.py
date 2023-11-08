
#open file with f
f = open("one_hundred.txt")

#split up the lines to have just numbers
master_list = []
for line in f:
    if len(line) >1:
        list_nums = line.split()
        list_nums = [int(i) for i in list_nums]
        master_list.extend(list_nums)
f.close()

#find missing numbers in the list
missing_numbers = []
for r in range(1,101):
    if r not in master_list:
        missing_numbers.append(r)

#sort out the lists and print
missing_numbers.sort()
master_list.sort()

#create a variable to print it onto a different txt fike
output_missing = print(f"The missing numbers: {missing_numbers}")
output_master = print(f"The numbers we had: {master_list}")

#open the separate file and write in it
output = open("one_hundred_sorted.txt", "w")
output.writelines(str(output_missing))
output.writelines(str(output_master))
output.close()

#reading the file
with open("one_hundred_sorted.txt", "r") as read:
    print(read.read())

