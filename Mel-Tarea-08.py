from ast import Str
from hashlib import new
from multiprocessing.connection import answer_challenge
from operator import ne
from time import process_time_ns


def alg_div(a: int, d: int):
    if d == 0:
        answer = "Error"
    elif a == 0:
        answer = {
            "quotient": 0,
            "residue": 0
        }
    elif a > 0:
        if d > 0:
            r = remainder(d, a)
            q = int(perfDivision(d, a - r))
        else:
            r = remainder(abs(d), a)
            q = - int(perfDivision(d, a - r))

        answer = {
            "quotient": q,
            "residue": r
        }

    else:
        if d > 0:
            r = negRemainder(d, a)
            r_tempo = remainder(abs(d), abs(a))
            if r != 0:
                q = -(int(perfDivision(d, abs(a + r_tempo))) + 1)
            if r == 0:
                q = -int(perfDivision(d, abs(a + r_tempo)))
        else:
            r = negRemainder(abs(d), a)
            r_tempo = remainder(abs(d), abs(a))
            if r != 0:
                q = int(perfDivision(abs(d), abs(a + r_tempo))) + 1
            if r == 0:
                q = int(perfDivision(abs(d), abs(a + r_tempo)))

        answer = {
            "quotient": q,
            "residue": r
        }


    return answer

def remainder(a, d):

    d_str = str(d)
    
    ceros = True
    cerosCount = 0

    if d != 0:
        while ceros:
            if d_str[-1] == "0":
                cerosCount += 1
                d_str = d_str[:-1]
                if d_str != "":
                    d = int(d_str)
            else:
                ceros = False
                break

    numDigits = len(d_str)

    actualDigit = 1

    flag = True

    while (actualDigit <= numDigits) and flag:
        if int(d_str[0:actualDigit]) >= a:
            flag = False
        else:
            actualDigit += 1

    
    if flag:
        answer = d

    else:
        a_ = a
        count = 0
        
        while int(d_str[0:actualDigit]) >= a_:
            a_ += a
            count += 1

        a_ -= a

        digitDiff = int(d_str[0:actualDigit]) - a_

        if digitDiff == 0:
            if d_str[actualDigit: len(d_str)+1] != "":
                d = int(d_str[actualDigit:len(d_str)+1])
            else:
                d = 0

        else:
            d = d = int(str(int(d_str[0:actualDigit]) - a_) + d_str[actualDigit:len(d_str)+1])

        answer = remainder(a, d)

    return answer

def perfDivision(a, d):
    d_str = str(d)
    
    ceros = True
    cerosCount = 0

    if d != 0:
        while ceros:
            if d_str[-1] == "0":
                cerosCount += 1
                d_str = d_str[:-1]
                if d_str != "":
                    d = int(d_str)
            else:
                ceros = False
                break

    numDigits = len(d_str)
    
    actualDigit = 1

    flag = True

    while (actualDigit <= numDigits) and flag:
        if int(d_str[0:actualDigit]) >= a:
            flag = False
        else:
            actualDigit += 1

    
    if flag:
        answer = ""

    else:
        a_ = a
        count = 0
        
        while int(d_str[0:actualDigit]) >= a_:
            a_ += a
            count += 1

        a_ -= a

        digitDiff = int(d_str[0:actualDigit]) - a_

        if digitDiff == 0:
            if d_str[actualDigit: len(d_str)+1] != "":
                d = int(d_str[actualDigit:len(d_str)+1])
            else:
                d = 0

        else:
            d = d = int(str(int(d_str[0:actualDigit]) - a_) + d_str[actualDigit:len(d_str)+1])

        answer = str(count) + str(perfDivision(a, d))

    return answer + "0"*cerosCount

def negRemainder(a, d):
    d_str = str(d)
    
    ceros = True
    cerosCount = 0

    if d != 0:
        while ceros:
            if d_str[-1] == "0":
                cerosCount += 1
                d_str = d_str[:-1]
                if d_str != "":
                    d = int(d_str)
            else:
                ceros = False
                break
    
    ceros = True
    cerosCount = 0

    if d != 0:
        while ceros:
            if d_str[-1] == "0":
                cerosCount += 1
                d_str = d_str[:-1]
                if d_str != "":
                    d = int(d_str)
            else:
                ceros = False
                break

    numDigits = len(d_str)

    actualDigit = 2

    flag = True

    while (actualDigit <= numDigits) and flag:
        if abs(int(d_str[0:actualDigit])) >= a:
            flag = False
        else:
            actualDigit += 1

    if flag:
        if int(d_str[0:actualDigit]) >= 0:
            answer = int(d_str[0:actualDigit])
        else:
            answer = int(d_str[0:actualDigit]) + a
    
    else:
        a_ = a
        count = 0
        
        while abs(int(d_str[0:actualDigit])) >= a_:
            a_ += a
            count += 1

        a_ -= a

        digitDiff = int(d_str[0:actualDigit]) + a_

        if digitDiff == 0:
            if d_str[actualDigit: len(d_str)+1] != "":
                d = -int(d_str[actualDigit:len(d_str)+1])
            else:
                d = 0
        else:
            d = d = int(str(int(d_str[0:actualDigit]) + a_) + d_str[actualDigit:len(d_str)+1])

        answer = negRemainder(a, d)

    return answer

def shifted_zero(a : int, d : int):
    if d == 0:
        answer = "Error"
    else:
        dicc = alg_div(a, d)

        if dicc["residue"] == 0:
            answer = {
                "l" : dicc["quotient"],
                "s" : 0,
            }
        else:
            s = abs(d) - dicc["residue"]
            newDicc = alg_div(a + s, d)
            answer = {
                "l" : newDicc["quotient"],
                "s" : s,
            }

    return answer