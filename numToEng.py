def deff(number):
    l = {
        3: "hundred",
        4: "thousand"
    }
    return l.get(len(number), 1)

def numIsSingle(number):
    num = int(number)
    if num == 0:
        return "zero"
    elif num == 1:
        return "one"
    elif num == 2:
        return "two"
    elif num == 3:
        return "three"
    elif num == 4:
        return "four"
    elif num == 5:
        return "five"
    elif num == 6:
        return "six"
    elif num == 7:
        return "seven"
    elif num == 8:
        return "eight"
    elif num == 9:
        return "nine"

def tyies(num):
    if len(num) == 2:
        if num[0] == '1':
            l = {0: "ten", 1: "eleven", 2: "twelve", 3: "thirteen", 4: "fourteen", 5: "fifteen",
                 6: "sixteen", 7: "seventeen", 8: "eighteen", 9: "nineteen"}
            return l.get(int(num[1]), -1)

        h = {2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
        if num[1] == '0':
            return h.get(int(num[0]), -1)
        else:
            return h.get(int(num[0]), -1) + ' ' + numIsSingle(num[1])
    
    return -1

def outputFn(num, first):
    if len(num) < 1:
        return
    
    if first is False:
        print("and", end=' ')
    
    while num[0] == '0' and len(num) > 1:
        num = num[1:]

    twies = tyies(num)
    if twies != -1:
        print(twies, end=' ')
        return

    initial = numIsSingle(num[0])
    call = deff(num)
    if call == 1:
        call = ''

    print(str(initial) + ' ' + str(call), end=' ')

    outputFn(num[1:], False)


num = input("enter number: ")
outputFn(num, True)
print()


