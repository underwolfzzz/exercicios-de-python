min = 10
seg = 59

while seg != 0 and min != -1:
    for seg in range (59, -1, -1):
        print(f'{min}:{seg}')
        if seg == 0:
            min = min - 1
            seg = 59
        