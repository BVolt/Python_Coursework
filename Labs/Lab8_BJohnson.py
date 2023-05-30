"""
Author: Brenden Johnson
Assignment: Lab 8
Due: 4-9-2023
Course: 2520.01
"""
import random


# Q1
def question1():
    # Part 1
    infile = open("input.txt", "r")
    lines = infile.readlines()
    print(lines[0])
    print(lines[2])
    infile.close()

    # Part 2
    infile = open("input.txt", "r")
    lines = []
    for line in infile:
        lines.append(line)
    print(lines[1])
    print(lines[3])
    infile.close()


question1()

'''
Output

We can't touch

We hunker down

But we still reach out

But we still rise up
'''


def question2():
    fp = open('data1.txt', 'w')
    fp.write("hello\t")
    fp.write("how are you")
    fp.write("\n")
    fp.write("thank you")
    fp.write("bye\n")
    fp.close()

    fp = open('data2.txt', 'w')
    fp.writelines(["hello\t", "how are you\n", "\n", "thank you", "bye\n"])
    fp.close()

    # display first file
    fp = open('data1.txt', 'r')
    print("Contents of data1.txt")
    for line in fp:
        ln = line.rstrip()
        print(ln)
    fp.close()

    # display second file
    fp = open('data2.txt', 'r')
    print("\nContents of data2.txt")
    for line in fp:
        ln = line.rstrip()
        print(ln)
    fp.close()


question2()


'''
Output
Contents of data1.txt
hello	how are you
thank youbye

Contents of data2.txt
hello	how are you

thank youbye
'''


# Q3
def question3():
    outfile = open("text.txt", "w")
    outfile.write("102\n20.5\n20.5.6\n#25\n30.2\n")
    for i in range(0, 16):
        outfile.write(str(random.randint(0, 30))+"\n")
    outfile.close()
    while True:
        try:
            filename = input("Please enter filename: ")
            infile = open(filename, "r")
            break
        except FileNotFoundError:
            print("File not found.")
    outputlist = []
    for num in infile:
        number = num.rstrip()
        try:
            outputlist.append(float(number))
        except ValueError:
            outputlist.append(0.0)
    print("The file lines as floats:")
    print(outputlist)


question3()

'''
Output


Please enter filename: gg.txt
File not found.
Please enter filename: text.txt
The file lines as floats:
[102.0, 20.5, 0.0, 0.0, 30.2, 30.0, 15.0, 18.0, 21.0, 18.0, 18.0, 25.0, 9.0, 10.0, 22.0, 26.0, 18.0, 13.0, 23.0, 8.0, 12.0]
'''