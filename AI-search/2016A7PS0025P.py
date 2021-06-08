import copy
import turtle
import Tkinter as tk
import sys
import time

class state:
    def __init__(self,arr,start):
        self.arr = arr
        self.start = start


def initalstateGenerator (p):
    arr = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    x = 16*p/100
    x = 16 - x
    y = x/4
    r = 20 +x-1
    if y > 3 and x>=12:
        y = 3
    if x>0 :
        for j in range(y+1):
            for i in range(4):
                if x == i+j*4:
                    return state(arr,r)
                arr[20+i+j*4] = 0
                arr[i*4+j]=0
            if x/4 >= j+1:
                arr[16+j]=0
                
        if x>=13:
            arr[36]=0
            r = 36
        if x>=14:
            arr[37]=0
            r =37
        if x>=15:
            arr[38]=0
            r = 38
        if x==16:
            arr[39]=0
            r =39
        return state(arr,r)
    
    return state(arr,0)


def createrootnode (StateList1,StateList2,s):  # s = rootnode
    StateList1.append(s)
    StateList2.append(s)


def GoalTest(ps,numberOfSquares,GoalStates):           # ps = present state
    if numberOfSquares == 0:
        if ps.arr == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
            return True
    if numberOfSquares == 1:
        for i in range(30):
            if ps.arr == GoalStates[i].arr:
                return True
    if numberOfSquares == 2:
        for i in range(30,192):
            if ps.arr == GoalStates[i].arr:
                return True
    if numberOfSquares == 3:
        for i in range(192,840):
            if ps.arr == GoalStates[i].arr:
                return True
    return False

def addchild_DFS (ps,StateList1):
    for i in range(ps.start, 40):
        arr1 = copy.deepcopy(ps.arr)
        if ps.arr[i] == 1:
            arr1[i] = 0
            StateList1.insert(0,state(arr1,i))

def addchild_BFS (ps,StateList2):
    for i in range(ps.start, 40):
        arr1 = copy.deepcopy(ps.arr)
        if ps.arr[i] == 1:
            arr1[i] = 0
            StateList2.append(state(arr1,i))

def DFSearch (StateList1,numberOfSquares,GoalStates,t1):
    i = 1              #DFSearch
    print "DFS, each node took ",sys.getsizeof(StateList1[0]) ," bytes"
    while  StateList1 :
        ps = StateList1[0]
        draw_state(ps,t1)
        if GoalTest(ps,numberOfSquares,GoalStates) == True:
            print "DFS nodes are ",i
            print "DFS took memory ",i*64," bytes"
            print "DFS GoalState",ps.arr
            return ps
        StateList1.remove(ps)
        addchild_DFS(ps,StateList1)
        i =i + 1
    print "No GoalState"
    return None

def BFSearch (StateList2,numberOfSquares,GoalStates,t2):   
    i = 1           #BFSearch
    print "BFS, each node took ",sys.getsizeof(StateList2[0]) ," bytes"
    while  StateList2 :
        ps = StateList2[0]
        draw_state(ps,t2)
        if GoalTest(ps,numberOfSquares,GoalStates) == True:  
            print "BFS nodes are ",i
            print "BFS took memory ",i*64," bytes"
            print "BFS GoalState",ps.arr
            return ps
        StateList2.remove(ps)
        addchild_DFS(ps,StateList2)
        i = i+1
    print "No GoalState"
    return None
            
