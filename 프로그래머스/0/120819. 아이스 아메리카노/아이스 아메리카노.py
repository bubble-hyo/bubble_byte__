def solution(money):
    answer = []
    coffee = money // 5500
    mon = money % 5500
    answer.append(coffee)
    answer.append(mon)
    return answer