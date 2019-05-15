# Owner adarsha sachan

# importing library to generate grapgh 
import matplotlib.pyplot as plt
import matplotlib.path as mpath
# generating random value
import random
from random import randint
# using time funct
import time
import datetime
import statistics
import pandas as pd

# Creating bubble_sort function 
#https://www.geeksforgeeks.org/bubble-sort/
def BubbleSort(iterable):
       # noting start timing
        sta=time.time()
        while True:
            corrected = False
            # checking each input length
            for item in range(0, len(iterable) - 1):
                # considering ascending order
                if iterable[item] > iterable[item + 1]:
                    iterable[item], iterable[item + 1] = iterable[item + 1], iterable[item]
                    corrected = True  
            if not corrected:
                # when function finish then calcutaing timing and returning
                end=time.time()
                totaltime=(end-sta)
                return totaltime

# Creating selectionSort function 
#https://www.geeksforgeeks.org/selection-sort/
def selectionSort(iterable):
    # noting start timing
    sta=time.time()
    #checking each input length
    for i in range(len(iterable)):
      # Find the rest elemint
       minPos = i
       for j in range(i+1, len(iterable)):
           if iterable[minPos] > iterable[j]:
               minPos = j            
       # Swap the found minimum element with minPos      
       temp = iterable[i]
       iterable[i] = iterable[minPos]
       iterable[minPos] = temp
       # when function finish then calcutaing timing and returning
       end=time.time()
       totaltime=(end-sta)
    return totaltime

# Creating mergeSort function 
#https://www.youtube.com/watch?v=JSceec-wEyw

def MergeSort(iterable):
    # noting start timing
    sta=time.time()
    if len(iterable)>1:
        # deviding in 3 parts index mid,left,right
        mid = len(iterable)//2
        lefthalf = iterable[:mid]
        righthalf = iterable[mid:]

        MergeSort(lefthalf)
        MergeSort(righthalf)

        i=0
        j=0
        k=0
        # while left and right 
        while i < len(lefthalf) and j < len(righthalf):
            #first half
            if lefthalf[i] < righthalf[j]:
                iterable[k]=lefthalf[i]
                i=i+1
            else:
                iterable[k]=righthalf[j]
                j=j+1
            k=k+1
        #second half
        while i < len(lefthalf):
            iterable[k]=lefthalf[i]
            i=i+1
            k=k+1
        #Merge the two halves sorted
        while j < len(righthalf):
            iterable[k]=righthalf[j]
            j=j+1
            k=k+1
            ## when function finish then calcutaing timing and returning
        end=time.time()
        totaltime=(end-sta)
        return totaltime


##===========================##
# Creating insertionSort function 
#https://www.geeksforgeeks.org/insertion-sort/
def InsertionSort(iterable):

    sta=time.time()
    #print(sta)
  # check  1 to len(iterable)
    for index in range(1,len(iterable)):
        # index for current value
        value = iterable[index]
        position = index
       # change position  of ariterabler which is greater than iterable position ahead to current   
        while position>0 and iterable[position-1]>value:
            iterable[position]=iterable[position-1]
            position = position-1
            # when function finish then calcutaing timing and returning
            end=time.time()
            totaltime=(end-sta)
    return totaltime

# Creating radix_sort function 
#http://www.geekviewpoint.com/python/sorting/radixsort
#https://www.sanfoundry.com/python-program-implement-radix-sort/
def RadixSort(nums, base=10):
    # noting start timing
    sta=time.time()
    # Isolate the base  from number
    result_list = []
    power = 0
    while nums:
        bins = [[] for _ in range(base)]
        for x in nums:
            #Drop number in right bucket
            bins[x // base**power % base].append(x)
        nums = []
        for bin in bins:
            for x in bin:
                if x < base**(power+1):
                    #append number in bucket
                    result_list.append(x)
                else:
                    nums.append(x)
        power += 1
        end=time.time()
        totaltime=(end-sta)
        #print(result_list)
    return totaltime
####################



#############
def main():
    # number of trial 

    Trail= [1000, 1500,2000,2500,3500,4000,4500,5000,6000,7000,10000]
    # No of code run 
    NumOfRun=10


    # program start 
    PrgStart=datetime.datetime.now()

    print("Program start",PrgStart.strftime("%I:%M:%S %p"))
    #for each shoting function generating a rendom number between 1 t0 100000 in the array of Trail _
    #then same array running as NumOfRun (10)then calculating a mean time

    bubbletime=[]
    bubbletime =[ round(statistics.mean([(BubbleSort(random.sample(range(100000), num))) for j in range(1,NumOfRun)]),3) for num in Trail  ]
    selectionSort_time=[]
    selectionSort_time =[ round(statistics.mean([(selectionSort(random.sample(range(100000), num))) for j in range(1,NumOfRun)]),3) for num in Trail]
    mergeSort_time=[]
    mergeSort_time =[round(statistics.mean([(MergeSort(random.sample(range(100000), num))) for j in range(1,NumOfRun)]),3) for num in Trail]
    insertionSort_time=[]
    insertionSort_time =[round(statistics.mean([(InsertionSort(random.sample(range(100000), num))) for j in range(1,NumOfRun)]),3) for num in Trail]
    radix_sort_time=[]
    radix_sort_time =[round(statistics.mean([(RadixSort(random.sample(range(100000), num))) for j in range(1,NumOfRun)]),3) for num in Trail]



    # print each shoring time and trial
    print("Bubble Sort timing is ",bubbletime,"for trial ",Trail)
    print("selection Sort timing is ",selectionSort_time,"for trial",Trail)
    print("Radix Sort timing is ",radix_sort_time,"for trial",Trail)
    print("Insertion Sort timing is ",insertionSort_time,"for trial",Trail)
    print("Merge Sort timing is ",mergeSort_time,"for trial",Trail)
    # creating all in one plot 
    plt.plot(Trail,bubbletime,color='red', marker='.', linestyle='-.', linewidth=2, markersize=12,label='Bubble_sort')
    plt.plot(Trail,selectionSort_time, marker='.', linestyle='-.', linewidth=2, markersize=12,label='Selection_Sort')
    plt.plot(Trail,radix_sort_time, marker='*', linestyle='-.', linewidth=2, markersize=8,label='Radix_Sort')
    plt.plot(Trail,insertionSort_time, marker='.', linestyle='-.', linewidth=2, markersize=12,label='Insertion_Sort')
    plt.plot(Trail,mergeSort_time, marker='.', linestyle='-.', linewidth=2, markersize=8,label='Merge_Sort')
    plt.legend()
    plt.xlabel('No of Input')
    plt.ylabel('Running time (milliseconds)')
    # prog finish
    Prgend=datetime.datetime.now()
    print("Program end",Prgend.strftime("%I:%M:%S %p"))
    plt.show()
    # using panda creating a list of data
    data = [[Trail],[radix_sort_time],[insertionSort_time],[selectionSort_time],[mergeSort_time],[bubbletime]]
    index=['Trail','RadixSort','InsertionSort','SelectionSort','MergeSort','BubbleSort']
    # creating dataframe
    df = pd.DataFrame(data,index=index)
    #print(df.to_html)
    print(df)

# calling first main function    
if __name__ == '__main__':
    main()