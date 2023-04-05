import sys
from collections import deque
import copy


def isSafe(field, visited, x, y):     # to check if it is safe to go to (x, y)(i.e plain land)
    return field[x][y] == 0 and not visited[x][y]


def isValid(x, y, M, N):       # Check if (x, y) coordinates is inside grid
    return M > x >= 0 and N > y >= 0



def BFS(grid):   # BFS to rescue human starting from source cell

    # M × N grid
    (M, N) = (len(grid), len(grid[0]))


    # four possible movements from a cell
    r = [-1, 0, 0, 1]
    c = [0, -1, 1, 0]


    time = 0      # variable for waiting time
    found = 0     # variable to determine if able to reach destination anytime
    for iteration in range(M + N):
            mat = copy.deepcopy(grid)      #check if cell is plain land,mark it as visited and enqueue
            visited = [[False for x in range(N)] for y in range(M)]
            q = deque()
            for n in range(M):
                if mat[n][0] == 0:
                    q.append((n, 0, 0))
                    visited[n][0] = True

            for cnt in range(iteration):  # robot waiting while flood cell spreads to all adjacent cells
                for p in range(M):
                    for s in range(N):
                        for t in range(len(r)):
                            if mat[p][s] == 1 and isValid(p + r[t], s + c[t], M, N) \
                                and mat[p + r[t]][s + c[t]] == 0:
                                mat[p + r[t]][s + c[t]] = sys.maxsize

                for a in range(M):
                    for b in range(N):
                        if mat[a][b] == sys.maxsize:
                            mat[a][b] = 1

# after waiting - robot begins movement, flood continues to adjacent cells
            while q:                 # loop till queue empty
                for p in range(M):
                    for s in range(N):
                        for t in range(len(r)):
                            if mat[p][s] == 1 and isValid(p + r[t], s + c[t], M, N) \
                                    and mat[p + r[t]][s + c[t]] == 0:
                                mat[p + r[t]][s + c[t]] = sys.maxsize
                for a in range(M):
                    for b in range(N):
                        if mat[a][b] == sys.maxsize:
                            mat[a][b] = 1

                (i, j, dist) = q.popleft()    # distance to destination

                # if the destination is reached, return time waited
                if (i == M - 1 and j == N - 1):
                    found = 1
                    time = iteration + 1

                  # all four possible movements from current cell, mark as visited and enqueue
                for k in range(len(r)):
                    if (isValid(i + r[k], j + c[k], M, N) and
                            isSafe(mat, visited, i + r[k], j + c[k])):
                        visited[i + r[k]][j + c[k]] = True
                        q.append((i + r[k], j + c[k], dist + 1))

    if found == 0: # if robot never reaches destination
        time = -1
    return time

if __name__ == '__main__':
                                    # test cases
    arr1 = [[0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 1, 0],
            [0, 2, 0, 0, 1, 2, 0],
            [0, 0, 2, 2, 2, 0, 2],
            [0, 0, 0, 0, 0, 0, 0]]

    """
    arr2 =  [[0,0,0,0],
             [0,1,2,0],
             [0,2,0,0]]

    arr3 = [[0,0,0],
            [2,2,0],
            [1,2,0]]
    """

    (M, N) = (len(arr1), len(arr1[0]))  # dimensions of grid
    shortesttime = BFS(arr1)
    print("Input array is ",arr1)
    print("\nOutput:\n")

    if (M > 100 or N > 100):
        print("Grid size greater than acceptable limits")
    else:
        if shortesttime == -1:
            print(shortesttime,"- Impossible for robot to safely rescue the human")

        elif shortesttime == M+N:   # the max dist/time for robot to reach destination is always < M+N
            shortesttime = 1000000000
            print(shortesttime,"- Robot can always safely rescue the human anytime")

        else:
            print(shortesttime,"- Maximum time robot can stay in its initial position while safely rescuing the human")
