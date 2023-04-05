
if __name__ == '__main__':
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    commands = [4,-1,4,-2,4]
    #commands = [4, -1, 3]
    #commands = [6,-1,-1,6]

    obstacles = {(2,4)}

    maxdist = 0
    pos = 1
    x = y = 0

    for unit in commands:
        if unit == -2:        # direction to left
            pos = (pos - 1) % 4
        elif unit == -1:      # direction to right
            pos = (pos + 1) % 4
        else:
            for i in range(unit):
                curposx = x + direction[pos][0]
                curposy = y + direction[pos][1]
                if (curposx,curposy) not in obstacles:   # if position after movement not an obstacle
                    x = x + direction[pos][0]
                    y = y + direction[pos][1]
                    maxdist = max(maxdist, x*x + y*y)     # max of current to previous distances

    print('The furthest point the robot ever gets from origin is - ',maxdist)





