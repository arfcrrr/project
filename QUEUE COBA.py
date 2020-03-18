#difference between stack n queue
#stack : first in first out

print(24*'=')
print(' WELCOME TO YUM\'S CAFE ')
print(24*'=')

class Cafe:
    name = None
    order = None
    amount = None
    price = None
    total = None
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.Cafe = []
        
        #making 3 static datas
        for i in range(0, cust):
            self.Cafe.append([])
            self.Cafe[i] = Cafe()
            
    def createEmpty(self):
        self.first = -1
        self.last = -1
    
    def isEmpty(self):
        result = False
        if(self.first == -1):
            result = True
        return result
    
    def isFull(self):
        result = False
        if(self.last == len(self.Cafe)-1):
            result = True
        return result
    
    def add(self, name, order, amount, price, total):
        if(self.isEmpty() == True): #if queue is still empty
            self.last = 0
            self.first = 0
            self.Cafe[0].name = name
            self.Cafe[0].order = order
            self.Cafe[0].amount = amount
            self.Cafe[0].price = price
            #self.Cafe[0].total = amount*price
        else:
            if(self.isFull() != True): #if queue is empty 
                self.last = self.last + 1
                self.Cafe[self.last].name = name
                self.Cafe[self.last].order = order
                self.Cafe[self.last].amount = amount
                self.Cafe[self.last].price = price
                #total_price = self.Cafe[self.last].amount*self.Cafe[self.last].price
                #self.Cafe[self.last].total = total_price
            else:
                print('Queue is full!')
        
    def delete(self):
        if(self.last == 0): #if stack contain 1 element
            self.first = -1
            self.last = -1
        else:
            for i in range(self.first+1, self.last+1):
                self.Cafe[i-1].name = self.Cafe[i].name
                self.Cafe[i-1].order = self.Cafe[i].order
                self.Cafe[i-1].amount = self.Cafe[i].amount
                self.Cafe[i-1].price = self.Cafe[i].price
                #self.Cafe[i-1].total = self.Cafe[i].total
                
            self.last = self.last - 1
            
    def PrintQueue(self):
        if(self.first != -1):
            print()
            print(5*'-','ORDERS',5*'-' )
            print('')
            for i in range(self.last, (self.first-1), -1):
                print(15*'=')
                print('ORDER [', i+1, ']')
                print('Name : ', self.Cafe[i].name)
                print('Order : ', self.Cafe[i].order)
                print('Amount : ', self.Cafe[i].amount)
                print('Price : $', self.Cafe[i].price)
                #print('Total : $', self.Cafe[i].total)
            print(15*'=')
        else:
            print('NO NEED TO WAIT! PLEASE INPUT YOUR ORDER TO CASHIER') #if stack is empty
            
cafe = Queue() #making object
print()
print(5*'-', 'Before Ordering', 5*'-')
cafe.createEmpty()
cafe.PrintQueue()

cust = int(input('How many customers do we have : '))
print('')

print(5*'-', ' Input Customer\'s Order', 5*'-')
for i in range(0, cust):
    print()
    print(16*'=')
    print(' Customer [', i+1, ']')
    print(16*'=')
    cust_input = cafe.add(input('Name : '),
                          input('Order : '),
                          int(input('Amount : ')),
                          int(input('Price : ')))
                          #print('Total : ', total_price))

cafe.PrintQueue()
print()

print(5*'=', 'Thanks for coming!', 5*'=')
cafe.delete()
cafe.PrintQueue() 
                