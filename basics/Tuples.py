import time;
my_iphone = ("Iphone 5", 1, 5.0)
for data in my_iphone:
    print(data)

# my_iphone[1] = 2
# Error: 'tuple' object does not support item assignment
# Tuple is immutable

# my_iphone = my_iphone + ("test")
# Error: 'tuple' object does not support item assignment
# Tuple is immutable

tic = time.time()
my_list = list(range(10000000))
my_other_list = list(map(lambda x: x**2, my_list))
toc = time.time()

print("Elapsed Time in Seconds: ", toc - tic)

tic = time.time()
my_tuple = tuple(range(10000000))
my_other_tuple = tuple(map(lambda x: x**2, my_tuple))
toc = time.time()

print("Elapsed Time in Seconds: ", toc - tic)

# In general tuple related operations are faster then list since tuple is immutable


