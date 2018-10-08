# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Node(object):
  
    def __init__(self,name):
        self.name=name
    
    def getname(self):
        return self.name
    
    def __str__(self):
        return self.name
    

class Edge(object):
    def __init__(self,source,dest):
        self.source=source
        self.dest=dest
    
    def getsource(self):
        return self.source
    
    def getdestination(self):
        return self.dest
    
    def __str__(self):
        return self.source.getname()+'-->'+self.dest.getname()
    


class Digraph(object):
    
    def __init__(self):
        self.edges={}
        
    def addNode(self,node):
        if node in self.edges:
            raise ValueError('Duplicate Node')
        else:
            self.edges[node]=[]
        
    def addEdge(self,edge):
        source=edge.getsource()
        dest=edge.getdestination()
        if not(source in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[source].append(dest)
        
    def children(self,node):
        return self.edges[node]
    
    def hasNode(self,node):
        return node in self.edges
    
    def getNode(self,name):
        for n in self.edges:
            if n.getname()==name:
                return n
        raise NameError(name)
        
    def __str__(self):
        result=''
        for source in self.edges:
            x=''
            for dest in self.edges[source]:
                x=x+dest.getname()+', '
            result=result+source.getname()+'--> '+x[:-1]+'\n'

        return result[:-1]
    
class Graph(Digraph):
    
    def __init__(self):
        Digraph.__init__(self)
        
    def addEdge(self,edge):
        Digraph.addEdge(self,edge)
        rev=Edge(edge.getdestination(),edge.getsource())
        Digraph.addEdge(self,rev)
        
        
        
def buildRomaniagraph(Graph):
    """
    This block builds nodes and edges for the map of Romania.
    
    """
    
    g=Graph()
    for name in ('Oradea','Zerind','Arad','Timisoara', 'Lugoj','Mehadia', 
                 'Dobreta','Sibiu','Fagaras','Rimnicu Vilcea','Pitesti','Craiova',
                 'Bucharest','Giurgiu','Urziceni','Hirsova','Eforie','Vaslui',
                 'Iasi','Nearnt'):
        g.addNode(Node(name))
        
        
    g.addEdge(Edge(g.getNode('Oradea'),g.getNode('Zerind')))
    g.addEdge(Edge(g.getNode('Oradea'),g.getNode('Sibiu')))
    g.addEdge(Edge(g.getNode('Zerind'),g.getNode('Arad')))
    g.addEdge(Edge(g.getNode('Arad'),g.getNode('Timisoara')))
    g.addEdge(Edge(g.getNode('Lugoj'),g.getNode('Timisoara')))
    g.addEdge(Edge(g.getNode('Lugoj'),g.getNode('Mehadia')))
    g.addEdge(Edge(g.getNode('Mehadia'),g.getNode('Dobreta')))
    g.addEdge(Edge(g.getNode('Dobreta'),g.getNode('Craiova')))
    g.addEdge(Edge(g.getNode('Craiova'),g.getNode('Pitesti')))
    g.addEdge(Edge(g.getNode('Craiova'),g.getNode('Rimnicu Vilcea')))
    g.addEdge(Edge(g.getNode('Rimnicu Vilcea'),g.getNode('Sibiu')))
    g.addEdge(Edge(g.getNode('Sibiu'),g.getNode('Fagaras')))
    g.addEdge(Edge(g.getNode('Pitesti'),g.getNode('Bucharest')))
    g.addEdge(Edge(g.getNode('Bucharest'),g.getNode('Giurgiu')))
    g.addEdge(Edge(g.getNode('Bucharest'),g.getNode('Urziceni')))
    g.addEdge(Edge(g.getNode('Arad'),g.getNode('Sibiu')))
    g.addEdge(Edge(g.getNode('Rimnicu Vilcea'),g.getNode('Pitesti')))
    g.addEdge(Edge(g.getNode('Bucharest'),g.getNode('Fagaras')))
    g.addEdge(Edge(g.getNode('Vaslui'),g.getNode('Urziceni')))
    g.addEdge(Edge(g.getNode('Hirsova'),g.getNode('Urziceni')))
    g.addEdge(Edge(g.getNode('Hirsova'),g.getNode('Eforie')))
    g.addEdge(Edge(g.getNode('Vaslui'),g.getNode('Iasi')))
    g.addEdge(Edge(g.getNode('Iasi'),g.getNode('Nearnt')))
  
    return g



def DFS(graph,start,end,path,shortest):
    path=path+[start]
    if start==end:
        return path
    for node in graph.children(start):
        if node not in path:
            if shortest==None or len(path)<len(shortest):
                newpath=DFS(graph,node,end,path,shortest)
                if newpath!=None:
                    shortest=newpath
    return shortest


def ShortestPath(graph,start,end):
    return DFS(graph,start,end,[],None)

def test_DFS(source,destination):
    
    g=buildRomaniagraph(Graph)
    sp=ShortestPath(g,g.getNode(source),g.getNode(destination))
    x=[]
    for i in sp:
        x.append(i.getname())
    if sp!=None:        
        print('\n Shortest Path from', source, 'to', destination,'using DFS is',x)
        
    else:
        print('There is no path from', source, 'to', destination)
        
        
test_DFS('Dobreta','Fagaras')


def BFS(graph,start,end):
    initialpath=[start]
    pathqueue=[initialpath]
    while len(pathqueue)!=0:
        tmppath=pathqueue.pop(0)
        lastnode=tmppath[-1]
        if lastnode==end:
            return tmppath
        for nextnode in graph.children(lastnode):
            if nextnode not in tmppath:
                newpath=tmppath+[nextnode]
                pathqueue.append(newpath)
    return None


def test_BFS(source,destination):
    
    g=buildRomaniagraph(Graph)
    x=BFS(g,g.getNode(source),g.getNode(destination))
    y=[]
    for i in x:
        y.append(i.getname())
    if x!=None:
        print('\n Shortest Path from', source, 'to', destination,'using BFS is', y)
    else:
        print('There is no path from', source, 'to', destination)
        
        
test_BFS('Dobreta','Fagaras')
    