import random
"""Here is a self check that really covers everything so far. You may have heard of the infinite
monkey theorem? The theorem states that a monkey hitting keys at random on a typewriter
keyboard for an infinite amount of time will almost surely type a given text, such as the complete works
of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long do you 
think it would take for a Python function to generate just one sentence
of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”
You are not going to want to run this one in the browser, so fire up your favorite Python IDE. The
way we will simulate this is to write a function that generates a string that is 27 characters long
by choosing random letters from the 26 letters in the alphabet plus the space. We will write
another function that will score each generated string by comparing the randomly generated
string to the goal.
A third function will repeatedly call generate and score, then if 100% of the letters are correct
we are done. If the letters are not correct then we will generate a whole new string. To make
it easier to follow your program’s progress this third function should print out the best string
generated so far and its score every 1000 tries."""
import time

start = time.time()
print("start of the program")
b = 'methinks it is like a weasel'
seq = 'abcdefghijklmnopqrstuvwxyz '
qu = float(input("Type in the % of correctly identified sequence you want to have. Keep in mind , that higher the %, higher the time, needed to find it(on average).\n"))
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
