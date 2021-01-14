#!/usr/bin/python
#Alchetra.py
#Parth Parakh, 14th Jan'21 
#purpose: coding question

#---------------------------------------------------------------------
#import modules
import sys
import csv
#---------------------------------------------------------------------
#helper function
def getfile():
    x = set();
    with open(sys.argv[1],"r")as f:
        csv_reader = csv.reader(f,delimiter=',')
        for row in csv_reader:
            for name in row:
                if(name[0]==' '):
                    name = name[1:]
                x.add(name)
    return x
#---------------------------------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
#Graph class
class Graph: 
    def __init__(self, V):
        self.V = V 
        self.visited = {}
        self.graph = {}
        self.curr_graph = []
        self.result = 0;
        self.count = 1;
        
 #this method is used to create a graph which is essentially a collection of adjacency lists
    def add(self):
        with open(sys.argv[1],"r")as f:
            d = set()
            csv_reader = csv.reader(f,delimiter=',')
            for row in csv_reader:
                if row[0] in d:   # if key is already present then throw error
                    return 0
                else:
                    d.add(row[0])
                head = Node(row[0])
                n = head
                for name in row[1:]:
                    if(name[0]==' '):  # removing space is present
                        name = name[1:]
                    node = Node(name)
                    n.next = node
                    n = n.next
                self.graph[head.value] = head.next # since head is used as key, we cant include it in our data.
                #Alice : Dinesh->carol ( correct) ;  Alice : Alice->Dinesh->carol (incorrect)
    
    def DFS(self,v):  
        self.count+=1
        self.visited[v] = True;
        for name in self.graph:
            if (name==v):
                val = self.graph[name];
                    while(val.next!=None):
                        if(self.visited[val.value]!=True):
                            self.DFS(val.value)
                        val = val.next 
        return 0;
    
    def countCycles(self,V):  
        for name in V:  
            self.count=0
            self.visited = dict.fromkeys(V,False)
            self.visited[name]=True
            self.DFS(name)  
            self.result = max(self.result,self.count)
        return self.result; 
#-----------------------------------------------------------------------------------
# main caller
if __name__ == '__main__':
    try:
        V = getfile()
    except IndexError:
        print("Please specify a file")
        sys.exit(1)
    g = Graph(V)
    if(g.add()==0):
        print("Error : please check the file")
        sys.exit()
    print(g.countCycles(V))
#-----------------------------------------------------------------------------------