
class stack:
    def __init__(self):
        self.items=[]

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def prints(self):
        print(self.items)



if __name__ == '__main__' :
    s=stack()
    n=int(input())
    for i in range(n):
        s.push(input())
    s.prints()
    