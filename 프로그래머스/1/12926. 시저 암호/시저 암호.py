def solution(s, n):
    # 대문자 65-90, 소문자 97-122
    # A = 65, Z = 90, z = 122, 공백 = 32
    s = list(s)
    
    for i in range(len(s)):
        # 대문자일때
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        # 소문자일때
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
    return "".join(s)
            
    