def goalstates (GoalStates):
    arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    # 1 square  range(30)
    
    #-----------------------------------------------   1  square 1 x 1  = 16
    for i in range(16):
        for j in range(20,36):
            arr1 = copy.deepcopy(arr)
            arr1[i] = 1
            arr1[i+4] = 1
            arr1[j] = 1
            arr1[j+4] = 1
            GoalStates.append(state(arr1,j+4))

    #----------------------------------------------    1 square 2 x 2   =  9
    for i in range(3):
        for j in range(3):
            arr1 = copy.deepcopy(arr)
            arr1[i*4 + j] = 1
            arr1[i*4 + j + 1] = 1
            arr1[i*4 + j + 8] = 1
            arr1[i*4 + j + 9] = 1
            arr1[20 + i + j*4] = 1
            arr1[21 + i + j*4] = 1
            arr1[28 + i + j*4] = 1
            arr1[29 + i + j*4] = 1
            GoalStates.append(state(arr1,29 + i + j*4))
            
    #----------------------------------------------    1 square 3 x 3   =  4
    for i in range(2):
        for j in range(2):
            arr1 = copy.deepcopy(arr)
            arr1[i*4 + j] = 1
            arr1[i*4 + j + 1] = 1
            arr1[i*4 + j + 2] = 1
            arr1[i*4 + j + 12] = 1
            arr1[i*4 + j + 13] = 1
            arr1[i*4 + j + 14] = 1
            arr1[20 + i + j*4] = 1
            arr1[21 + i + j*4] = 1
            arr1[22 + i + j*4] = 1
            arr1[32 + i + j*4] = 1
            arr1[33 + i + j*4] = 1
            arr1[34 + i + j*4] = 1
            GoalStates.append(state(arr1,34 + i + j*4))

    #----------------------------------------------    1 square 4 x 4   =  1
    arr1 = [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]
    GoalStates.append(state(arr1,39))

    # 2 squares  range(30,192)

    #--------------------------------------------   2 squares 1 x 1  = 120
    for i in range(15):
        for j in range(i+1,16):
            arr1 = copy.deepcopy(arr)
            for k in range(40):
                arr1[k] =GoalStates[i].arr[k] + GoalStates[j].arr[k]
                if arr1[k] ==2:
                   arr1[k] =1
            GoalStates.append(state(arr1,GoalStates[j].start))

    #--------------------------------------------   2 squares 3 x 3  = 6
    for i in range(16,24):
        for j in range(i+1,25):
            arr1 = copy.deepcopy(arr)
            for k in range(40):
                arr1[k] =GoalStates[i].arr[k] + GoalStates[j].arr[k]
                if arr1[k] ==2:
                   arr1[k] =1
            GoalStates.append(state(arr1,GoalStates[j].start))

    #--------------------------------------------   2 squares 2 x 2  = 36
    for i in range(33,28):
        for j in range(i+1,29):
            arr1 = copy.deepcopy(arr)
            for k in range(40):
                arr1[k] =GoalStates[i].arr[k] + GoalStates[j].arr[k]
                if arr1[k] ==2:
                   arr1[k] =1
            GoalStates.append(state(arr1,GoalStates[j].start))

    # 3 squares  range(192,840)

    #--------------------------------------------  3 squares 1 x 1  = 560
    for i in range(14):
        for j in range(i+1,15):
            for k in range(j+1,16):
                arr1 = copy.deepcopy(arr)
                for m in range(40):
                    arr1[m] =GoalStates[i].arr[m] + GoalStates[j].arr[m] + GoalStates[k].arr[m] 
                if arr1[m] > 1:
                   arr1[m] = 1
                GoalStates.append(state(arr1,GoalStates[k].start))

    #--------------------------------------------  3 squares 2 x 2  = 84
    for i in range(16,23):
        for j in range(i+1,24):
            for k in range(j+1,25):
                arr1 = copy.deepcopy(arr)
                for m in range(40):
                    arr1[m] =GoalStates[i].arr[m] + GoalStates[j].arr[m] + GoalStates[k].arr[m] 
                if arr1[m] > 1:
                   arr1[m] = 1
                GoalStates.append(state(arr1,GoalStates[k].start))

    #--------------------------------------------  3 squares 3 x 3  = 4
    for i in range(33,27):
        for j in range(i+1,28):
            for k in range(j+1,29):
                arr1 = copy.deepcopy(arr)
                for m in range(40):
                    arr1[m] =GoalStates[i].arr[m] + GoalStates[j].arr[m] + GoalStates[k].arr[m] 
                if arr1[m] > 1:
                   arr1[m] = 1
                GoalStates.append(state(arr1,GoalStates[k].start))
    
    return GoalStates


