def openOrSenior(data):
    x = ''
    for person in data:
        if person[0] >= 55 and person[1] > 7:
            x = 'Senior'
        else:
            x = 'Open'
    return x

print(openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]))