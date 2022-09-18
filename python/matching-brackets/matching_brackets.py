def is_paired(input_string):
    bracs = []
    for i in input_string:
        if i in ["(", "{", "["]:
            bracs.append(ord(i))
        elif i in [")", "]", "}"]:
            if len(bracs) == 0:
                return False
            elif bracs[-1] == ord(i) - 1 or bracs[-1] == ord(i) - 2:
                bracs.pop()
            else:
                return False

    if len(bracs) == 0:
        return True
    else:
        return False

