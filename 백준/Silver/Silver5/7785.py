import sys
input=sys.stdin.readline

people=set()
for i in range(int(input())):
    name, order=map(str, input().split())
    if order=='enter':
        people.add(name)
    elif order=='leave':
        if name in people:
            people.discard(name)

people=list(people)
people.sort(reverse=True)
for i in people:
    print(i)
