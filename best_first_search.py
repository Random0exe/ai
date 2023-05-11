import collections

def bfs(forest, sr, sc, tr, tc):
    R, C = len(forest), len(forest[0])
    queue = collections.deque([(sr, sc, 0)])
    seen = {(sr, sc)}
    
    while queue:
        r, c, d = queue.popleft()
        
        if r == tr and c == tc:
            return d
        
        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if (0 <= nr < R and 0 <= nc < C and
                    (nr, nc) not in seen and forest[nr][nc]):
                seen.add((nr, nc))
                queue.append((nr, nc, d+1))
    
    return -1

if __name__ == '__main__':
    # Example usage
    forest = [[1, 1, 0, 0],
              [1, 1, 1, 1],
              [0, 0, 1, 0],
              [0, 1, 1, 1]]
    
    sr, sc = 0, 0
    tr, tc = 3, 3
    
    distance = bfs(forest, sr, sc, tr, tc)
    print("Shortest distance:", distance)
