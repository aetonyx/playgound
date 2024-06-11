#!/usr/bin/python3

def romanizer(numbers):
    resultArray = []
    
    for number in numbers:
        resultArray.append(romanize(number))

    return resultArray


def romanize(num):
    # space = O(1)
    # runtime = O(n) where n is lenght of number -> limited by definition of problem to 4

    returnValue = []
    
    o = 0
    d = 0
    c = 0
    m = 0

    #ones
    o = num % 10
    num = num // 10
    
    #tens
    if num >= 0:
        d = num % 10
        num  = num // 10
    
    #hundreds
    if num >= 0:
        c = num % 10
        num = num // 10
    
    #thousands
    if num >= 0:
        m = num % 10

    #adding numbers in reverse order as I'm adding to back of list

    #add thousands (problem was limited to 1 to 1000)
    if m == 1: returnValue.append('M')

    #adding hundreds
    if c == 1: returnValue.append('C')
    if c == 2: returnValue.append('CC')
    if c == 3: returnValue.append('CCC')
    if c == 4: returnValue.append('CD')
    if c == 5: returnValue.append('D')
    if c == 6: returnValue.append('DC')
    if c == 7: returnValue.append('DCC')
    if c == 8: returnValue.append('DCCC')
    if c == 9: returnValue.append('CM')
    
    #adding tens
    if d == 1: returnValue.append('X')
    if d == 2: returnValue.append('XX')
    if d == 3: returnValue.append('XXX')
    if d == 4: returnValue.append('XL')
    if d == 5: returnValue.append('L')
    if d == 6: returnValue.append('LX')
    if d == 7: returnValue.append('LXX')
    if d == 8: returnValue.append('LXXX')
    if d == 9: returnValue.append('XC')

    #Adding ones
    if o == 1: returnValue.append('I')
    if o == 2: returnValue.append('II')
    if o == 3: returnValue.append('III')
    if o == 4: returnValue.append('IV')
    if o == 5: returnValue.append('V')
    if o == 6: returnValue.append('VI')
    if o == 7: returnValue.append('VII')
    if o == 8: returnValue.append('VIII')
    if o == 9: returnValue.append('IX')

    return ''.join(returnValue)


if __name__ == "__main__":
    
    #running some tests
    assert romanizer([999, 14, 42]) == ['CMXCIX', 'XIV', 'XLII']
    assert romanizer([2]) == ['II']
    assert romanizer([1000, 100, 10, 1]) == ['M', 'C', 'X', 'I']
