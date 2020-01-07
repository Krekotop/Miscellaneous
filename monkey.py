import random
import time
#This program will compute how much time on average it is going to take for random guesser(monkey) to get certain % right
#for the given sentence(in this case, the sentence is "methinks it is like a weasel")
start = time.time()
print("start of the program")
b = 'methinks it is like a weasel'
seq = 'abcdefghijklmnopqrstuvwxyz ' #alphabet plus space
qu = float(input("Type in the % of correctly identified sequence you want to see. Keep in mind , that higher the %,\n
                 higher the time it takes to find it(on average).\n"))
def score(a,b):
    global k
    k = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            k += 1
    return (k*100/28)
def generate_string(seq):
    c = 't'
    for i in range(27):
        c = random.choice(seq) + c
    return c[0:26]
def check():
    j = 0
    t = 0
    p = 0
    while t < qu:
        l = generate_string(seq)
        t = score(l,b)
        j+=1
        if t > p:
            p = t
            print(p)
    print("Our score is: ", t)
    print("Our sequence for that score is: ", l)
    print("Number of iterations",j)
check()
end = time.time()
print("It took ",end - start,"seconds")
