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
EMPTY=0
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
def put_item(lineid, pointer, value, total):
    if value==BLOCK:
        total-=1
    linelist[lineid].content[pointer]=value
    otherline=pointer+n if lineid<n else pointer
    otherpointer=(lineid+n)%n
    linelist[otherline].content[otherpointer]=value
    return total

def no_block_here(lineid, pointer, value):
    if linelist[lineid].content[pointer]==value:
        return False
    return True

def full_fill_line(lineid, total):
    lastpoint=0
    for block in linelist[lineid].blocks:
        i=0
        while i < block:
            if no_block_here(lineid, lastpoint, BLOCK):
                total = put_item(lineid, lastpoint, BLOCK, total)
            lastpoint+=1
            i+=1
        if lastpoint!=n:
            put_item(lineid, lastpoint, NOBLOCK, total)
            lastpoint+=1
            i+=1         
    return total

def solve_fulls(n, linelist, total):
    for i in range(2*n):
        if linelist[i].mintot==n:
            total=full_fill_line(i, total)
            linelist[i].isfinished=1
            # print(total)
            # print_it()
            # input()
    
    return total

# Main idea behind filling the half lines is this:
# The difference between the minimum length of one line and the size n, gives us how many 
# less a block will have pixels. Lets say size is 10 and we have 5 2 two pieces.
# Minimum length needed is 5+2+1(space between)=8.
# Difference from size is 10-8=2.
# For the first piece 5-2(diff)=3. We will put 3 pixel for this one. And then jump one as space
# After that we calculate the diff again. 2-2=0 this time. so we don't fill any pixel, but add 
# it to our last pointer. Then add one more for space. This way it can fill all the halfs.
def half_fill_line(lineid, total, difference):
    lastpoint=0
    for block in linelist[lineid].blocks:
        lastpoint+=difference
        diffb=block-difference
        if diffb > 0:
            i=0
            while i < diffb:
                if no_block_here(lineid, lastpoint, BLOCK):                    
                    total=put_item(lineid, lastpoint, BLOCK, total)
                lastpoint+=1
                i+=1
        lastpoint+=1   
            
    return total

def solve_halfs(n, linelist, total):
    for i in range(2*n):
        if linelist[i].mintot>n/2 and linelist[i].max>(n-linelist[i].mintot): # first condition checks if there is possibility for half filling. Second one checks in that possibility can we fill any block. Maybe total length is long enough but pieces are all 2's and 1's.
            total=half_fill_line(i, total, n-linelist[i].mintot)
            # print(total)
            # print_it()
            # input()
    
    return total

def start_counting(lineid, lastpoint):
    count=0
    while linelist[lineid].content[lastpoint] == 1:
        count+=1
        lastpoint+=1
    return lastpoint, count

def add_x_to_both_end(lineid, pointer, block, n):
    if pointer < n and linelist[lineid].content[pointer]!= NOBLOCK :
        put_item(lineid, pointer, NOBLOCK, total)
    if pointer-block-1>=0 and linelist[lineid].content[pointer]!= NOBLOCK :
        put_item(lineid, pointer-block-1, NOBLOCK, total)

def x_out(lineid):
    for i in range(n):
        if linelist[lineid].content[i] == EMPTY:
            put_item(lineid, i, NOBLOCK, total)

#Gotta work more on this value check function. This is the most important part.
def val_check(n, lineid):
    isfin=1
    lastpoint=0
    for block in linelist[lineid].blocks:
        didyouenter=1
        while lastpoint < n:
            if linelist[lineid].content[lastpoint] == 1:
                didyouenter=0
                lastpoint, blcount=start_counting(lineid, lastpoint)
                if blcount == block:
                    add_x_to_both_end(lineid, lastpoint, block, n)
                else:
                    isfin = 0
            else:
                lastpoint+=1
        if didyouenter==1:
            isfin = 0
        lastpoint+=1
           
    if isfin==1:
        linelist[lineid].isfinished=1
        x_out(lineid)
    
    return

def solve_rest(n, linelist, total):
    
    while total>0:
        for i in range(n):
            if linelist[i].isfinished==0:
                val_check(n, i)
    return total

def solve_it(n, linelist, total):
    
    
    total = solve_fulls(n, linelist, total)
     
    total = solve_halfs(n, linelist, total)
    
    total = solve_rest(n, linelist, total)
    print(total)
    print_it()

if __name__=="__main__":
    n, linelist, total = take_inputs()
    solve_it(n,linelist,total)
