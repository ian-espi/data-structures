# name: Ian Espinosa
# email: IanEspinosaBiz@gmail.com
# program: benchmark.py

import random
import time
import timeit

def bubbleSort(aList): # sort list in place
    for passnum in range(len(aList) - 1, 0, -1):
        for i in range(passnum):
            if aList[i] > aList[i + 1]:
                temp = aList[i]
                aList[i] = aList[i + 1]
                aList[i + 1] = temp


def mergeSort(aList): # sort list in place
    if len(aList) > 1:
        mid = len(aList) // 2
        lefthalf = aList[:mid]
        righthalf = aList[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                aList[k] = lefthalf[i]
                i = i + 1
            else:
                aList[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            aList[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            aList[k] = righthalf[j]
            j = j + 1
            k = k + 1


def bigList(n): # creates a list of 1 to in in random order
    theList = [i+1 for i in range(n)] # 1,2,3,... n
    random.shuffle(theList) # randomly shuffle elements
    return theList


# DO NOT MODIFY defs above this line
# -------------------------------------------
# Add your code after this comment block to plot the time it takes to run
# the previous functions bubbleSort(aList), mergeSort(aList)
# on a list created by calling bigList(n) with n at different sizes in
# range(1000,10000,1000)
#
# Use timeit or the time method to time how log bubbleSort and mergeSort take to
# run on a list of n size created by calling bigList(n), make sure to call
# bigList(n) once for timing each function for every value of n
# Print the timings in a tab delimited table as shown below using
#   print( n, t1, t2, sep='\t') # where t1 is the time for merge and t2 is time for bubble
#
# Here is a example of the form your output should look like
# NOTE the <tab> just shows you that there will be tabs between each column
# Also make sure to print the headings at the top before you loop starts
# when you call timeit, set number equal to 1 !

# N  <tab>  merge  <tab>  bubble
# 1000  <tab>  0.0136160  <tab>  0.21380919
# 2000  <tab>  0.0329329  <tab>  0.81959286
# 3000  <tab>  0.0413493  <tab>  1.83145118
# 4000  <tab>  0.0569270  <tab>  3.32819083
# 5000  <tab>  0.0708057  <tab>  5.15382035
# 6000  <tab>  0.0868657  <tab>  7.44444825
# 7000  <tab>  0.1045654  <tab>  10.2676698
# 8000  <tab>  0.1207415  <tab>  13.6543210
# 9000  <tab>  0.2433110  <tab>  17.4238122


print("N", "    merge", "    bubble", sep="\t")
for n in range(1000, 10000, 1000):
    aList = bigList(n)

    t1 = timeit.Timer("bubbleSort(aList)", "from __main__ import bubbleSort, aList")
    t2 = timeit.Timer("mergeSort(aList)", "from __main__ import mergeSort, aList")

    print("%d\t%.6f\t%.6f" % (n, t2.timeit(number=1), t1.timeit(number=1)))