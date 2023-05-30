"""
Author: Brenden Johnson
Assignment: Lab 6
Due Date: 3-15-2023
Class: 2520.01
"""
import random


# Task 1
def task1():
    sentence = input("Enter a sentence: ")  # Subtask 1
    print("You entered: ", sentence)
    seq = sentence.split()  # Subtask 2
    print("List: ", seq)
    newseq = '#'.join(seq)  # Subtask 3
    print("Concatenated:", newseq)


task1()
'''
Output

Test 1

Enter a sentence: Good morning CS2520
You entered:  Good morning CS2520
List:  ['Good', 'morning', 'CS2520']
Concatenated: Good#morning#CS2520

Test 2

Enter a sentence: I love chocolate but also love chocolate cookies
You entered:  I love chocolate but also love chocolate cookies
List:  ['I', 'love', 'chocolate', 'but', 'also', 'love', 'chocolate', 'cookies']
Concatenated: I#love#chocolate#but#also#love#chocolate#cookies
'''


# Task 2
def task2():
    # Subtask 1
    inpt = ''
    list1 = []
    while inpt != '#':
        inpt = input("Please enter integer list element (enter # to end): ")
        if inpt != '#':
            list1.append(int(inpt))
    print("Input List 1: ", list1)

    # SubTask 2
    list2 = [random.randint(0, 50) for i in range(20)]
    print("Random List 2: ", list2)

    # Subtask 3
    lastEl = list1[len(list1)-1]
    print("Last Element of list 1: ", lastEl)
    list1.reverse()
    print("Reverse of list 1", list1)

    # Subtask 4
    listcombination = list1 + list2
    listcombination.sort()
    listcombination.reverse()
    print("Combination of list 1 and 2 in descending order:\n", listcombination)


task2()
'''
Output

Test 1

Please enter integer list element (enter # to end): 5
Please enter integer list element (enter # to end): 2
Please enter integer list element (enter # to end): 21
Please enter integer list element (enter # to end): 23
Please enter integer list element (enter # to end): 13
Please enter integer list element (enter # to end): 17
Please enter integer list element (enter # to end): 8
Please enter integer list element (enter # to end): 1
Please enter integer list element (enter # to end): 12
Please enter integer list element (enter # to end): 45
Please enter integer list element (enter # to end): #
Input List 1:  [5, 2, 21, 23, 13, 17, 8, 1, 12, 45]
Random List 2:  [15, 2, 15, 28, 10, 20, 48, 37, 34, 36, 2, 48, 24, 45, 13, 49, 1, 6, 27, 40]
Last Element of list 1:  45
Reverse of list 1 [45, 12, 1, 8, 17, 13, 23, 21, 2, 5]
Combination of list 1 and 2 in descending order:
 [49, 48, 48, 45, 45, 40, 37, 36, 34, 28, 27, 24, 23, 21, 20, 17, 15, 15, 13, 13, 12, 10, 8, 6, 5, 2, 2, 2, 1, 1]
 

Test 2

Please enter integer list element (enter # to end): 8
Please enter integer list element (enter # to end): 6
Please enter integer list element (enter # to end): 7
Please enter integer list element (enter # to end): 5
Please enter integer list element (enter # to end): 3
Please enter integer list element (enter # to end): 0
Please enter integer list element (enter # to end): 9
Please enter integer list element (enter # to end): 369
Please enter integer list element (enter # to end): #
Input List 1:  [8, 6, 7, 5, 3, 0, 9, 369]
Random List 2:  [32, 48, 7, 28, 20, 26, 31, 8, 38, 0, 40, 10, 35, 7, 16, 4, 17, 0, 45, 7]
Last Element of list 1:  369
Reverse of list 1 [369, 9, 0, 3, 5, 7, 6, 8]
Combination of list 1 and 2 in descending order:
 [369, 48, 45, 40, 38, 35, 32, 31, 28, 26, 20, 17, 16, 10, 9, 8, 8, 7, 7, 7, 7, 6, 5, 4, 3, 0, 0, 0]
'''


# Task 3
def task3():
    # Subtask 1
    names = ("Winny", "Ada", "Lev", "Kay", "Jack", "Sam", "Mark")
    ages = [20, 18, 22, 16, 20, 18, 18]
    # names = ("John", "Adalna", "Levine", "Kaybob", "Jacker", "Sammy", "Markus")
    # ages = [42, 60, 12, 91, 20, 20, 116]
    tupoftups = tuple(zip(names, ages))
    print("Tuple of Tuples\n",tupoftups)

    # Subtask 2
    youngest = sorted(tupoftups, key=lambda x: (x[1]))[0][0]
    print("Youngest Person is:", youngest)
    averageAge = sum(ages)/len(ages)
    print("Average Age: %.2f" % averageAge)

    # Subtask 3
    alphlist = sorted(tupoftups, key=lambda x: (x[0][0]))
    desclist = tuple(sorted(alphlist, key=lambda x: (x[1]), reverse=True))
    print("Sorted tuple\n", desclist)


task3()
'''
Output

Test 1

Tuple of Tuples
 (('Winny', 20), ('Ada', 18), ('Lev', 22), ('Kay', 16), ('Jack', 20), ('Sam', 18), ('Mark', 18))
Youngest Person is: Kay
Average Age: 18.86
Sorted tuple
 (('Lev', 22), ('Jack', 20), ('Winny', 20), ('Ada', 18), ('Mark', 18), ('Sam', 18), ('Kay', 16))


Test 2

Tuple of Tuples
 (('John', 42), ('Adalna', 60), ('Levine', 12), ('Kaybob', 91), ('Jacker', 20), ('Sammy', 20), ('Markus', 116))
Youngest Person is: Levine
Average Age: 51.57
Sorted tuple
 (('Markus', 116), ('Kaybob', 91), ('Adalna', 60), ('John', 42), ('Jacker', 20), ('Sammy', 20), ('Levine', 12))

'''