# GUI ------------------------
def draw_h(t):                      # transvers 135px and dot of 15
    t.color("yellow")            
    t.fd(135)
    t.color("red")
    t.dot(15)
    
def draw_v(t):                      # transvers 135px and dot of 15
    t.color("red")
    t.dot(15)
    t.color("yellow")
    t.fd(135)

def jump(t):
    t.color("white")
    t.fd(135)

# Start -----------           Displays the state
def draw_state(ps,t):
    t.up()
    t.goto(-270,270)
    t.setheading(0)
    t.down()
    for i in range(4):
        if ps.arr[i] == 1:
            draw_h(t) 
        else:
            jump(t)
    t.up()
    t.goto(-270,135)
    t.down()
    for i in range(4,8):
        if ps.arr[i] == 1:
            draw_h(t) 
        else:
            jump(t)
    t.up()
    t.goto(-270,0)
    t.down()
    for i in range(8,12):
        if ps.arr[i] == 1:
            draw_h(t) 
        else:
            jump(t)
    t.up()
    t.goto(-270,-135)
    t.down()
    for i in range(12,16):
        if ps.arr[i] == 1:
            draw_h(t) 
        else:
            jump(t)
    t.up()
    t.goto(-270,-270)
    t.down()
    for i in range(16,20):
        if ps.arr[i] == 1:
            draw_h(t) 
        else:
            jump(t)
    t.up()
    t.goto(-270,270)
    t.setheading(270)
    t.down()
    for i in range(20,24):
        if ps.arr[i] == 1:
            draw_v(t) 
        else:
            jump(t)
    t.up()
    t.goto(-135,270)
    t.down()
    for i in range(24,28):
        if ps.arr[i] == 1:
            draw_v(t) 
        else:
            jump(t)
    t.up()
    t.goto(0,270)
    t.down()
    for i in range(28,32):
        if ps.arr[i] == 1:
            draw_v(t) 
        else:
            jump(t)
    t.up()
    t.goto(135,270)
    t.down()
    for i in range(32,36):
        if ps.arr[i] == 1:
            draw_v(t) 
        else:
            jump(t)
    t.up()
    t.goto(270,270)
    t.down()
    for i in range(36,40):
        if ps.arr[i] == 1:
            draw_v(t) 
        else:
            jump(t)
# ---------------------------------

#----------- MAIN PROGRAM ----------------------------------
 
       

print "ENTER THE VALUE OF PERCENTAGE"
p = int(raw_input())
print "ENTER THE VALUE OF SQUARES SHOULD BE LEFT"
numberOfSquares = int(raw_input())
root = tk.Tk()

# left frame to hold display
left = tk.Frame(root,height=200, width=260)
left.pack(side = tk.LEFT, fill= tk.Y)
left.configure(background= "black")

# right frame to hold buttons
middle = tk.Frame(root,height=600, width=550)
middle.pack(side = tk.LEFT, fill= tk.Y)
can1 = tk.Canvas(master=middle,width=553,height=600)
can1.pack()



# right frame to hold buttons
right = tk.Frame(root,height=600, width=550)
can2 = tk.Canvas(master=right,width=553,height=600)
right.pack(side = tk.LEFT, fill= tk.Y)
can2.pack()



#-------------------------- DFS Turtle ------------------------------
t1 = turtle.RawTurtle(can1)
t1.ht() # to hide turtle
t1.pensize(5)               # thickness
t1.speed(500000)

#-------------------------- BFS Turtle ------------------------------
t2 = turtle.RawTurtle(can2)
t2.ht() # to hide turtle
t2.pensize(5)               # thickness
t2.speed(500000)



StateList1 = []
StateList2 = []
GoalStates = []
goalstates (GoalStates)
s = initalstateGenerator(p)
createrootnode (StateList1,StateList2,s)
x = time.time()
result1 =  DFSearch (StateList1,numberOfSquares,GoalStates,t1)
print "DFS took time ", time.time() - x
x = time.time()
result2 =  BFSearch (StateList2,numberOfSquares,GoalStates,t2)
print "BFS took time ", time.time() - x
t1.exitonclick()
t2.exitonclick()
tk.mainloop()
