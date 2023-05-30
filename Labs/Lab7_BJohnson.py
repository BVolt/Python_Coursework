"""
Author: Brenden Johnson
Assignment: Lab 7
Due Date: 3-27-2023
Course: 2520.01
"""
import random


# Task 1
def Task1():
    paragraph = "python is an easy language python is easy to learn and easy to code a lot of python modules that are easy to use go python"
    # paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem id ex ipsum. Sed Lorem mi et imperdiet tristique. id id molestie nibh. id commodo leo sit amet ex elementum, eget iaculis quam porttitor. Cras commodo placerat lacus, et efficitur ante. Fusce scelerisque tristique arcu eget posuere. Sed vestibulum viverra arcu."
    # paragraph = "During these investigations, a kaleidoscopic mixture of postulates from physics and mathematics has been introduced and used as heuristical tools; as a consequence it is not easy to see through and characterize the theory from a formal mathematical point of view, that is, only based upon these papers. The primary objective of the present paper is to close this gap. "
    listowords = paragraph.split()
    d = {i:listowords.count(i) for i in set(listowords)}
    top3 = sorted([i for i in d.values()], reverse= True)[:3]
    dtop3 = {}
    for item in d.items():
        print(item)
        if item[1] in top3 and len(dtop3) != 3:
            dtop3[item[0]] = item[1]
            top3.remove(item[1])
    print("\nHere are the top 3 values\n",dtop3)

Task1()

'''
Output

Test 1
('of', 1)
('language', 1)
('that', 1)
('is', 2)
('use', 1)
('easy', 4)
('a', 1)
('lot', 1)
('to', 3)
('are', 1)
('code', 1)
('go', 1)
('an', 1)
('modules', 1)
('python', 4)
('and', 1)
('learn', 1)

Here are the top 3 values
 {'easy': 4, 'to': 3, 'python': 4}
 

Test 2

('adipiscing', 1)
('dolor', 1)
('Fusce', 1)
('tristique.', 1)
('iaculis', 1)
('quam', 1)
('efficitur', 1)
('tristique', 1)
('imperdiet', 1)
('posuere.', 1)
('molestie', 1)
('ipsum.', 1)
('et', 2)
('lacus,', 1)
('Sed', 2)
('ex', 2)
('eget', 2)
('vestibulum', 1)
('commodo', 2)
('Cras', 1)
('amet,', 1)
('sit', 2)
('arcu', 1)
('ipsum', 1)
('consectetur', 1)
('ante.', 1)
('placerat', 1)
('elit.', 1)
('mi', 1)
('leo', 1)
('nibh.', 1)
('Lorem', 3)
('viverra', 1)
('amet', 1)
('scelerisque', 1)
('porttitor.', 1)
('elementum,', 1)
('id', 4)
('arcu.', 1)

Here are the top 3 values
 {'et': 2, 'Lorem': 3, 'id': 4}


Test 3

('formal', 1)
('from', 2)
('upon', 1)
('gap.', 1)
('used', 1)
('kaleidoscopic', 1)
('mathematics', 1)
('During', 1)
('tools;', 1)
('the', 2)
('present', 1)
('characterize', 1)
('point', 1)
('only', 1)
('consequence', 1)
('The', 1)
('these', 2)
('of', 3)
('easy', 1)
('to', 2)
('see', 1)
('been', 1)
('is,', 1)
('objective', 1)
('this', 1)
('and', 3)
('primary', 1)
('mixture', 1)
('introduced', 1)
('has', 1)
('through', 1)
('mathematical', 1)
('papers.', 1)
('is', 2)
('as', 2)
('a', 3)
('heuristical', 1)
('based', 1)
('that', 1)
('close', 1)
('physics', 1)
('investigations,', 1)
('not', 1)
('theory', 1)
('view,', 1)
('it', 1)
('postulates', 1)
('paper', 1)

Here are the top 3 values
 {'of': 3, 'and': 3, 'a': 3}

'''

# Task 2
def task2():
    l1 = [random.randint(1, 100) for i in range(100)]
    l2 = [i for i in range(1, 100) if i % 3 == 0 or i % 4 == 0 ]
    s1 = set(l1)
    s2 = frozenset(l2)
    r1 = s1 | s2
    print("R1 has", len(r1), "elements")
    r2 = s1 & s2
    print("R2 has", len(r2), "elements")
    r3 = s1 - s2
    print("R3 has", len(r3), "elements")


task2()

'''
Output

R1 has 77 elements
R2 has 35 elements
R3 has 28 elements
'''