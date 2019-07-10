
list_1 = [1,4,5,21,33,11,55,7,3,6,8,2,6,9]
list_1 = set(list_1)

print(list_1,type(list_1))

list_2 = set([2,4,5,6,11,44,55,66,77,3])

print(list_1,list_2)
"""交集"""
list_too = list_1.intersection(list_2)
print(list_too)
print("------------")
print(list_1 & list_2)
"""并集"""
list_union = list_1.union(list_2)
print(list_union)
print("===========")
print(list_1 | list_2)
#差集
list_diff_1 = list_1.difference(list_2)
list_diff_2 = list_2.difference(list_1)
print(list_diff_1)
print(list_diff_2)
print("+++++++++++++")
print(list_1 - list_2)

"""子集"""
list_3 = set([2,4,5])
print(list_3.issubset(list_1))
print(list_1.issuperset(list_3))
"""对称差集"""

print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2)

