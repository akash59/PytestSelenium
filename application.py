import random

devices = ['switch', 'tv', 'switch', 'tv', 'switch', 'tv', 'switch', 'tv', 'switch', 'tv', 'switch', 'tv']


def name_devices(device_list):
    unique_devices = []
    device_dict = {}
    for device in device_list:
        if device not in device_dict:
            device_dict[device] = 1
            unique_devices.append(device)
        else:
            updated_name = device + str(device_dict[device])
            unique_devices.append(updated_name)
            device_dict[device] = device_dict[device] + 1
    return unique_devices


result = name_devices(devices)
print(result)


def fill_list(my_list, list_length, low, high):
    for i in range(0, list_length):
        my_list.append(random.randint(low, high))
    print(my_list)


fill_list([], 5, 0, 10)
print(random.__name__)


def gen():
    L = []
    for i in range(1000000):
        L.append(i * i)
    return L


def gen_new():
    for i in range(10):
        yield i * i


values = gen_new()
x = [x for x in values]
print(x)


def count_words(my_str):
    words = my_str.split(" ")
    for word in words:
        if word == "Geeks":
            yield word


count = 0
ss = "Geeks for Geeks is an awesome website. I love Geeks for Geeks"
result = count_words(ss)
for i in result:
    count += 1
print(count)


# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function 
                    passed as an argument.""")
    print(greeting)


greet(shout)
greet(whisper)

