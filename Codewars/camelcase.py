import re
def solution(s):
    return " ".join([i for i in re.split("([A-Z][^A-Z]*)", s) if i])
    



print(solution("helloWorld"))
print(solution("breakCamelCase"))
