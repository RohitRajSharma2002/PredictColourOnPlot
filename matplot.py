

from matplotlib import pyplot as plt
import random

def createPlot():
    global co
    co = [] 

    for i in range(1,20):
        newCo = (random.randint(1,10), random.randint(1,25))
        co.append(newCo)

    for point in co:
        if point[1] < 15:
            plt.scatter(point[0], point[1], c= 'green')
        elif point[1] > 15:
            plt.scatter(point[0], point[1], c= 'red')
        else:
            plt.scatter(point[0], point[1], c= 'black')

def predictColour(x,y):
    newPoint = (x,y)
    distA = []
    distB = []
    for i in co:
        dist = (((i[0]-newPoint[0])*(i[0]-newPoint[0])) + ((i[1]-newPoint[1])*(i[1]-newPoint[1])))**(0.5)
        if i[1] >=15:
            distB.append(dist)
        else:
            distA.append(dist)
    print(distA, distB)
    if min(distA) < min(distB):
        return 'green'
    elif min(distA) > min(distB):
        return 'red'

def addPoint(x,y):
    plt.scatter(x,y, c = predictColour(x,y))
    print('point added')
    plt.annotate('your point', (x,y))
    plt.show()

createPlot()
yourPoint = input('Enter your point')
pointTup = yourPoint.split(',')
addPoint(int(pointTup[0]),int(pointTup[1])) 


    
