name = "Iphone 16 Pro"
print(type(name))

screen_size = 6.0
print(type(screen_size))

num_of_speakers = 2
print(type(num_of_speakers))

print("I just bought an " + name + " with a screen size of " + str(screen_size) + "\nand " + str(num_of_speakers) + " speakers.\n")

a = 3
b = 2
print("a : " + str(a), ", b : "+ str(b) + "\na + b : " + str(a + b),"\na - b : " + str(a - b),"\na * b : " + str(a * b),"\na / b : " + str(a / b),"\nb / a : " + str(b / a),"\na ** b : " + str(a ** b),"\na % b : " + str(a % b),"\na // b : " + str(a // b),"\nb // a : " + str(b // a))



is_android = False

print(type(is_android))

if is_android:
    print("I am an android phone")
else:
    print("I am not an android phone")

print(is_android == False and num_of_speakers > 1)

# help(range)
print("executing 'for' loop")
for i in range(5):
    print(i, i ** 2)

i = 0
print("executing 'while' loop")
while i < 5:
    print(i , i ** 2)
    i += 1

def print_squares(stop_val):
    for i in range(stop_val):
        print(i, i ** 2)
        i += 1

def sum_of_range(stop_val):
    sum_ = 0
    for i in range(stop_val):
        sum_ += i
    return sum_

def print_squares_with_start_val(stop_val, start_val = 0):
    """ This function prints sqaures of numbers starting with "start_val" and ending (exclusively) with stop_val"""
    for i in range(start_val, stop_val):
        print(i, i ** 2)
        i += 1

print_squares(5)

print_squares_with_start_val(5, 2)

print(sum_of_range(5))


help(print_squares_with_start_val)

