list1 = [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4]

freq = {}

for num in list1:
    freq[num] = freq.get(num, 0) + 1

print(freq)