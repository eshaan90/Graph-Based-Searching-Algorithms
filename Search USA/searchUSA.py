# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import numpy as np
import math



class Node(object):
    """
    This class intializes the nodes for the map of US.
    
    """
    def __init__(self,name):
        self.name=name
    
    def getname(self):
        return self.name
    
    def __str__(self):
        return self.name
    



class Edge_weighted(object):
    
    """
    This class initializes weighted edges for the map of US.
    """
    def __init__(self, src, dest, weight = 0.0):

        self.source = src
        self.destination = dest
        self.weight = weight
    
    def getsource(self):
        return self.source
    
    def getdestination(self):
        return self.destination
    
    def getweight(self): 
        return self.weight

    def __str__(self):
        return self.source.getname() + '->(' + str(self.weight) + ')'+ self.destination.getname()




class Digraph(object):
    """
    This class forms the edges between the nodes.
    """
    
    
    def __init__(self):
        self.nodes=[]
        self.edges={}
        self.coordinates={}
        self.weights={}
        
    def addNode(self,node):
        
        if node in self.nodes:
            raise ValueError('Duplicate Node')
        else:
            self.nodes.append(node)
            self.edges[node]=[]
        
    def addEdge(self,edge):
        source=edge.getsource()
        dest=edge.getdestination()
        weight=edge.getweight()
        
        if not(source in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        
        self.edges[source].append(dest)
        if (source,dest) not in self.weights:
            self.weights[(source,dest)]=weight
            self.weights[(dest,source)]=weight
    
    
    def addCoordinates(self,node,lat,long):
        if node in self.coordinates:
            raise ValueError('Duplicate Node')
        else:
            self.coordinates[node]=[lat,long]
        
        
    def children(self,node):
        return self.edges[node]
    
    def hasNode(self,node):
        return node in self.nodes
    
    
    def getedgeweight(self,src,dest):
        return self.weights[(src,dest)]
    
    
    def getLatitude(self,node):
        if not(node in self.coordinates):
            raise ValueError('Node not in graph')
        else:
            return self.coordinates[node][0]
    
    
    def getLongitude(self,node):
        if not(node in self.coordinates):
            raise ValueError('Node not in graph')
        else:
            return self.coordinates[node][1]
        
        
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
        rev=Edge_weighted(edge.getdestination(),edge.getsource())
        Digraph.addEdge(self,rev)
        
  

      
def addheuristic(g,city1,city2):
    """
    This function calculates the heuristic value between two cities.
    """
    Lat1=g.getLatitude(city1)
    Lat2=g.getLatitude(city2)
    Long1=g.getLongitude(city1)
    Long2=g.getLongitude(city2)
    
    Lat1=Lat1.astype(np.float)
    Lat2=Lat2.astype(np.float)
    Long1=Long1.astype(np.float)
    Long2=Long2.astype(np.float)
        
    value=math.sqrt(math.pow(69.5*(Lat1-Lat2), 2)+math.pow(69.5*(Long1-Long2)*math.cos(((Lat1+Lat2)/360)*math.pi), 2))
        
    return value



  
def buildUSgraph(Graph):
    """
    This function builds nodes and edges for the map of US.
    
    """
    
    g=Graph()

    cities=np.array([['albanyGA',31.58,84.17],['albanyNY',42.66,73.78],['albuquerque',35.11,106.61],['atlanta',33.76,84.40],
                   ['augusta',33.43,82.02],['austin',30.30,97.75],['bakersfield',35.36,119.03],['baltimore',39.31,76.62],
                   ['batonRouge',30.46,91.14],['beaumont',30.08,94.13],['boise',43.61,116.24],['boston',42.32,71.09],
                   ['buffalo',42.90,78.85],['calgary',51.00,114.00],['charlotte',35.21,80.83],['chattanooga',35.05,85.27],
                   ['chicago',41.84,87.68],['cincinnati',39.14,84.50],['cleveland',41.48,81.67],['coloradoSprings', 38.86, 104.79],
                   ['columbus',39.99,82.99],['dallas',32.80,96.79],['dayton',39.76,84.20],['daytonaBeach',29.21,81.04],
                   ['denver',39.73,104.97],['desMoines',41.59,93.62],['elPaso',31.79,106.42],['eugene',44.06,123.11],
                   ['europe',48.87,-2.33],['ftWorth',32.74,97.33],['fresno',36.78,119.79],['grandJunction',39.08,108.56],
                   ['greenBay',44.51,88.02],['greensboro',36.08,79.82],['houston',29.76,95.38],['indianapolis',39.79,86.15],
                   ['jacksonville',30.32,81.66],['japan',35.68,220.23],['kansasCity',39.08,94.56],['keyWest',24.56,81.78],
                   ['lafayette',30.21,92.03],['lakeCity',30.19,82.64],['laredo',27.52,99.49],['lasVegas',36.19,115.22],
                   ['lincoln',40.81,96.68],['littleRock',34.74,92.33],['losAngeles',34.03,118.17],['macon',32.83,83.65],
                   ['medford',42.33,122.86],['memphis',35.12,89.97],['mexia',31.68,96.48],['mexico',19.40,99.12],
                   ['miami',25.79,80.22],['midland',43.62,84.23],['milwaukee',43.05,87.96],['minneapolis',44.96,93.27],
                   ['modesto',37.66,120.99],['montreal',45.50,73.67],['nashville',36.15,86.76],['newHaven',41.31,72.92],
                   ['newOrleans',29.97,90.06],['newYork',40.70,73.92],['norfolk',36.89,76.26],['oakland',37.80,122.23],
                   ['oklahomaCity',35.48,97.53],['omaha',41.26,96.01],['orlando',28.53,81.38],['ottawa',45.42,75.69],
                   ['pensacola',30.44,87.21],['philadelphia',40.72,76.12],['phoenix',33.53,112.08],['pittsburgh',40.40,79.84],
                   ['pointReyes',38.07,122.81],['portland',45.52,122.64],['providence',41.80,71.36],['provo',40.24,111.66],
                   ['raleigh',35.82,78.64],['redding',40.58,122.37],['reno',39.53,119.82],['richmond',37.54,77.46],
                   ['rochester',43.17,77.61],['sacramento',38.56,121.47],['salem',44.93,123.03],['salinas',36.68,121.64],
                   ['saltLakeCity',40.75,111.89],['sanAntonio',29.45,98.51],['sanDiego',32.78,117.15],['sanFrancisco',37.76,122.44],
                   ['sanJose',37.30,121.87],['sanLuisObispo',35.27,120.66],['santaFe',35.67,105.96],['saultSteMarie',46.49,84.35],
                   ['savannah',32.05,81.10],['seattle',47.63,122.33],['stLouis',38.63,90.24],['stamford',41.07,73.54],
                   ['stockton',37.98,121.30],['tallahassee',30.45,84.27],['tampa',27.97,82.46],['thunderBay',48.38,89.25],
                   ['toledo',41.67,83.58],['toronto',43.65,79.38],['tucson',32.21,110.92],['tulsa',36.13,95.94],['uk1',51.30,0.00],
                   ['uk2',51.30,0.00],['vancouver',49.25,123.10],['washington',38.91,77.01],['westPalmBeach',26.71,80.05],
                   ['wichita',37.69,97.34],['winnipeg',49.90,97.13],['yuma',32.69,114.62]])

    for city in cities:
        g.addNode(Node(city[0]))
        g.addCoordinates(g.getNode(city[0]),city[1],city[2])
    
    
    
    g.addEdge(Edge_weighted(g.getNode('albanyNY'),g.getNode('montreal'),226))
    g.addEdge(Edge_weighted(g.getNode('albanyNY'),g.getNode('boston'),166))
    g.addEdge(Edge_weighted(g.getNode('albanyNY'),g.getNode('rochester'),148))
    g.addEdge(Edge_weighted(g.getNode('albanyGA'),g.getNode('tallahassee'),120))
    g.addEdge(Edge_weighted(g.getNode('albanyGA'),g.getNode('macon'),106))
    g.addEdge(Edge_weighted(g.getNode('albuquerque'),g.getNode('elPaso'),267))
    g.addEdge(Edge_weighted(g.getNode('albuquerque'),g.getNode('santaFe'),61))
    g.addEdge(Edge_weighted(g.getNode('atlanta'),g.getNode('macon'),82))
    g.addEdge(Edge_weighted(g.getNode('atlanta'),g.getNode('chattanooga'),117))
    g.addEdge(Edge_weighted(g.getNode('augusta'),g.getNode('charlotte'),161))
    g.addEdge(Edge_weighted(g.getNode('augusta'),g.getNode('savannah'),131))
    g.addEdge(Edge_weighted(g.getNode('austin'),g.getNode('houston'),186))
    g.addEdge(Edge_weighted(g.getNode('austin'),g.getNode('sanAntonio'),79))
    g.addEdge(Edge_weighted(g.getNode('bakersfield'),g.getNode('losAngeles'),112))
    g.addEdge(Edge_weighted(g.getNode('bakersfield'),g.getNode('fresno'),107))
    g.addEdge(Edge_weighted(g.getNode('baltimore'),g.getNode('philadelphia'),102))
    g.addEdge(Edge_weighted(g.getNode('baltimore'),g.getNode('washington'),45)) 
    g.addEdge(Edge_weighted(g.getNode('batonRouge'),g.getNode('lafayette'),50))
    g.addEdge(Edge_weighted(g.getNode('batonRouge'),g.getNode('newOrleans'),80))
    g.addEdge(Edge_weighted(g.getNode('beaumont'),g.getNode('houston'),69))
    g.addEdge(Edge_weighted(g.getNode('beaumont'),g.getNode('lafayette'),122))
    g.addEdge(Edge_weighted(g.getNode('boise'),g.getNode('saltLakeCity'),349))
    g.addEdge(Edge_weighted(g.getNode('boise'),g.getNode('portland'),428))
    g.addEdge(Edge_weighted(g.getNode('boston'),g.getNode('providence'),51))
    g.addEdge(Edge_weighted(g.getNode('buffalo'),g.getNode('toronto'),105))
    g.addEdge(Edge_weighted(g.getNode('buffalo'),g.getNode('rochester'),64))
    g.addEdge(Edge_weighted(g.getNode('buffalo'),g.getNode('cleveland'),191))
    g.addEdge(Edge_weighted(g.getNode('calgary'),g.getNode('vancouver'),605))
    g.addEdge(Edge_weighted(g.getNode('calgary'),g.getNode('winnipeg'),829))
    g.addEdge(Edge_weighted(g.getNode('charlotte'),g.getNode('greensboro'),91))
    g.addEdge(Edge_weighted(g.getNode('chattanooga'),g.getNode('nashville'),129))
    g.addEdge(Edge_weighted(g.getNode('chicago'),g.getNode('milwaukee'),90))
    g.addEdge(Edge_weighted(g.getNode('chicago'),g.getNode('midland'),279))
    g.addEdge(Edge_weighted(g.getNode('cincinnati'),g.getNode('indianapolis'),110))
    g.addEdge(Edge_weighted(g.getNode('cincinnati'),g.getNode('dayton'),56))
    g.addEdge(Edge_weighted(g.getNode('cleveland'),g.getNode('pittsburgh'),157))
    g.addEdge(Edge_weighted(g.getNode('cleveland'),g.getNode('columbus'),142))
    g.addEdge(Edge_weighted(g.getNode('coloradoSprings'),g.getNode('denver'),70))
    g.addEdge(Edge_weighted(g.getNode('coloradoSprings'),g.getNode('santaFe'),316))
    g.addEdge(Edge_weighted(g.getNode('columbus'),g.getNode('dayton'),72))
    g.addEdge(Edge_weighted(g.getNode('dallas'),g.getNode('denver'),792))
    g.addEdge(Edge_weighted(g.getNode('dallas'),g.getNode('mexia'),83))
    g.addEdge(Edge_weighted(g.getNode('daytonaBeach'),g.getNode('jacksonville'),92))
    g.addEdge(Edge_weighted(g.getNode('daytonaBeach'),g.getNode('orlando'),52))
    g.addEdge(Edge_weighted(g.getNode('denver'),g.getNode('wichita'),523))
    g.addEdge(Edge_weighted(g.getNode('denver'),g.getNode('grandJunction'),246))
    g.addEdge(Edge_weighted(g.getNode('desMoines'),g.getNode('omaha'),135))
    g.addEdge(Edge_weighted(g.getNode('desMoines'),g.getNode('minneapolis'),246))
    g.addEdge(Edge_weighted(g.getNode('elPaso'),g.getNode('sanAntonio'),580))    
    g.addEdge(Edge_weighted(g.getNode('elPaso'),g.getNode('tucson'),320)) 
    g.addEdge(Edge_weighted(g.getNode('eugene'),g.getNode('salem'),63))
    g.addEdge(Edge_weighted(g.getNode('eugene'),g.getNode('medford'),165))
    g.addEdge(Edge_weighted(g.getNode('europe'),g.getNode('philadelphia'),3939))
    g.addEdge(Edge_weighted(g.getNode('ftWorth'),g.getNode('oklahomaCity'),209))
    g.addEdge(Edge_weighted(g.getNode('fresno'),g.getNode('modesto'),109))
    g.addEdge(Edge_weighted(g.getNode('grandJunction'),g.getNode('provo'),220))
    g.addEdge(Edge_weighted(g.getNode('greenBay'),g.getNode('minneapolis'),304))
    g.addEdge(Edge_weighted(g.getNode('greenBay'),g.getNode('milwaukee'),117))
    g.addEdge(Edge_weighted(g.getNode('greensboro'),g.getNode('raleigh'),74))
    g.addEdge(Edge_weighted(g.getNode('houston'),g.getNode('mexia'),165))
    g.addEdge(Edge_weighted(g.getNode('indianapolis'),g.getNode('stLouis'),246))
    g.addEdge(Edge_weighted(g.getNode('jacksonville'),g.getNode('savannah'),140))
    g.addEdge(Edge_weighted(g.getNode('jacksonville'),g.getNode('lakeCity'),113))
    g.addEdge(Edge_weighted(g.getNode('japan'),g.getNode('pointReyes'),5131))
    g.addEdge(Edge_weighted(g.getNode('japan'),g.getNode('sanLuisObispo'),5451))
    g.addEdge(Edge_weighted(g.getNode('kansasCity'),g.getNode('tulsa'),249))
    g.addEdge(Edge_weighted(g.getNode('kansasCity'),g.getNode('stLouis'),256))
    g.addEdge(Edge_weighted(g.getNode('kansasCity'),g.getNode('wichita'),190))
    g.addEdge(Edge_weighted(g.getNode('keyWest'),g.getNode('tampa'),446))
    g.addEdge(Edge_weighted(g.getNode('lakeCity'),g.getNode('tampa'),169))
    g.addEdge(Edge_weighted(g.getNode('lakeCity'),g.getNode('tallahassee'),104))
    g.addEdge(Edge_weighted(g.getNode('laredo'),g.getNode('sanAntonio'),154))
    g.addEdge(Edge_weighted(g.getNode('laredo'),g.getNode('mexico'),741))
    g.addEdge(Edge_weighted(g.getNode('lasVegas'),g.getNode('losAngeles'),275))
    g.addEdge(Edge_weighted(g.getNode('lasVegas'),g.getNode('saltLakeCity'),486))
    g.addEdge(Edge_weighted(g.getNode('lincoln'),g.getNode('wichita'),277))
    g.addEdge(Edge_weighted(g.getNode('lincoln'),g.getNode('omaha'),58))
    g.addEdge(Edge_weighted(g.getNode('littleRock'),g.getNode('memphis'),137))
    g.addEdge(Edge_weighted(g.getNode('littleRock'),g.getNode('tulsa'),276))
    g.addEdge(Edge_weighted(g.getNode('losAngeles'),g.getNode('sanDiego'),124))
    g.addEdge(Edge_weighted(g.getNode('losAngeles'),g.getNode('sanLuisObispo'),182))
    g.addEdge(Edge_weighted(g.getNode('medford'),g.getNode('redding'),150))
    g.addEdge(Edge_weighted(g.getNode('memphis'),g.getNode('nashville'),210)) 
    g.addEdge(Edge_weighted(g.getNode('miami'),g.getNode('westPalmBeach'),67))
    g.addEdge(Edge_weighted(g.getNode('midland'),g.getNode('toledo'),82))
    g.addEdge(Edge_weighted(g.getNode('minneapolis'),g.getNode('winnipeg'),463))
    g.addEdge(Edge_weighted(g.getNode('modesto'),g.getNode('stockton'),29))
    g.addEdge(Edge_weighted(g.getNode('montreal'),g.getNode('ottawa'),132))
    g.addEdge(Edge_weighted(g.getNode('newHaven'),g.getNode('providence'),110))
    g.addEdge(Edge_weighted(g.getNode('newHaven'),g.getNode('stamford'),92))
    g.addEdge(Edge_weighted(g.getNode('newOrleans'),g.getNode('pensacola'),268))
    g.addEdge(Edge_weighted(g.getNode('newYork'),g.getNode('philadelphia'),101))
    g.addEdge(Edge_weighted(g.getNode('norfolk'),g.getNode('richmond'),92))
    g.addEdge(Edge_weighted(g.getNode('norfolk'),g.getNode('raleigh'),174))
    g.addEdge(Edge_weighted(g.getNode('oakland'),g.getNode('sanFrancisco'),8))
    g.addEdge(Edge_weighted(g.getNode('oakland'),g.getNode('sanJose'),42))
    g.addEdge(Edge_weighted(g.getNode('oklahomaCity'),g.getNode('tulsa'),105))
    g.addEdge(Edge_weighted(g.getNode('orlando'),g.getNode('westPalmBeach'),168))
    g.addEdge(Edge_weighted(g.getNode('orlando'),g.getNode('tampa'),84))
    g.addEdge(Edge_weighted(g.getNode('ottawa'),g.getNode('toronto'),269))
    g.addEdge(Edge_weighted(g.getNode('pensacola'),g.getNode('tallahassee'),120))
    g.addEdge(Edge_weighted(g.getNode('philadelphia'),g.getNode('pittsburgh'),319))
    g.addEdge(Edge_weighted(g.getNode('philadelphia'),g.getNode('newYork'),101))
    g.addEdge(Edge_weighted(g.getNode('philadelphia'),g.getNode('uk1'),3548))
    g.addEdge(Edge_weighted(g.getNode('philadelphia'),g.getNode('uk2'),3548))
    g.addEdge(Edge_weighted(g.getNode('phoenix'),g.getNode('tucson'),117))
    g.addEdge(Edge_weighted(g.getNode('phoenix'),g.getNode('yuma'),178))
    g.addEdge(Edge_weighted(g.getNode('pointReyes'),g.getNode('redding'),215))
    g.addEdge(Edge_weighted(g.getNode('pointReyes'),g.getNode('sacramento'),115))
    g.addEdge(Edge_weighted(g.getNode('portland'),g.getNode('seattle'),174))
    g.addEdge(Edge_weighted(g.getNode('portland'),g.getNode('salem'),47))
    g.addEdge(Edge_weighted(g.getNode('reno'),g.getNode('saltLakeCity'),520))
    g.addEdge(Edge_weighted(g.getNode('reno'),g.getNode('sacramento'),133))
    g.addEdge(Edge_weighted(g.getNode('richmond'),g.getNode('washington'),105))
    g.addEdge(Edge_weighted(g.getNode('sacramento'),g.getNode('sanFrancisco'),95))   
    g.addEdge(Edge_weighted(g.getNode('sacramento'),g.getNode('stockton'),51))
    g.addEdge(Edge_weighted(g.getNode('salinas'),g.getNode('sanJose'),31))
    g.addEdge(Edge_weighted(g.getNode('salinas'),g.getNode('sanLuisObispo'),137))
    g.addEdge(Edge_weighted(g.getNode('sanDiego'),g.getNode('yuma'),172))
    g.addEdge(Edge_weighted(g.getNode('saultSteMarie'),g.getNode('thunderBay'),442))
    g.addEdge(Edge_weighted(g.getNode('saultSteMarie'),g.getNode('toronto'),436))
    g.addEdge(Edge_weighted(g.getNode('seattle'),g.getNode('vancouver'),115))
    g.addEdge(Edge_weighted(g.getNode('thunderBay'),g.getNode('winnipeg'),440))
    
    return g





def finalpath(parent,current):
    totalpath=[current]
    while current in parent.keys():
        current=parent[current]
        totalpath.append(current)        

    return totalpath




def a_star(graph,start,end,path,no_of_expanded_nodes):
    """
    A* search algorithm
    """
    
    
    openset=[]
    closedset=[]
    openset.append(start)
    parent={}
    gscore={}
    fscore={}
    for src in graph.nodes:
        gscore[src]=float('inf')
        fscore[src]=float('inf')
    gscore[start]=0
    fscore[start]=addheuristic(graph,start,end)
    
    while len(openset)>0:
       x=fscore[openset[0]]
       for i in openset:
           if fscore[i]<=x:
               x=fscore[i]
               current=i
       if current==end:
           return (finalpath(parent,current), no_of_expanded_nodes,closedset)
       
       openset.remove(current)
       closedset.append(current)
       no_of_expanded_nodes+=1
        
       for node in graph.children(current):
           if node in closedset:
                continue
           if node not in openset:
                openset.append(node)
           new_gs=gscore[current]+graph.getedgeweight(current,node)
           if new_gs>=gscore[node]:
               continue
           parent[node]=current
           gscore[node]=new_gs
           fscore[node]=new_gs+addheuristic(graph,node,end)
    return 'Fail'


def test_a_star(source,destination):
    g=buildUSgraph(Graph)
    (shortest,no_of_expandednodes,expandednodes)=a_star(g,g.getNode(source),g.getNode(destination),[],0)
    print('------------------------------')
    print('\n While traversing from',source,'to',destination)
    print('\n Using A*star search: ')
    print('\n No of Expanded Nodes=',no_of_expandednodes)
    
    names=[]
    for i in expandednodes:
        names.append(i.getname())
    print('\n Expanded nodes are: ', names)

    totalcost=0
    print('\n The shortest path contains',len(shortest),'nodes.')
    shortest.reverse()
    for i in range(len(shortest)-1):
        totalcost=totalcost+g.getedgeweight(shortest[i],shortest[i+1])
        
        
    names=[]
    for i in shortest:
        names.append(i.getname())
    print('\n The shortest path is= ',names)
    print('\n Total path cost= ',totalcost,'\n\n' )
    print('\n------------------------------')

    
    return None
    
    
test_a_star('greensboro','cincinnati')   
test_a_star('reno','desMoines')      
test_a_star('desMoines','reno')      
test_a_star('newHaven','lasVegas')      
test_a_star('lasVegas','newHaven') 
test_a_star('calgary','lincoln')
      

    



def uniform_cost_search(graph,start,end,path,no_of_expanded_nodes):
    
    openset=[]
    closedset=[]
    openset.append(start)
    parent={}
    gscore={}
    for src in graph.nodes:
        gscore[src]=float('inf')
        
    gscore[start]=0
    
    while len(openset)>0:
       x=gscore[openset[0]]
       for i in openset:
           if gscore[i]<=x:
               x=gscore[i]
               current=i
       if current==end:
           return (finalpath(parent,current),no_of_expanded_nodes,closedset) 
       
       openset.remove(current)
       closedset.append(current)
       no_of_expanded_nodes+=1
        
       for node in graph.children(current):
           if node in closedset:
               continue
           if node not in openset:
               openset.append(node)
           new_gs=gscore[current]+graph.getedgeweight(current,node)
           if new_gs>=gscore[node]:
               continue
           parent[node]=current
           gscore[node]=new_gs
    return 'Fail'



def test_uniform(source,destination):
    
    g=buildUSgraph(Graph)
    (shortest,no_of_expandednodes,expandednodes)=uniform_cost_search(g,g.getNode(source),g.getNode(destination),[],0)
    print('------------------------------')
    print('\n While traversing from',source,'to',destination)
    print('\n Using Uniform Cost search: ')
    print('\n No of Expanded Nodes=',no_of_expandednodes)
    
    names=[]
    for i in expandednodes:
        names.append(i.getname())
    print('\n Expanded nodes are: ', names)

    totalcost=0
    print('\n The shortest path contains',len(shortest),'nodes.')
    shortest.reverse()
    for i in range(len(shortest)-1):
        totalcost=totalcost+g.getedgeweight(shortest[i],shortest[i+1])
        
        
    names=[]
    for i in shortest:
        names.append(i.getname())
    print('\n The shortest path is= ',names)
    print('\n Total path cost= ',totalcost,'\n\n' )
    print('\n------------------------------')

    
#test_uniform('greensboro','cincinnati')   
#test_uniform('japan','desMoines')      
#test_uniform('desMoines','japan')      
#test_uniform('newHaven','lasVegas')      
#test_uniform('lasVegas','newHaven') 
#test_uniform('calgary','lincoln')




def greedy(graph,start,end,path,no_of_expanded_nodes):
    
    openset=[]
    closedset=[]
    openset.append(start)
    parent={}
    hscore={}
    for src in graph.nodes:
        hscore[src]=float('inf')
        
    hscore[start]=addheuristic(graph,start,end)
    
    while len(openset)>0:
       x=hscore[openset[0]]
       for i in openset:
           if hscore[i]<=x:
               x=hscore[i]
               current=i
       if current==end:
           return (finalpath(parent,current),no_of_expanded_nodes,closedset) 
       
       openset.remove(current)
       closedset.append(current)
       no_of_expanded_nodes+=1
        
       for node in graph.children(current):
           if node in closedset:
               continue
           if node not in openset:
               openset.append(node)
           parent[node]=current
           hscore[node]=addheuristic(graph,node,end)
    return 'Fail'



def test_greedy(source,destination):
    g=buildUSgraph(Graph)
    (shortest,no_of_expandednodes,expandednodes)=greedy(g,g.getNode(source),g.getNode(destination),[],0)
    print('\n------------------------------')
    print('\n While traversing from',source,'to',destination)
    print('\n Using greedy search: ')
    print('\n No of Expanded Nodes=',no_of_expandednodes)
    
    names=[]
    for i in expandednodes:
        names.append(i.getname())
    print('\n Expanded nodes are: ', names)

    totalcost=0
    print('\n The shortest path contains',len(shortest),'nodes.')
    shortest.reverse()
    for i in range(len(shortest)-1):
        totalcost=totalcost+g.getedgeweight(shortest[i],shortest[i+1])
        
        
    names=[]
    for i in shortest:
        names.append(i.getname())
    print('\n The shortest path is= ',names)
    print('\n Total path cost= ',totalcost,'\n\n' )
    print('\n------------------------------')

test_greedy('greensboro','cincinnati')   
test_greedy('reno','desMoines')      
test_greedy('desMoines','reno')      
test_greedy('newHaven','lasVegas')      
test_greedy('lasVegas','newHaven') 
test_greedy('calgary','lincoln')

    

def searchUSA(searchtype,source, destination):
    
    if str(searchtype)=='greedy':
        test_greedy(source,destination)
    elif str(searchtype)=='astar':
        test_a_star(source,destination)
    elif str(searchtype)=='uniform':
        test_uniform(source,destination)
    else:
        print('Incorrect value entered, try again')
    return None

    
        
        