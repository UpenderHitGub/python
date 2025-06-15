name = "Iphone 16 Pro"

screen_size = 6.0

num_of_speakers = 2

my_phone = [name, screen_size, num_of_speakers]

print(type(my_phone))
print(my_phone)
print("length: " + str(len(my_phone)))
print(my_phone[0])

my_dads_phone = my_phone #shallow copy, any changes to one objects reflects in another
my_dads_phone[0] = "Iphone 16 Pro Max"

print(my_dads_phone)
print(my_phone)

my_phone[0] = name

my_dads_phone = list(my_phone) #deep copy, any changes to one objects does not reflect in another
my_dads_phone = my_phone.copy() #deep copy, any changes to one objects does not reflect in another
my_dads_phone = my_phone[:] #deep copy, any changes to one objects does not reflect in another
my_dads_phone[0] = "Iphone 16 Pro Max"

print(my_dads_phone)
print(my_phone)

for data in my_phone:
    print(data)

iphone_specs = ["single sim", 50000]

my_phone = my_phone + iphone_specs

print(my_phone)

a = list(range(0,5))
print(a)

even_nums = list(filter(lambda x: x % 2 == 0, a))
print(even_nums)

squares = list(map(lambda x: x ** 2, a))
print(squares)