import numpy as np
import sys, json
from timeit import default_timer as time
# because it won't just print()  to console like that
def sho(x):
    print(x, file=sys.stderr)

def find(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find(key, d):
                    yield result
# Resized when data loaded. also, everyone with their own copy? Is it even persistent?
# These are grid size not like board.
food_sdr = np.zeros((1,1))
prey_sdr = np.zeros((1,1))
wall_sdr = np.zeros((1,1)) # don't forget to count yourself
mine_sdr = np.zeros((1,1)) # the places I can reach before anyone else
prev_x = 0
prev_y = 0

def decide(data):
    start = time()
    board=makeboard(data)
    # Later try ?vector fields? .. many steps of free space ahead is same but closed/walled-off spaces get exponentially worse.
    # Later try heading to corners?

    # Decision time!
    # Raw value
    space = deadly_neighbours()
    
    # Give line of smell-
    space = list(map(lambda a,b:a+np.mean(b), space, [board[:hy+1,hx+1],board[hy+1,hx+2:],board[hy+2:,hx+1],board[hy+1,:hx+1]]))

    # Give randomness
    space = list(map(lambda a,b:a+b/2, space,np.random.rand(4)))


    decision = space.index(max(space))
    end = time()
    sho("RUNTIME: {0}ms. AIM < 120ms, currently using {1}%".format(((end - start) * 1000),(((end - start) * 1000) / 1.2)))
    return decision

def makeboard(data):
	food = list(zip(find('x',data.get("food")),find('y',data.get("food"))))
    w = data.get("width")
    h = data.get("height")
    food_sdr.resize(h,w)
    prey_sdr.resize(h,w)
    wall_sdr.resize(h,w)
    snake_data = data.get("snakes")["data"] 
    mySnake = data.get("you")
    myBod = list(zip(find('x',mySnake),find('y',mySnake)))
    X,Y = myBod[0] #current
    
    snakes=[] # Nested list of snake coords
    for snake in snake_data:
        snakes.append(zip(find('x',snake),find('y',snake)))
    
    # Make grid with edges (w+2)x(h+2) with survival score (-1 is ded?) and implement basic constraints
    board = np.zeros((h+2,w+2))
    board[0] = -1
    board.T[0] = -1
    board.T[w+1] = -1
    board[h+1] = -1

    # Scores are context dependent (defined as behaviours like grow, chill, kill)
    if mySnake["health"] > 90:
        food_reward = 0
    elif mySnake["health"] > 70:
        food_reward = 0.1
    elif mySnake["health"] > 50:
        food_reward = 0.5
    elif mySnake["health"] > 20:
        food_reward = 5
    else:
    	food_reward = 10
    # Scores given to +events can be varied later to tune behaviour
    
    for x,y in food_points:
        board[y+1,x+1] = food_reward # * (math.fabs(x-hx)+math.fabs(y-hy)+2)

    for x,y in snake_points:
        board[y+1,x+1] = -1

    board[hy+1,hx+1] = -5

	return board

def deadly_neighbours(x,y,grid):
	return list(pt, pt, pt, pt)