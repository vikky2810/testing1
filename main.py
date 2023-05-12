def diamond(n):
    str = ''
    if n % 2 == 0 or n < 0:
        return None
    else:
        for i in range(1,n):
            for j in range(0 , i +1 ,2):
                str += "*"
            print("\n")
        return str

print(diamond(3))