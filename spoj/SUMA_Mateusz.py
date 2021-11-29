sum = 0

while True:
    try:
        wej = int(input())
        sum += wej
        print(sum)
    except EOFError:
        break
    