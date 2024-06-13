import random
global goal
answer = ""
goal = input("Please write your goal: ")
goal = goal.lower()

def fitness(test):
    score = 0
    for i in range(len(goal)):
        if (ord(test[i]) != ord(goal[i])):
            score += 1
    
    return score
def startPopulation():
    person = ""
    for i in range(len(goal)):
        person += str(chr(random.randint(97,122)))
    return person
def evolute(test):
    numberofgen = random.randint(0, len(goal)-1)
    evolutechar = chr(random.randint(97,122))
    helper = list(test)
    helper[numberofgen] = evolutechar
    test = "".join(helper)
    return test
def child(father, mother):
    child = ""

    for i in range(len(goal)):
        a = random.randint(0,1)
        if a == 0:
            child += (father[i])
        else:
            child += (mother[i])
    return child
def create_first_pop(num):
    l = []
    for i in range(num):
        l.append(startPopulation())
    return l
initial_pop = create_first_pop(60) #initial population
father = ""
mother = ""
text =""
while (text != goal):
    #initial_pop = sorter(initial_pop)
    initial_pop.sort(key=fitness)
    father = initial_pop[0]
    mother =initial_pop[1]
    text = child(father, mother)
    text = evolute(text)
    if fitness(text) < fitness(mother) or fitness(text) < fitness(father):
        initial_pop.append(text)
    print(text)
