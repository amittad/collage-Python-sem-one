def collage():
    a=[i for i in range(1,10) if i%2==0]
    print(a)

def tabale():
    yield collage()

for i in tabale():
    print(i) 
