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

