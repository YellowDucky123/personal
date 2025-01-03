def deff(number):
    if len(number) == 3:
        return "hundred"
    elif len(number) >= 4 and len(number) <= 6:
        return "thousand"
    elif len(number) >= 7 and len(number) <= 9:
        return "million"
    elif len(number) >= 10 and len(number) <= 12:
        return "billion"
    return 1

def numIsSingle(number):
    num = int(number)
    l = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    return l.get(num)

def tyies(num):
    if len(num) == 2:
        if num[0] == '1':
            l = {0: "ten", 1: "eleven", 2: "twelve", 3: "thirteen", 4: "fourteen", 5: "fifteen",
                 6: "sixteen", 7: "seventeen", 8: "eighteen", 9: "nineteen"}
            return l.get(int(num[1]), -1)

        h = {2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
        start = h.get(int(num[0]), -1)
        if start == -1:
            return -1

        if num[1] == '0':
            return start
        else:
            return start + ' ' + numIsSingle(num[1])
    
    return -1

def outputFn(num, my_list):
    if len(num) < 1:
        return
    
    if len(num) == 1:
        number = numIsSingle(num)
        my_list.append(number)
        return
    
    if int(num) == 0:
        return
    
    while num[0] == '0' and len(num) > 1:
        num = num[1:]
    
    twies = tyies(num)
    if twies != -1:
        my_list.append("and")
        my_list.append(twies)
        return

    flag = 1
    if len(num) == 5 or len(num) == 8 or len(num) == 11:
        string = num[:2]
        initial = tyies(string)
        flag = 2
    elif len(num) == 6 or len(num) == 9 or len(num) == 12:
        initial = outputFn(num[:3], my_list)
        flag = 3
    else:
        initial = numIsSingle(num[0])

    call = deff(num)
    if call == 1:
        call = ''
        my_list.append("and")

    if initial is not None:
        my_list.append(str(initial))
    my_list.append(str(call))

    outputFn(num[flag:], my_list)


num = input("enter number: ")
my_list = []
outputFn(num, my_list)

string = ""
for item in my_list:
    string += item + ' '

print(string)


