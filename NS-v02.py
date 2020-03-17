# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 00:54:03 2020

@author: acibi

I will try to solve nonogram one more time. With this program I will try to utilize
classes. I aim to make lines into objects. Every line has many attributes such as being 
vertical/horizontal, finished/unfinished, how many blocks in it, is it full at the beginning or not
connections with the vertical/horizontal lines. 

Main purpose here is to learn how to use classes, so nothing to lose. Let's begin.
"""

BLOCK=1
NOBLOCK=-1

class Lines():
    """
    LineID is from 0 to 2*n-1, inclusive, keeps ID of all the lines.
    Iscolumn is showing if the lines is row or column. 0 for row, 1 for column
    Blocks hold all the pixel blocks that make a line
    Blockquantity is showing how many parts makes the line
    min is the smallest block
    max is the biggset block
    mintot is sum of all blocks plus one space between each pair. Minimum length required to finish all blocks
    isfinished shows if the line is finished. 0 is not finished, 1 is finished.
    Content shows which parts are already filled. 0 is empty, 1 is block, -1 is X.
    """
    
    def __init__(self, lineid, iscolumn, blocks, length):
        self.lineid=lineid 
        self.iscolumn=iscolumn
        self.blocks=blocks
        self.blockquantity=len(blocks)
        self.min=min(blocks)
        self.max=max(blocks)
        self.mintot=sum(blocks)+len(blocks)-1 
        self.isfinished=0
        self.content=[0]*length
            
        
    def __str__(self):
        return "LineID: %s, Verticality: %s, %s blocks shaped like %s, where min %s and max %s, line min lenght is %s" % (self.lineid, self.verticality, self.blockquantity, self.blocks, self.min, self.max, self.mintot)

#Just for writing whole lines list, maybe will be discarded in the future
def writelines(linelist):
    for i in range(len(linelist)):
        print(linelist[i])

def take_inputs():
    #Getting the input
    with open('nono.txt','r') as file:
        content=file.readlines()
        n=int(content[0])
        for i in range(len(content)):
            content[i]=content[i].replace('\n','')
        blocks=content[1:]
    
    #initializing lines list with Lines class    
    total=0
    linelist=list()
    for i in range(len(blocks)):
        blocks[i]=blocks[i].split(' ')
        blocks[i] = list(map(int, blocks[i]))
        linelist.append(Lines(i, 0 if i<n else 1, blocks[i], n))
        total+=sum(blocks[i])
        
    #writelines(linelist)   
    total=int(total/2)

    return n, linelist, total

def print_it():
    for i in range(n):
        print(''.join([(str(elem)).rjust(3, ' ') for elem in linelist[i].content]))


# This function puts row and column values together
# It helps me to eliminate the need for adding if/else to check iscolumn of each line
def put_item(lineid, pointer, value):
    linelist[lineid].content[pointer]=value
    otherline=pointer+n if lineid<n else pointer
    otherpointer=(lineid+n)%n
    linelist[otherline].content[otherpointer]=value


def full_fill_line(lineid):
    lastpoint=0
    for block in linelist[lineid].blocks:
        i=0
        while i < block:
            put_item(lineid, lastpoint, BLOCK)
            lastpoint+=1
            i+=1
        if lastpoint!=n:
            put_item(lineid, lastpoint, NOBLOCK)
            lastpoint+=1
            i+=1            

def solve_fulls(n, linelist, total):
    for i in range(2*n):
        if linelist[i].mintot==n:
            full_fill_line(i)

def solve_it(n, linelist, total):
    
    solve_fulls(n, linelist, total)
    print_it()

if __name__=="__main__":
    n, linelist, total = take_inputs()
    solve_it(n,linelist,total)
