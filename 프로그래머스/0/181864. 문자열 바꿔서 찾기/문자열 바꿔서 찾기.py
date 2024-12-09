def solution(myString, pat):
    my = ""
    for i in myString:
        if i == "A":
            my += "B"
        else:
            my += "A"
    if pat in my:
        return 1
    else:   
        return 0