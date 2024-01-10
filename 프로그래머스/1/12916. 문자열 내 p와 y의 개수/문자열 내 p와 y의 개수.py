def solution(s):
    # 소문자로 수정
    s = s.lower()
    return True if s.count("p") == s.count("y") else False