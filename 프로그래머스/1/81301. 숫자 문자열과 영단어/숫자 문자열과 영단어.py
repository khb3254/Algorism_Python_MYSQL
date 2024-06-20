def solution(word):
    dic = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in dic:
        if i in word:
            idx = str(dic.index(i))
            word = word.replace(i, idx)
    answer = int(word)
        
    return answer