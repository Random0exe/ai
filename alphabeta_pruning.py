MAX, MIN = 1000, -1000 
def minimax(depth, nodeIndex, maximizingPlayer, 
			values, alpha, beta): 

	if depth == 3: 
		return values[nodeIndex] 

	if maximizingPlayer: 
	
		best = MIN

		for i in range(0, 2): 
			
			val = minimax(depth + 1, nodeIndex * 2 + i, 
						False, values, alpha, beta) 
			best = max(best, val) 
			alpha = max(alpha, best) 

			if beta <= alpha: 
				break
		
		return best 
	
	else: 
		best = MAX
		for i in range(0, 2): 
		
			val = minimax(depth + 1, nodeIndex * 2 + i, 
							True, values, alpha, beta) 
			best = min(best, val) 
			beta = min(beta, best) 
			if beta <= alpha: 
				break
		
		return best 
	
if __name__ == "__main__": 

    values = []
    for i in range(0, 8):

        x = int(input(f"Enter Value {i}  : "))
        values.append(x)

    print ("The optimal value is :", minimax(0, 0, True, values, MIN, MAX)) 

    '''Output:
    Enter Value 0  : 3
    Enter Value 1  : 5
    Enter Value 2  : 6
    Enter Value 3  : 9
    Enter Value 4  : 1
    Enter Value 5  : 2
    Enter Value 6  : 0
    Enter Value 7  : -1
    The optimal value is : 5'''