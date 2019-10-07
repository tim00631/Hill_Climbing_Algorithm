from functions import func
import sys
def readfile():
    file_in = sys.argv[1]
    file_out = sys.argv[2]
    inputfile = open(file_in,"r")
    outputfile = open(file_out,"w")
    line1 = inputfile.readline()
    (xmin,xmax) = line1.split('\n')[0].split(',')
    (xmin,xmax) = (int(xmin),int(xmax))
    line2 = inputfile.readline()
    (ymin,ymax) = line2.split('\n')[0].split(',')
    (ymin,ymax) = (int(ymin),int(ymax))
    n = int(inputfile.readline())
    A = []
    for i in range(n):
        (x,y) = inputfile.readline().split('\n')[0].split(',')
        (x,y) = (int(x),int(y))
        A.append((x,y))
    return xmin,xmax,ymin,ymax,A,outputfile
def BruteForce(xmin,xmax,ymin,ymax):
    min = 1000000.0
    count = 0
    for x in range(xmin,xmax):
        for y in range(ymin,ymax):
            if func(x,y) < min:
                min = func(x,y)
            count = count + 1;
    return min,count

def HillClimbing(starpoint):
    current = starpoint
    count = 0
    while True:
        count = count + 1
        neighbor = neighbor_min(current)
        if getfunc(neighbor) >= getfunc(current):
            break
        else :
            current = neighbor
    return getfunc(current),count
def neighbor_min(current):
    (x,y) = current
    B = [(x,y+1),(x,y-1),(x-1,y),(x+1,y)]
    min = getfunc(B[0])
    neighbor = B[0]
    for i in B:
        if getfunc(i) < min:
            min = getfunc(i)
            neighbor = i
    return neighbor

def getfunc(point):
    return func(point[0], point[1])

def main():
    xmin,xmax,ymin,ymax,A,outputfile = readfile()
    min, count = BruteForce(xmin,xmax,ymin,ymax)
    outputfile.write('%.3f\n'%min)
    for point in A:
        min, count = HillClimbing(point)
        outputfile.write('%.3f\n'%min)
    outputfile.close()
if __name__ == '__main__':
    main()