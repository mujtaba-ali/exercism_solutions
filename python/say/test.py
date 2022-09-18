import subprocess
import sys

#if len(sys.argv) != 2:
#    print("[usage] python3 test.py number")
#    sys.exit(1)

#n = sys.argv[1]

inner = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 
        7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 
        13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 
        17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 
        30: "thirty", 40: "fourty", 50: "fifty", 60: "sixty", 70: "seventy", 
        80: "eighty", 90: "ninety"}
outer = ["trillion", "billion", "million", "thousand"]

def words(number):
    number_s = str(number)
    number_split = []
    initial = ""

    while len(number_s) % 3 != 0:
        initial += number_s[0]
        number_s = number_s[1:]
    if initial != "":
        number_split.append(three_digits(initial))    

    while len(number_s) > 0:
        number_split.append(three_digits(number_s[:3]))
        number_s = number_s[3:]
                
    i = len(number_split) - 1
    while i > 0:
        number_split.insert(i, f" {outer[-1]} ")
        del outer[-1]
        i -= 1
    return "".join(number_split)
    

def three_digits(n_string):
    lst = []
    lst2 = []
    f = ""

    if len(n_string) > 2:
        lst2.append(n_string[0])
        lst2.append(n_string[1:3])

    else:
        lst2.append(0)
        lst2.append(n_string[:])

    if int(lst2[1]) in range(11, 20):
        lst.append(inner[int(lst2[1])])
    else:
        for i,j in enumerate(lst2[1][::-1]):
            lst.append(inner[int(j)*(10**i)])
        
    if lst2[0] != 0:
        f += inner[int(lst2[0])]+" hundred "

#    if sum([int(i) for i in lst2[1]]) > 0:
    if "0" not in lst2[1]:
        f += ("-".join(lst[::-1]))
    else:
        f += "".join(lst[::-1])
    
    return f

#subprocess.call(["say", words(int(n))])
print(words(1002345))
