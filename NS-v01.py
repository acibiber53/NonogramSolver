# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 20:27:14 2020

@author: Ubeydullah SARK
Student ID: 19456662
"""

#+First I will try to create fully fillings matrix for different sizes. We can get this number from use and print out the output
#Make the board fill the fulls and nulls

BLK='\u2588'

# This is recursive method that finds all possible line filling combinations for given size
def levelsearch(partnumber, size):
    if partnumber==1:
        return str(size)
    if size==1:
        return str(1)
    if size==2:
        return str(2)
    
    k=list()
    small=1
    big=size-((partnumber-1)*2)
    while small <= big:
        k.append(','.join([str(small)+stringo for stringo in levelsearch(partnumber-1,size-small-1).split(',')]))
        small+=1
    return ','.join([i for i in k])
    

# This method finds all full methods for the board size    
def fullfinder(parts,size):
    i=1
    result=list()
    while i <= parts:
        result.append(levelsearch(i,size))        
        i+=1
    result=(','.join(result)).split(',')
    return result
    
# This method writes board out
def printing(board):
    print('\n\n'.join(['  '.join([elem for elem in row])for row in board]))


# This method only fills the full lines at the beginning.
def fillfull(board, fulls, blocks, total):

    for i in range(n):
        if blocks[i] in fulls:
            parting=list(fulls[fulls.index(blocks[i])])
            indexc=0
            for item in parting:
                for j in range(int(item)):
                    board[i][indexc]=BLK # block character
                    indexc+=1
                if indexc<n:
                    board[i][indexc]='X'
                    indexc+=1
    i+=1
    limi=2*n
    while i<limi:
        col=i-n
        if blocks[i] in fulls:
            parting=list(fulls[fulls.index(blocks[i])])
            indexr=0
            for item in parting:
                for j in range(int(item)):
                    board[indexr][col]=BLK
                    indexr+=1
                if indexr<n:
                    board[indexr][col]='X'
                    indexr+=1
        i+=1
    t=0
    for row in board:
        t+=row.count(BLK)
    print(t)
    total-=t
    printing(board)
    return board, total


# This method will slowly fill the board
def filler(size, blocks, total):
    fulls=fullfinder(int((size+1)/2),size)
    
    board=[['_']*n for i in range(n)]

    board, total=fillfull(board, fulls, blocks, total)
    
    

# This method gets input from a txt file. First line is board size n . Next n line row values, next n line column values.
def takeinputs():
    with open('nono.txt','r') as file:
        content=file.readlines()
        n=int(content[0])
        for i in range(len(content)):
            content[i]=content[i].replace('\n','')
        blocks=content[1:]
        
    for i in range(len(blocks)):
        if ' ' in blocks[i]:
            blocks[i]=blocks[i].replace(' ','')
    total=0
    for i in range(n):
        total+=sum([int(i) for i in list(blocks[i])])
       
    return n, blocks, total

if __name__=='__main__':
    n, blocks, total=takeinputs()
    
    
    filler(n, blocks, total)
    