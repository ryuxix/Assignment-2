# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None

# Creating add_front
    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head  
        # Points to the current head.
        self.head = new_node
        # Update the head of the list to be the new node

# Creating add_end
    def add_end(self,name):
        new_node = Node(name)
        if self.head is None: 
            self.head = Node(name)
            return
         # If the list is empty it makes the new node the head.

        current = self.head
        while current.next: 
            current = current.next 
        current.next = new_node
        # Looks at the list to find the last node and sets the next pointer of the last node to the new node.

# Creating removing name
    def remove(self, name):
        if self.head is None:
            print(f"{name} not found")
            return
        # Tells you if name was not found.

        # Case 1 Removing the Head Node
        if self.head.name == name:
            self.head = self.head.next
            print(f"{name} has been removed from the waitlist.")
            return
        
        # Case 2  Searching for the node to remove
        current_node = self.head
        while current_node.next:
            if current_node.next.name == name:
                current_node.next = current_node.next.next
                print(f"{name} has been removed from the waitlist.")
                return

# Creating print_list
    def print_list(self):
        if self.head is None:
            print("The waitlist is empty")
            return
        current_node = self.head
        while current_node:
            print(current_node.name)
            current_node = current_node.next


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            waitlist.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?
'''
# The Memo
# I would say how my list works is by linking the nodes together where each node stores the name of the customer and a pointer that tells the program where the next node is located. Instead of being stored in one block of memory the linked list is spread out in different memory locations.
# I would say the main connections between the nodes are what allow the program to move through the list in order. This can make linked lists flexible because you can easily add or remove data without having to shift everything around. 
# The role that the head plays in a linked list is that it represents the starting point of the list. Without the head you would have no way of accessing the rest of the nodes since each one is connected by its pointer to the next. I feel like a real engineer may need a custom list like this when working with situations where data changes frequently and memory flexibility is important. 
# For example, when operating a system linked lists are used to manage tasks or processes that are constantly being created and removed. With a custom list it gives engineers control over how data is stored, updated, and accessed which can be useful for performance and problem solving.
