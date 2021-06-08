# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 01:20:03 2018

@author: 2016A7PS0025P(S.K.V.PURUSHOTHAM)
"""

import turtle
import Tkinter as tk
from datetime import datetime
import sys

class state:
    def __init__(self,arr,n):
        self.arr = arr
        self.n = n
        
def sumConstraint(s):
    n = s.n
    c = n*(n*n + 1)/2
    r = 0
    col =0
    d1 = 0
    d2 =0
    #---- rows,columns,diagonals --------
    for i in range(0,n):
        for j in range(0,n):
            r = r + s.arr[i][j]
            col = col + s.arr[j][i]
        d1 = d1 + s.arr[i][i]
        d2 = d2 + s.arr[i][n-1-i]
        if r == c and col == c:
            r = 0
            col = 0
        else:
            return 0
    if d1 == c and d2 == c:
        return 1
    else:
        return 0

#------------------ Alldiff -----
def allDiff(s):
    n =  s.n
    arr1 = [0 for h in range(n*n)]
    for k in range(0,n*n):
        for i in range(0,n):
            for j in range(0,n): 
               arr1[k] = s.arr[i][j]
    for k in range(0,n*n):
        for i in range(0,n*n): 
            if arr1[k] == arr1[i]:
                return 0
    return 1

# GUI ------------------------
# Start -----------           Displays the state
def draw_state(s,t):
    t.up()
    t.goto(-300,300)
    t.down()
    for k in range(0,n+1):
        t.fd(60*n)
        t.up()
        t.goto(-300,240- k*60)
        t.down()
    t.up()
    t.goto(-300,300)
    t.down()
    t.setheading(270)
    for k in range(0,n+1):
        t.fd(60*n)
        t.up()
        t.goto(-240+k*60,300)
        t.down()
    for i in range(0,n):
        for j in range(0,n):
            t.up()
            t.goto(-270+j*60,270-i*60)
            t.down()
            t.write(s.arr[i][j])

# ---------------------------------

#----------- MAIN PROGRAM ----------------------------------
 
       


root = tk.Tk()
root.title("main")
    
# left frame to hold display
left = tk.Frame(root,height=200, width=300)
#--------
lab =tk.Text(master = left,width=60,height=20,bg ="black",fg ="white")
lab.pack()


#-------
left.pack(side = tk.LEFT, fill= tk.Y)
left.configure(background= "yellow")


# right frame to hold buttons
right = tk.Frame(root,height=1000, width=1000)
can2 = tk.Canvas(master=right,width=600,height=600)
right.pack(side = tk.RIGHT, fill= tk.Y)
can2.pack()



t2 = turtle.RawTurtle(can2)
t2.ht() # to hide turtle
t2.pensize(5)               # thickness
t2.speed(500000)

#------------------- DFS_BT --------
def DFS_BT(s):
    n = s.n
    x =0
    x = heuristic1(s)
    if x==0 :
        s= state([[0 for h in range(n)]for y in range(n)],n)
        x = heuristic2(s)
        if x== 0 :
            s= state([[0 for h in range(n)]for y in range(n)],n)
            x = heuristic3(s)

    return s
    
#------------------------------- 4K multiple--------------
def heuristic1(s):
    n = s.n
	# 2-D matrix with all entries as 0
    s.arr = [[(n*y)+x+1 for x in range(n)]for y in range(n)]

	# Change value of s.array elements at fix location
	# as per the rule (n*n+1)-s.arr[i][[j]
	# Corners of order (n/4)*(n/4)
	# Top left corner
    for i in range(0,n/4):
        for j in range(0,n/4):
            s.arr[i][j] = (n*n + 1) - s.arr[i][j]


	# Top right corner
    for i in range(0,n/4):
        for j in range(3 * (n/4),n):
            s.arr[i][j] = (n*n + 1) - s.arr[i][j]

	# Bottom Left corner
    for i in range(3 * (n/4),n):
        for j in range(0,n/4):
            s.arr[i][j] = (n*n + 1) - s.arr[i][j]

	# Bottom Right corner
    for i in range(3 * (n/4),n):
        for j in range(3 * (n/4),n):
            s.arr[i][j] = (n*n + 1) - s.arr[i][j]

	# Centre of matrix,order (n/2)*(n/2)
    for i in range(n/4,3 * (n/4)):
        for j in range(n/4,3 * (n/4)):
            s.arr[i][j] = (n*n + 1) - s.arr[i][j]
    
    if sumConstraint(s) == 1 :
        return 1
    else :
        return 0

#----------------------------- ODD SQUARE----------------

def heuristic2(s):
	# 2-D s.array with all
	# slots set to 0
    n = s.n
    s.arr = [[0 for x in range(n)]for y in range(n)]
    
    if n%2 == 0:
        return 0
	# initialize position of 1
    i = n / 2
    j = n - 1

	# Fill the magic square
	# by placing values
    num = 1
    while num <= (n * n):
        if i == -1 and j == n: # 3rd condition
			j = n - 2
			i = 0
        else:

			# next number goes out of
			# right side of square
			if j == n:
				j = 0

			# next number goes
			# out of upper side
			if i < 0:
				i = n - 1

        if s.arr[int(i)][int(j)]: # 2nd condition
			j = j - 2
			i = i + 1
			continue
        else:
            s.arr[int(i)][int(j)] = num
            num = num + 1

        j = j + 1
        i = i - 1 # 1st condition


    if sumConstraint(s) == 1:
        return 1
    else :
        return 0    



def SubEven(n):
    s= state([[0 for x in range(n)]for y in range(n)],n)

	# initialize position of 1
    i = n / 2
    j = n - 1

	# Fill the magic square
	# by placing values
    num = 1
    while num <= (n * n):
		if i == -1 and j == n: # 3rd condition
			j = n - 2
			i = 0
		else:

			# next number goes out of
			# right side of square
			if j == n:
				j = 0

			# next number goes
			# out of upper side
			if i < 0:
				i = n - 1

		if s.arr[int(i)][int(j)]: # 2nd condition
			j = j - 2
			i = i + 1
			continue
		else:
			s.arr[int(i)][int(j)] = num
			num = num + 1

		j = j + 1
		i = i - 1 # 1st condition


    return s.arr
#------------------- 4k+2 form --------------
def heuristic3(s):
    x = n/2
    s.arr = [[0 for h in range(n)]for y in range(n)]
    subarray = SubEven(x)
#----------- 1st quadrant ---------
    for i in range(0, x):
		for j in range(0, x):
			s.arr[i][j] = subarray[i][j]
#-------- 2nd quadrant ----------
    for i in range(0, x):
		for j in range(0, x):
			s.arr[i][j+x] = subarray[i][j] + 2*x*x
#-------- 3rd quadrant ----------
    for i in range(0, x):
		for j in range(0, x):
			s.arr[i+x][j] = subarray[i][j] + x*x
#-------- 4th quadrant ----------
    for i in range(0,x):
		for j in range(0,x):
			s.arr[i+x][j+x] = subarray[i][j] + 3*x*x
#---- adjustments -------
    if n-6 != 0:
        y = (n-6)/4
        for j in range(0, y):
            for i in range(0, x):
                t = s.arr[i][n-1-y]
                s.arr[i][n-1-y] = s.arr[i+x][n-1-y]
                s.arr[i+x][n-1-y] = t
    y = (n-6)/4 + 1
#------- 1st row --------
    for j in range(0, y):
        t = s.arr[0][j]
        s.arr[0][j] = s.arr[x][j]
        s.arr[x][j] = t   
#------- last row -----
    for j in range(0, y):
        t = s.arr[x-1][j]
        s.arr[x-1][j] = s.arr[n-1][j]
        s.arr[n-1][j] = t 
#---------- middle rows --------
    for j in range(0, y):
        for i in range(1, x-1):
            t = s.arr[i][j+1]
            s.arr[i][j+1] = s.arr[i+x][j+1]
            s.arr[i+x][j+1] = t 

    if sumConstraint(s) == 1 and allDiff(s) == 1 :
        return 1
    else :
        return 0



# Driver Program
print "SQUARE SIDE LENGTH"
n = int(raw_input())
s= state([[0 for x in range(n)]for y in range(n)],n)
s = DFS_BT(s)
 
tstart = datetime.now()
draw_state(s,t2)
tend = datetime.now()
t = tend - tstart
#---
lab.insert(tk.INSERT,"time taken (h:m:s:ms) = ")
lab.insert(tk.INSERT,t)
lab.insert(tk.INSERT,"\n")
lab.insert(tk.INSERT,"memory for each node = ")
lab.insert(tk.INSERT,sys.getsizeof(s))
lab.insert(tk.INSERT,"\n")
lab.insert(tk.INSERT,"number of nodes =  ")
lab.insert(tk.INSERT,n*n)
lab.insert(tk.INSERT,"\n")
lab.insert(tk.INSERT,"total memory required for nodes = ")
lab.insert(tk.INSERT,sys.getsizeof(s)*n*n)
lab.insert(tk.INSERT,"\n")
tk.mainloop()