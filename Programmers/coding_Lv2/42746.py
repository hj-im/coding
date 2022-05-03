def solution(numbers):
    numbers = [str(item) for item in numbers]
    numbers.sort(key = lambda x:x*3, reverse=True)
    answer = int(''.join(numbers))
    return str(answer)



