#Maximum Ticket Price Problem - Toy Problem
def maxAmount(M, N, seats): 

	q = [] 

	for i in range(M): 
		q.append(seats[i]) 

	ticketSold = 0

	ans = 0

	q.sort(reverse = True) 
	while (ticketSold < N and q[0] > 0): 
		ans = ans + q[0] 
		temp = q[0] 
		q = q[1:] 
		q.append(temp - 1) 
		q.sort(reverse = True) 
		ticketSold += 1

	return ans

if __name__ == '__main__': 

	seats = []

	rows = int(input("Enter number of rows available : ")) 

	for i in range(0, rows):
		empty = int(input())
		seats.append(empty)

	print(seats)
	M = len(seats) 
	N = int(input("Enter the number of People standing in the queue : "))

	print("Maximum Profit generated = ", maxAmount(N, M, seats))
'''Output
Enter number of rows available : 4
2
3
5
4
[2, 3, 5, 4]
Enter the number of People standing in the queue : 4
Maximum Profit generated =  16
'''