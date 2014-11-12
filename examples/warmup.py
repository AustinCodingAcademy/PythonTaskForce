file = open('orders.txt', 'r')

lines = file.read()

my_list = lines.split("\n")

print my_list[::3]

print my_list[1::3]

print my_list[2::3]


