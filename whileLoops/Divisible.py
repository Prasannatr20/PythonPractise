i = 0
div3=0
div5=0
divBoth=0
while(i <=100):
    if i%3==0 and i%5==0:
        divBoth+=1
    elif i%3==0:
        div3+=1
    elif i%5==0:
        div5+=1
    i+=1
print("Count of div by Both->",divBoth)
print("Count of div by 3->",div3)
print("Count of div by 5->",div5)