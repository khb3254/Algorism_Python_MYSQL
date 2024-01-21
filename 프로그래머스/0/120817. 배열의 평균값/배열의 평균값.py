def solution(numbers):
    anwer = 0
    for number in numbers:
        anwer += number
    return anwer / len(numbers)