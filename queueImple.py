def isEmpty(q):
    return len(q) == 0

def enqueue(a, q):
    q.append(a)
    
def dequeue(q):
    if isEmpty(q):
        return "Underflow!"
    else:
        return q.pop(0)
    
def peek(q):
    if isEmpty(q):
        return "Underflow!"
    else:
        return q[-1]
    
def display(q):
    if isEmpty(q):
        return "Underflow!"
    else:
        for item in q:
            print(item, end=" ")
        print("Front to rear: ", q[0])
            
queue = []

while True:
    print("Press key for performing particular functions: \n1. Enqueue \n2. Dequeue \n3. Peek \n4. Display \n5. Exit")
    try: 
        choice = int(input("Enter command: "))
        if(choice == 1):
            element = int(input("Enter the element you want to enqueue: "))
            enqueue(element, queue)
            
        elif(choice == 2):
            item = dequeue(queue)
            if item == "Underflow!":
                print("Queue is empty")
            else:
                print("Dequeued element: ", item)
                
        elif(choice == 3):
            item = peek(queue)
            if item == "Underflow!":
                print("Queue is empty!")
            else:
                print("\nFront element: ", item)
                
        elif(choice == 4):
            display(queue)
            
        elif(choice == 5):
            print("Exiting")
            break
        else:
            print("Invalid choice!")
        
    except ValueError:
        print("Enter valid keys!") 
        
    
            
            
        
            

                
    