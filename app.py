import pandas as pd


data1 = pd.read_csv('list1.csv').values
data2 = pd.read_csv('list2.csv').values

list1 = []
list2 = []
# result = [x for x in data ]
for a in data1:
    for x in a:
        # print (x)
        list1.append(x)


for a in data2:
    for x in a:
        # print (x)
        list2.append(x)

# print(list1)
# print(list2)

result = [x for x in list1 if x not in list2]

print(result)
