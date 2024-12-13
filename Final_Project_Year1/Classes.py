import random as rd
import time

#timer class
class Timer:
    #the variable
    def __init__(s):
        s._start:int = 0
        s._end:int = 0

    #display the time passed
    def display_time(s):
        from math import floor
        T = s._end - s._start
        min = floor(T//60)
        sec = floor(T%60)
        return f'{min} minutes {sec} seconds'
    
    def get_time(s):
        if (s._start == 0) or (s._end == 0):
            return 2678400
        else:
            return s._end - s._start
    
    #take note of time for start then end
    def timed(s):
        if s._start == 0:
            s._start = time.time()
        else:
            s._end = time.time()

    #reset the timer
    def clear_time(s):
        s._start = 0
        s._end = 0
    
    #reset the end time
    def clear_end(s):
        s._end = 0

#sudoku class
class Sudoku(Timer):
    #initalizing
    def __init__(s):
        s.grid = [[0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0]]
        s.__ranges = [1,2,3,4,5,6,7,8,9]
        s.__lock = []
        super().__init__()
    
    #add lock coordinate
    def add_lock(s,x,y):
        if [x,y] not in s.__lock:
            s.__lock.append([x,y])
    
    #clear lock
    def clear_lock(s):
        s.__lock = []
    
    #check coordinate not locked
    def lock(s,x,y):
        if [x,y] in s.__lock:
            return False
        else:
            return True

    #display grid
    def __str__(s):
        display = ""
        for i in range(9):
            display += str(s.grid[i])
            if i < 8:
                display += "\n"
        return display
    
    def display(s):
        return s.grid
    
    #insert answer
    def insert(s,x,y,ans):
        if ans in s.__ranges:
            if s.lock(x,y):
                s.grid[y][x] = ans
    
    #delete specified answer
    def delete(s,x,y):
        if s.lock(x,y):
            s.grid[y][x] = 0
    
    #clear grid
    def clear(s):
        for y in range(9):
            for x in range(9):
                s.grid[y][x] = 0
        s.clear_lock()

    #clear answer
    def clear_answer(s):
        for y in range(9):
            for x in range(9):
                if [x,y] not in s.__lock:
                    s.grid[y][x] = 0
    
    #check if grid has empty answer
    def checkempty(s):
        flag = False
        for i in range(9):
            for j in range(9):
                if s.grid[i][j] == 0:
                    flag = True
                    break
        if flag:
            return True
        else:
            return False
            
    #check answer
    def correct(s):
        if s.checkempty() == False:  #check for empty value
            #check no dupe in row or column
            for x in range(9):
                check = []
                #row check
                if len(s.grid[x]) != len(set(s.grid[x])):  #the 'x' variable is the y-axis for this line specifically
                    return False
                #column check
                for y in range(9):
                    check.append(s.grid[y][x])
                    if len(check) != len(set(check)):
                        return False
            #3x3 grid check for dupe
            for y in range(0,7,3):
                count = 0
                while count<3:
                    for x in range(0,7,3):
                        a = []
                        for y1 in range(3):
                            for x1 in range(3):
                                a.append(s.grid[y+y1][x+x1])
                        if len(a) != len(set(a)):
                            return False
                    count += 1
            return True
        else:   #if there is an empty value (0)
            return False
    
    #create random sudoku (WIP)
    def make_sudoku(s):
        #still in progress
        while True:
            for y in range(9):
                rd.shuffle(s.__ranges)
                while True:
                    if s.__ranges not in s.grid:
                        s.grid[y]=s.__ranges.copy()
                        break
                s.__ranges.sort()
            if s.correct():
                break
    
    #make sudoku (copy)
    #Source: https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
    def make_sudoku_copy(s):
        base  = 3
        side  = base*base

        # pattern for a baseline valid solution
        def pattern(r,c): return (base*(r%base)+r//base+c)%side

        # randomize rows, columns and numbers (of valid base pattern)
        def shuffle(s): return rd.sample(s,len(s)) 
        rBase = range(base) 
        rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
        cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
        nums  = shuffle(range(1,base*base+1))

        # produce board using randomized baseline pattern
        s.grid = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

    #empty sudoku to present user
    def empty_random(s):
        for y in range(9):
            for x in range(9):
                if rd.randint(1,5) < 4:
                    s.grid[y][x] = 0
                else:
                    s.add_lock(x,y)
