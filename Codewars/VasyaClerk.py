def tickets(people):
    cashier = {100:0,50:0,25:0}
    for pay in people:
        if pay == 25:
            cashier[25] += 1
        elif pay == 50:
            if cashier[25] == 0:
                return 'NO'
            cashier[50] += 1
            cashier[25] -= 1
        else:
            cashier[100] += 1
            if cashier[50] >= 1 and cashier[25] >= 1:
                cashier[50] -= 1
                cashier[25] -= 1
            elif cashier[25] >= 3:
                cashier[25] -= 3
            else:
                return 'NO'
    return 'YES'

def tickets(people):
    cash = 0
    yes = True
    for i in people:
            if i == 25:
                cash += 25
            elif i == 50:
                cash -= 25
                if cash < 0:
                    yes = False
                    break
            elif i == 100:
                cash -= 75
                if cash < 0:
                    yes = False
                    break
            else:
                break
    if yes == True:
        return 'YES'
    else:
        return 'NO'
                
 

print(tickets([25,25,50]))
print(tickets([25, 100]))
print(tickets([25, 25, 50, 50, 100]))
print(tickets([25,50,25,100,25,25,50,100,25,50,25,100,25,25,25,100]))