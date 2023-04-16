#!/usr/bin/python3
#MCTF23
#geoz

import socket
import networkx

HOST = "mazelanding.misc.midnightflag.fr"
PORT =  17001

def FindShorthestPath(rawMaze):
    graph = networkx.DiGraph()
    maze = [] 
    
    for elt in rawMaze:
        if elt == "■":
            maze.append(False)
        elif elt ==".":
            maze.append(True)
        elif elt == "✈":
            maze.append("S")
        elif elt == "𓊹":
            maze.append("E")
    
    yLength = len(rawMaze.split("\n"))
    xLength = int(len(maze) / yLength)
    
    start = (maze.index("S")//xLength, maze.index("S")%xLength)
    end = (maze.index("E")//xLength, maze.index("E")%xLength)
    maze[maze.index("S")] = True
    maze[maze.index("E")] = True

    # A little bit dirty but it works :)
    for i in range(len(maze)):
        if maze[i]:
            try :
                if maze[i + 1]:
                    j = i + 1
                    graph.add_edge((i//xLength, i%xLength), (j//xLength, j%xLength))
            except :
                continue
            try :
                if maze[i - 1]:
                    j = i - 1
                    graph.add_edge((i//xLength, i%xLength), (j//xLength, j%xLength))
            except :
                continue
            try :
                if maze[i + xLength]:
                    j = i + xLength
                    graph.add_edge((i//xLength, i%xLength), (j//xLength, j%xLength))
            except :
                continue
            try :
                if maze[i - xLength]:
                    j = i - xLength
                    graph.add_edge((i//xLength, i%xLength), (j//xLength, j%xLength))
            except :
                continue
    
    return networkx.shortest_path(graph,start,end)


socket = socket.socket()  
socket.connect((HOST, PORT))  
data = socket.recv(4096).decode()
print('[MIDNIGHTFLAG23]\n' + data + '\n[\\MIDNIGHTFLAG23]\n')
socket.send("\n".encode())

while True :
    data = ""
    while True:
        data += socket.recv(4096).decode()
        if ">>" in data:
            break
        if "MCTF" in data :
            break
    print('[MIDNIGHTFLAG23]\n' + data + '\n[\\MIDNIGHTFLAG23]')
    rawMaze = data.split("Here is the maze, please help the plane !!\n\n")[1].replace("\n\n","\n").split('\n>>')[0].replace(" ","").replace("\r","")
    path = str(FindShorthestPath(rawMaze))
    print(path)
    socket.send(path.encode())
