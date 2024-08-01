#Project 22: Names Scores
import sys

letterScores = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,
                'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

def getScore(name, index):
    name = name.lower()
    score = 0
    for c in name:
        score += letterScores[c]
    return score*index

t = int(input().strip())
names = [input() for i in range(t)]
names.sort()

q = int(input().strip())
for i in range(q):
    n = input()
    if n in names:
        pos = names.index(n) + 1
        print(getScore(n, pos))
