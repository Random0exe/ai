import heapq

def astar(forest, sr, sc, tr, tc):
    R, C = len(forest), len(forest[0])
    heap = [(0, 0, sr, sc)]
    cost = {(sr, sc): 0}
    while heap:
        f, g, r, c = heapq.heappop(heap)
        if r == tr and c == tc: return g
        for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
            if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                ncost = g + 1 + abs(nr - tr) + abs(nc - tc)
                if ncost < cost.get((nr, nc), 9999):
                    cost[nr, nc] = ncost
                    heapq.heappush(heap, (ncost, g+1, nr, nc))
    return -1

if __name__ == '__main__':
    # Example usage
    forest = [[1, 1, 0, 0],
              [1, 1, 1, 1],
              [0, 0, 1, 0],
              [0, 1, 1, 1]]
    
    sr, sc = 0, 0
    tr, tc = 3, 3
    
    distance = astar(forest, sr, sc, tr, tc)
    print("Shortest distance:", distance)