import time

my_iphone = ["5g", 4.3, "single_sim", 2]
my_iphone.append(4.3)
my_set = set(my_iphone)

print(my_iphone)
print(my_set) #Set does not allow duplicates

tic = time.time()
my_num_list = list(range(10000000))
print(123 in my_num_list)
print(11123 in my_num_list)
print(11111111 in my_num_list)
toc = time.time()
print("Elapsed Time in Seconds: ", toc - tic)

tic = time.time()
my_num_set = set(range(10000000))
print(123 in my_num_set)
print(11123 in my_num_set)
print(11111111 in my_num_set)
toc = time.time()
print("Elapsed Time in Seconds: ", toc - tic)

# In general set related operations takes less time