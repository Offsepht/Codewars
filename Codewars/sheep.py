array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, 1,  True ]


def count_sheep(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count
print(count_sheep(array1))