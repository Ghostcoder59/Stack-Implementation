def isEmpty(stk):
    return len(stk) == 0

def push(s,a):
    s.append(a)
    
def pop(s):
    if isEmpty(s):
        return "Underflow!"
    else:
        return s.pop()
    
def peek(s):
    if isEmpty(s):
        return "Underflow!"
    else:
        return s[-1]

def display(s):
    if isEmpty(s):
        return "Underflow!"
    else:
        print(s[-1], "<-- Top")
        for item in reversed(s[:-1]):
            print(item)
        
stack = []

while True:
    print("Press the key to perform certain function\n1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit")
    try:
        choice = int(input("Enter command: "))
        if choice == 1:
            element = int(input("Enter the element to be inserted: "))
            push(stack, element)
        elif choice == 2:
            item = pop(stack)
            if item == "Underflow!":
                print("Underflow!")
            else:
                print("Popped item: ", item)
        elif choice == 3:
            item = peek(stack)
            if item == "Underflow!":
                print("Undderflow!")
            else:
                print("Top element: ", item)
                
        elif choice == 4:
            display(stack)
        
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
    except ValueError:
        print("Enter a valid number!")
        