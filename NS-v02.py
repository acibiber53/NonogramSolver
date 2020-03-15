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

class Lines():
    def __init__(self, lineid, verticality, blocks, length):
        self.lineid=lineid
        self.verticality=verticality
        self.blocks=blocks
        self.blockquantity=len(blocks)
        self.min=min(blocks)
        self.max=max(blocks)
        self.mintot=sum(blocks)+len(blocks)-1 #sum of all blocks plus one space between each pair. Minimum length required to finish all blocks
        self.isfinished=0
        self.content=[0]*length
        
    def __str__(self):
        return "LineID: %s, Verticality: %s, %s blocks shaped like %s, where min %s and max %s, line min lenght is %s" % (self.lineid, self.verticality, self.blockquantity, self.blocks, self.min, self.max, self.mintot)

#Just for writing whole lines list, maybe will be discarded in the future
def writelines(linelist):
    for i in range(len(linelist)):
        print(linelist[i])

def takeinputs():
    #Getting the input
    with open('nono.txt','r') as file:
        content=file.readlines()
        n=int(content[0])
        for i in range(len(content)):
            content[i]=content[i].replace('\n','')
        blocks=content[1:]
    
    #initializing lines list with Lines class    
    linelist=list()
    for i in range(len(blocks)):
        blocks[i]=blocks[i].split(' ')
        blocks[i] = list(map(int, blocks[i]))
        linelist.append(Lines(i, 0 if i<n else 1, blocks[i], n))
        
    writelines(linelist)   
        
    print(linelist[5].content)
    total=0
    for i in range(n):
        total+=sum([int(i) for i in list(blocks[i])])

    return n, linelist, total


if __name__=="__main__":
    takeinputs()
