#!/usr/bin/python3
#Alchera.py
#Parth Parakh, 14th Jan'21 
#purpose: coding assessment
#---------------------------------------------------------------------
#import modules
import sys
import csv
import numpy as np
#---------------------------------------------------------------------
#helper function
#Helps with 2 things : returns a set(non repetitive elements) which helps us determine the total players 
#and is also used to validate if cmd line argument is present or not
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
#creating a class to create a node to store string
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
#Graph class
#all encompassing class with methods and variables. will be creating an object of the class and call methods off it
class Graph: 
    def __init__(self, V):
        self.V = V 
        self.visited = {}  
        self.index = {}
        self.map = []
        self.graph = {}
        self.count = 0
        self.result = 1;
        
#this method is used to create a graph which is a collection of adjacency lists
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
                    if(name[0]==' '):  # removing space if present
                        name = name[1:]
                    node = Node(name)
                    n.next = node
                    n = n.next
                self.graph[head.value] = head.next # since head is used as key, we cant include it in our data.
                #Alice : Dinesh->carol ( correct) ;  Alice : Alice->Dinesh->carol (incorrect)
    
    #since string cant be used as index, we map each player with a number and will subsequently use this corresponding number as index
    def create_index(self):
        i = 0;
        for name in self.V:
            self.index[name] = i
            i+=1
    
    #using the index created above we will create a table that stores relation between each player. This is needed since player can only pass to another player if he can both see and be seen by that player. to keep the time complexity down to O(n^2) we need a hashmap
    def create_map(self):
        self.map = np.zeros((len(V),len(V)))
        #print(self.map)
        for name in self.graph:
            val = self.graph[name];
            while(val!=None):
                self.map[self.index[name]][self.index[val.value]] = 1
                val = val.next
        
    #this is our engine. for each visible player we can see, we check if we are visible as well by that player. If yes, then we proceed otherwise we dont
    #we also use a visited array to prevent infinite looping 
    def DFS(self,name):
        self.count+=1
        self.visited[name] =True
        val = self.graph[name]
        while(val!=None):
            if(self.map[self.index[val.value]][self.index[name]] and self.visited[val.value]==False):
                self.DFS(val.value)
            val = val.next
        self.result = max(self.result,self.count);
        self.count-=1
        
    #since the game cant start from any node, we need to check for each node, whats the best result we are getting
    def countCycles(self):  
        for name in self.V:  
            #print("**RESTART**")
            #print(name)
            self.count = 0
            self.visited = dict.fromkeys(V,False)
            self.visited[name]=True
            self.DFS(name)
            self.result = max(self.result,self.count)
        return self.result; 
#-----------------------------------------------------------------------------------
# main caller
#includes the graceful existing in case of no cmd line argument or if key is repeated.
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
    g.create_index()
    g.create_map()
    #print(g.map)
    print("Maximum number of players that can touch a single ball by passing it amongst themselves are:")
    print(g.countCycles())
#-----------------------------------------------------------------------------------