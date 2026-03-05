def solution(num_list):
    count_a = 0
    count_b = 0
    answer = []
    for i in num_list:
        if i%2 ==0 :
            count_a += 1
            
        else :
            count_b += 1
    
    answer.append(count_a)
    answer.append(count_b)
            
    return answer