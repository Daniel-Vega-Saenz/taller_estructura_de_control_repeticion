from winreg import REG_NO_LAZY_FLUSH


c=0
for i in range(6,70,5):
    c=c+1
    if(c==13):
        break
    print(i)
    