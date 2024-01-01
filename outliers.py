# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191]
# data = [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191]
# data = [1094, 1095, 1044, 1053, 1105, 1206, 1307, 1308, 1503, 1604, 1705, 1832, 1853, 1875, 1884, 1912, 3502, 3602]
data = []

# del data[0:2]
# print(data)
#
# del data[14:]
# print(data)

min_val = 100
max_val = 200

# process the low values in the list
stop = 0

for index, value in enumerate(data):
    if value >= min_val:
        stop = index
        break

print(stop)
del data[:stop]
print(data)

# process the high value in the list
start = 0

for index in range(len(data) - 1, - 1, -1):
    if data[index] <= max_val:
        # we have the index of the last item to keep
        # set 'start' to the position of the first
        # item to delete, which is 1 after 'index'
        start = index + 1
        break

print(start)
del data[start:]
print(data)
