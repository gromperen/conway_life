import time

N = 40
grid = [[0]*N for i in range(N)]
gridbuffer = grid
w = 20
paused = True

def setup():
    size(1000, 1000)

def draw():
    global grid
    if not paused:
        grid = gameoflife()
    x,y = 0,0
    for row in grid:
        for col in row:
            if col == 1:
                fill(255,0,0) #red
            else:
                fill(255) #white
            rect(x, y, w, w)
            x += w
        x = 0
        y += w
    if paused:
        fill(254, 254, 119) #yellow
    else:
        fill(142, 254, 119) #green
    rect(850, 0, 50, 50)
        
def mousePressed():
    print mouseX//w, mouseY//w
    x = mouseX//w
    y = mouseY//w
    if x < N and y < N:
        if grid[y][x] == 0:
            grid[y][x] = 1
        elif grid[y][x] == 1:
            grid[y][x] = 0

def keyPressed():
    global paused
    print(keyCode)
    print(key)
    if keyCode == 32: 
        if paused:
            paused = False
        elif not paused:
            paused = True
            
def gameoflife():
    global gridbuffer
    global grid
    for i in range(len(grid)):
        for j in range(len(grid)):
            nbs = checknbs(i, j, grid)
            print("neighbors" + str(nbs))
            if nbs == 3:
                gridbuffer[i][j] = 1
            elif nbs == 2 and grid[i][j] == 1:
                gridbuffer[i][j] = 1
            elif nbs < 2 or nbs > 3:
                gridbuffer[i][j] = 0
            else:
                gridbuffer[i][j] = 0
    time.sleep(1)
    return gridbuffer

def checknbs(i, j, grid):
    total = 0
    try:
        total += grid[i-1][j-1]
    except:
        print("bruh")
    try:
        total += grid[i][j-1]
    except:
        print("bruh")
    try:
        total += grid[i+1][j-1]
    except:
        print("bruh")
    try:
        total += grid[i-1][j]
    except:
        print("bruh")
    try:
        total += grid[i+1][j]
    except:
        print("bruh")
    try:
        total += grid[i-1][j+1]
    except:
        print("bruh")
    try:
        total += grid[i][j+1]
    except:
        print("bruh")
    try:
        total += grid[i+1][j+1]
    except:
        print("bruh")
    print("total ="+ str(total))
    return total
