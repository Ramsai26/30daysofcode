if __name__ == '__main__':
    n = int(input())
    PB={}
    for _ in range(0,n):
        name,contact = input().split()
        PB[name]=contact
    try:
        while(True):
            Dail=str(input())
            if Dail in PB:
                print(Dail+"="+PB[Dail])
            else:
                print('Not found')

    except(EOFError):
        pass
