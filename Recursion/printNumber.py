def numberPrint(Num):
    if Num>0:
        numberPrint(Num-1)
    print(Num)
numberPrint(5)