def calc1():
    s=10
    t=1
    while s<=20:
        s+=s//10
        t+=1
    return t
def calc2():
    s=10
    S=0
    t=1
    while S<=100:
        S+=s
        s+=s//10
        t+=1
    return t
def output(t1,t2):
    print(t1,t2)
    
if __name__ == '__main__':
    t1=calc1()
    t2=calc2()
    output(t1,t2)
    
    