l1 = [1,2,3,4]
l2 = [2,4,6,8]
l3 = [3,6,9,12]
l4 = [4,8,12,16]
le = [l2,l3,l4]
for una_lista in le:
    print(dict(zip(l1,una_lista)))
