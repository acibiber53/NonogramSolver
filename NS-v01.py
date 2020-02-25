# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 20:27:14 2020

@author: Ubeydullah SARK
Student ID: 19456662
"""

#+First I will try to create fully fillings matrix for different sizes. We can get this number from use and print out the output
#Make the board fill the fulls and nulls

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
    
    
def fullfinder(parts,size):
    i=1
    result=list()
    while i <= parts:
        result.append(levelsearch(i,size))        
        i+=1
    result=(','.join(result)).split(',')
    return result
    

def printing(board):
    print('\n'.join([' '.join([elem for elem in row])for row in board]))

def filler(size, fulls):
    board=[['0']*n for i in range(n)]
    printing(board)

if __name__=='__main__':
    n=int(input("How big is this square, honey?"))
    fulls=fullfinder(int((n+1)/2),n)
    filler(n,fulls)
    