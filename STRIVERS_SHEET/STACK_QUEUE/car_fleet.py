def pairing_fleet(target,position,speed):
    n=len(position)
    for i in range(n):
        for j in range(0,n-i-1):
            if position[j]>=position[j+1]:
                position[j],position[j+1]=position[j+1],position[j]
                speed[j],speed[j+1]=speed[j+1],speed[j]
    position=position[::-1]
    speed=speed[::-1]
    print(position)
    print(speed)
    arrival_time=[0]*n
    for i in range(n):
        arrival_time[i]=(target-position[i])/speed[i]
    print(arrival_time)
    stack=[]
    for i in range(n):
        if len(stack)==0:
            stack.append(arrival_time[i])
        elif arrival_time[i]>stack[-1]:
            stack.append(arrival_time[i])
    print(len(stack))
    return
if __name__=="__main__":
    target=int(input("enter target"))
    position=list(map(int,input().split(" ")))
    speed=list(map(int,input().split(" ")))
    pairing_fleet(target,position,speed)