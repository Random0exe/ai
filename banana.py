#(Toy Problem) Camel and banana problem

total=int(input('Enter no. of bananas at starting '))
distance=int(input('Enter distance you want to cover '))
load_capacity=int(input('Enter max load capacity of your camel '))
lose=0
start=total
for i in range(distance):
    while start>0:
        start=start-load_capacity

        if start==1:
            lose=lose-1

        lose=lose+2
#Here lose is decreased as in last trip camel will not go back.
    lose=lose-1
    start=total-lose
    if start==0:#Condition to check whether it is possible to take a single banana or not.
        break
print(start)

'''Output
Enter no. of bananas at starting 3000
Enter distance you want to cover 1000
Enter max load capacity of your camel 1000
533
'''