#Program/Source Code
#Here is source code of the Python Program to count the number of words in a text file. The program output is also shown below.

fname = input("Enter file name: ")
 
num_words = 0
 
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)