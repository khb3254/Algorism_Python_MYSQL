def solution(s):
    answer = []
    for i in range(len(s)):
        if len(answer) == 0 or answer[-1] != s[i]:
            answer.append(s[i])
        elif answer[-1] == s[i]:
            answer.pop()
            
    if len(answer) >= 1:
        return 0
    else: 
        return 1


   