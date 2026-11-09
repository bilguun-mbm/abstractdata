# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.

# Exercise 1
Stack = []
for x in range(10):
    Stack.append(-1)
TopOfStack=-1

def IsEmpty():
    global TopOfStack
    return TopOfStack == -1

def IsFull():
    global TopOfStack
    return TopOfStack == 9

# Exercise 2
def Push(Item):
    global Stack,TopOfStack
    
    if IsFull():
        return False
        
    TopOfStack = TopOfStack + 1
    Stack[TopOfStack] = Item
    
    return True


# Exercise 3
def Pop():
    global Stack,TopOfStack
    
    if IsEmpty():
        return -1
        
    ItemToReturn = Stack[TopOfStack]
    TopOfStack = TopOfStack - 1
    
    return ItemToReturn


# Exercise 4
# Exercise 4
def Peek():
    global Stack, TopOfStack
    if IsEmpty():
        return -1
    return Stack[TopOfStack]

def Size():
    global TopOfStack
    return TopOfStack + 1


# Exercise 5
def ReverseWord(Word):
    global Stack, TopOfStack
    TopOfStack = -1

    for letter in Word:
        Push(letter)
    NewString = ""
    while not IsEmpty():
        NewString = NewString + Pop()
    return NewString
