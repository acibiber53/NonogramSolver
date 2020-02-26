# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 20:27:14 2020

@author: Ubeydullah SARK
Student ID: 19456662
"""

#+First I will try to create fully fillings matrix for different sizes. We can get this number from use and print out the output
#Make the board fill the fulls and nulls

BLK='\u2588' # block character

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
def fillfull(board, fulls, blocks, total, unfinished):

    for i in range(n):
        if blocks[i] in fulls:
            unfinished.remove(i)
            parting=list(fulls[fulls.index(blocks[i])])
            indexc=0
            for item in parting:
                for j in range(int(item)):
                    board[i][indexc]=BLK 
                    indexc+=1
                if indexc<n:
                    board[i][indexc]='X'
                    indexc+=1
    i+=1
    limi=2*n
    while i<limi:
        col=i-n
        if blocks[i] in fulls:
            unfinished.remove(i)
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
    #print(t)
    total-=t
    
    return board, total, unfinished

def fillhalf(board, blocks, unfinished, size):
    halftotal=list()
    for i in unfinished:
        tmp=[int(i) for i in list(blocks[i])]
        ss=sum(tmp)+(len(tmp)-1)
        halftotal.append([ss,len(tmp),size-ss]) # totallength, howmanyparts, size-totallength
    
    for i in range(len(unfinished)):
        truindex=unfinished[i]
        if truindex<size: #rows
            if halftotal[i][0]>halftotal[i][2]: # check if the parts total are bigger than the size-parts_total, if yes we can still predict some tiles
                tmp=[int(i) for i in list(blocks[truindex])] #get parts
                lt=len(tmp)
                writeindex=0
                for j in range(lt): # iterate through the parts
                    item=tmp[j]
                    tindex=writeindex+item-1
                    diff=item-halftotal[i][2] # how many blocks we write
                    while diff > 0:
                        board[truindex][tindex]=BLK
                        diff-=1
                        tindex-=1
                    writeindex=writeindex+item+1
        else:  #columns
            col=truindex-size
            if halftotal[i][0]>halftotal[i][2]: # check if the parts total are bigger than the size-parts_total, if yes we can still predict some tiles
                tmp=[int(i) for i in list(blocks[truindex])] #get parts
                lt=len(tmp)
                writeindex=0
                for j in range(lt): # iterate through the parts
                    item=tmp[j]
                    tindex=writeindex+item-1
                    diff=item-halftotal[i][2] # how many blocks we write
                    while diff > 0:
                        board[tindex][col]=BLK
                        diff-=1
                        tindex-=1
                    writeindex=writeindex+item+1
                    
    return board, unfinished

# This method will slowly fill the board
def filler(size, blocks, total):
    fulls=fullfinder(int((size+1)/2),size)
    unfinished=[i for i in range(size*2)]
    
    board=[['_']*n for i in range(n)]

    board, total, unfinished=fillfull(board, fulls, blocks, total, unfinished)
    
    board, unfinished=fillhalf(board, blocks, unfinished, size)
    printing(board)
    #main check while
#    while total > 0:
        
#        for i in unfinished:
            #check if it is already finished
            
    

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
    