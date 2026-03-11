mylist = ['41', 'DROND', 'BVSs', '13', 'ZARA']

for item in mylist:
    if item.isdigit():
        print(item * 3)
    else:
        print(item + "#")