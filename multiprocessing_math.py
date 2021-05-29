from multiprocessing import Process, Queue
import random 

def cube(x):
    '''Find cube of a number'''
    for x in nos:
        print("{} cube is {}".format(x, x**3))

def evenno(x):
    '''Finding the even numbers'''
    for x in nos:
        if x % 2 == 0:
            print('{} is an even number '.format(x))

if __name__=="__main__":
    numbers = [3, 4, 5, 6, 7, 8]
    process1 = Process(target=cube, args=('x',))
    process2 = Process(target=evenno, args=('x',))
    process1.start()
    process2.start()
    process1.join()
process2.join()
print ("Done")
    