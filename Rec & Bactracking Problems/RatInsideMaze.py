# maze = [[0,-1,0],
#         [0,0,-1],
#         [-1,0,0]
#      ]
maze = [[0,0,0],
        [0,-1,0],
        [0,0,0]
     ]

# display maze

def display(maze):
    for i in range(len(maze)):
        for j in range(len(maze)):
            print(maze[i][j],end="   ")
        print("")

"""
conditions :
if maze[][] == -1 : return 0   block occured
if i,j == len(maze) : return 1 rat reach the destination
if i,j > len(maze) or i,j < 0 : return 0 rat exceeded the boundary

"""
def numberofways(i,j,m,maze):
    if i > m or j > m or i < 0 or j <0:
        return 0
    elif i == m and j == m:
        return 1
    elif maze[i][j] == -1:
        return 0
    else:
        a = numberofways(i,j+1,m,maze) # move right
        b = numberofways(i+1,j,m,maze) # move down

        return a+b

    

print("######### MAZE #######")
display(maze)
print("#########################")
print("Number of ways to reach desination:",numberofways(0,0,len(maze)-1,maze))