def dirReduc(arr):
    direction = [arr]
    opposite = {
        'north' : 'south',
        'south' : 'north',
        'east' : 'west',
        'west' : 'east'
    }
    for i in  arr[1::]:
        if arr[i].lower() == opposite(arr[i - 1]):
            direction.remove(arr[i])

    return direction


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))
