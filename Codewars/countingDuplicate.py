def duplicate_count(text):
    text1 = list(text)
    dup = set(text)
    
    if len(dup) == len(text1):
        return 0
    else:
        return len(text) - len(dup)
    



print(duplicate_count("abcde"))
print(duplicate_count("abcdea"))