from functions import func
import sys
xmin = 0
xmax = 0
ymin = 0
ymax = 0

def readfile():
    global xmin,xmax,ymin,ymax
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
    for x in range(xmin,xmax+1):
        for y in range(ymin,ymax+1):
            if func(x,y) < min:
                min = func(x,y)
            count = count + 1;
    return min,count

def HillClimbing(starpoint,stepsize):
    current = starpoint
    count = 0
    while True:
        neighbor = neighbor_min(current,stepsize)
        count = count + 5
        if getfunc(neighbor) >= getfunc(current):
            break
        else :
            current = neighbor
    return getfunc(current),count
def neighbor_min(current,stepsize):
    (x,y) = current
    B = [(x,y+stepsize),(x,y-stepsize),(x-stepsize,y),(x+stepsize,y)]
    min = getfunc(B[0])
    neighbor = B[0]
    for i in B:
        if getfunc(i) < min:
            min = getfunc(i)
            neighbor = i
    return neighbor

def getfunc(point):
    global xmin,xmax,ymin,ymax
    val = func(point[0],point[1])
    if point[0] > xmax or point[1] > ymax or point[0] < xmin or point[1] < ymin:
        return 1000000.0
    else:
        return val

def main():
    xmin,xmax,ymin,ymax,A,outputfile = readfile()
    min, count = BruteForce(xmin,xmax,ymin,ymax)
    # print('%.3f\n'%min,count)
    outputfile.write('%.3f\n'%min)
    for point in A:
        min, count = HillClimbing(point,1)
        outputfile.write('%.3f\n'%min)
        #outputfile.write('%.3f %d\n'% (min,count))
        #print('%.3f\n'%min,count)
    outputfile.close()

if __name__ == '__main__':
    main()