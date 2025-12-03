# # Name: HUSSAIN ABDULHAMID OLUWASEGUN
# # Matriculation Number: 230502026
# # Department: Computer Science
# # College: CONAS
# # Course Code: CSC 301
# # Course Title: Data Structure 

# # 			ASSIGNMENT 1(SOLUTIONS)

# # Activity 1:
# # Write a function to compute the sum of all elements in a list. Analyze its time complexity.
# # def total_sum(arr):
# #     total = 0
# #     for i in arr:
# #         total += i
# #     return total
# # •	Time Complexity: O(n)
# # •	Space Complexity: O(1)

# # Solution
# # Python Function:
# # def total_sum(arr):
# #     total = 0
# #     for i in arr:
# #         total += i
# #     return total   
# # (Refer to activity1.py file for an illustration(code))

# # 1. Time Complexity: O(n)
# # •	The loop runs once for each element in the list.
# # •	If the list has n elements, the function performs n additions.
# # •	Therefore, the time grows linearly with the size of the input.

# # 2. Space Complexity: O(1)
# # •	The function uses only one extra variable (total), regardless of the list size.
# # •	No additional data structures are created.
# # •	So memory usage stays constant.

# # Activity 2:
# # Trace how linked list insertion at the head works using a diagram?

# # Solution
# #  Insertion at the Head of a Linked List
# # Suppose we have an existing linked list:
# # HEAD
# # |
# # v
# # [10] -> [20] -> [30] -> None
# # And we want to insert a new node with value 5 at the head.
# # Step-by-Step Process (With Diagram)
# # Step 1: Create a new node:
# # Create a node containing the new data.
# # New Node
# # [5] -> None
# # Step 2: Point the new node to the current head:
# # Make the next pointer of the new node refer to what the head was pointing to.
# # New Node   HEAD
# #  	  |                    |
# #   v                    v
# #  [5]       ->     [10] -> [20] -> [30] -> None
# # Step 3: Move HEAD to the new node:
# # Update the head pointer to point to the new node.
# # HEAD
# #  	 |
# #  	 v
# # [5] -> [10] -> [20] -> [30] -> None
# # Final Diagram (After Insertion):
# # HEAD
# #  	 |
# #  	 v
# # [5] -> [10] -> [20] -> [30] -> None

# # Note:
# #  Very Short Explanation 
# # 1.	Create a new node.
# # 2.	Set new_node.next = head.
# # 3.	Update head = new_node.

# # 5. Laboratory Work
# # Tasks:
# # 1.	Create a class Node and LinkedList.
# # 2.	Implement:
# # o	insert_at_beginning(data)
# # o	insert_at_end(data)
# # o	delete_node(key)
# # o	display_list()
# # 3.	Test your linked list by inserting at least 5 values and deleting one.
# # Solution
# # Refer to   exercise5.py file.

# # 4.	Write short answers to:
# # o	What is the difference between arrays and linked lists?
# # o	What is the time complexity of insertion in a linked list?


# # Solution
# # 1. What is the difference between arrays and linked lists?
# # Arrays:
# # •	Stored in contiguous memory locations.
# # •	Fixed size (cannot grow easily).
# # •	Fast random access using index (O(1)).
# # Linked Lists:
# # •	Nodes are stored in non-contiguous memory.
# # •	Dynamic size (can grow/shrink easily).
# # •	No direct indexing — access is sequential (O(n)).

# # 2.  What is the time complexity of insertion in a linked list?
# # •	Insertion at the beginning: O(1)
# # •	Insertion at the end: O(n) if we traverse, or O(1) if tail pointer is used.
# # •	General Answer: O(1) for head insertion.

# # 6. Discussion Questions
# # 1.	What are the key differences between primitive data types and ADTs?

# # Solution

# # Primitive Data Types
# # •	Built into the programming language.
# # •	Store simple, basic values.
# # •	Fixed size.
# # •	Examples: int, float, char, bool.

# # Abstract Data Types (ADTs)
# # •	Not built-in; they are logical models for organizing data.
# # •	Define what operations can be performed, not how they are implemented.
# # •	Can store complex data.
# # •	Examples: Stacks, Queues, Linked Lists, Trees, Graphs.



# # Key Differences
# # Primitive Types	ADTs
# # Simple values	Complex data structures
# # Fixed size	Flexible size
# # Directly supported by language	Logical concept implemented by programmer
# # No special operations	Defined operations (push, pop, enqueue, insert, etc.)


# # 2.	Why are arrays considered static, and linked lists dynamic?

# # Solution
# # Arrays (Static)
# # •	Fixed size once created.
# # •	Memory is allocated in a continuous block.
# # •	You cannot increase or decrease the size at runtime.
# # •	Adding/removing elements is difficult.

# # Linked Lists (Dynamic)
# # •	Size can grow or shrink without limit during runtime.
# # •	Memory is allocated node by node, not continuously.
# # •	Easy to insert or delete any node.

# # 3.	In what situations would you prefer a linked list over an array?

# # Solution 
# # You would choose a linked list when:
# # a.	You need frequent insertions or deletions, especially at the head or middle.
# # b.	Memory efficiency is important, and you don't know the number of items beforehand.
# # c.	Dynamic size is needed — the list grows and shrinks during execution.
# # d.	You want efficient sequential access without shifting elements

# # 4.	Give real-world examples where each of the following would be useful:
# # o	Stack
# # o	Queue
# # o	Linked List

# # Solution 
# # a) Stack – LIFO (Last In, First Out)
# # Real-world examples:
# # •	Undo/Redo in Microsoft Word.
# # •	Browser history (Back button).
# # •	Plate stack in a kitchen.
# # •	Call stack during program execution.

# # b) Queue – FIFO (First In, First Out)
# # Real-world examples:
# # •	People standing in a bank queue.
# # •	Printer job scheduling.
# # •	Customer service ticket system.
# # •	Task scheduling in operating systems.

# # c) Linked List
# # Real-world examples:
# # •	Music playlist where you can add/remove songs easily.
# # •	Slide navigation in PowerPoint (next/previous slides).
# # •	Image viewer navigation.
# # •	Implementation of other data structures (stack, queue, hash chains).





# 			ASSIGNMENT 2 (SOLUTIONS)
# 1)	Difference between Queue and Stack?

# Solution

# 1. Order of Processing:
# •	Stack: Uses LIFO (Last In, First Out)
# •	Queue: Uses FIFO (First In, First Out)

# 2. Insertion and Removal Points:
# •	Stack: Both insert (push) and remove (pop) from the same end (top).
# •	Queue: Insert (enqueue) at the rear and remove (dequeue) from the front.

# 3. Structure Behaviour:
# •	Stack: Behaves like a stack of plates — last placed is first to be removed.
# •	Queue: Behaves like a line of people — first person in line is served first.

# 4. Main Operations:
# •	Stack: push, pop, peek.
# •	Queue: enqueue, dequeue, front, rear.

# 5. Applications:
# •	Stack: Used for function calls, undo operations, expression evaluation.
# •	Queue: Used for scheduling tasks, managing requests, printing jobs, buffering.


# 2)	Time Complexity of Stack and Queue?

# Solution

# 1. Stack
# Operations:
# 1.	Push (add an element)
# o	Array-based stack:
# 	Usually O(1) if there is space.
# 	If array needs resizing, worst-case O(n), but amortized O(1).
# o	Linked-list stack:
# 	Always O(1) because you just add a node at the head.
# 2.	Pop (remove top element)
# o	Array-based: O(1)
# o	Linked-list: O(1)
# 3.	Peek/Top (view top element)
# o	Both O(1)


# Summary for Stack:
# Operation	Array-based	Linked-list
# Push	O(1) amortized	O(1)
# Pop	O(1)	O(1)
# Peek	O(1)	O(1)


# 2. Queue
# Operations:
# 1.	Enqueue (add element at rear)
# o	Array-based queue:
# 	If using a simple array and shifting elements: O(n) (because of shifting).
# 	If using circular array, O(1).
# o	Linked-list queue:
# 	O(1) (just add node at rear pointer).
# 2.	Dequeue (remove element from front)
# o	Array-based queue:
# 	Simple array: O(n) (shift elements).
# 	Circular array: O(1)
# o	Linked-list queue:
# 	O(1) (just remove node from front pointer).
# 3.	Peek/Front (view front element)
# o	Both O(1)


# Summary for Queue:
# Operation	Array-based (circular)	Linked-list
# Enqueue	O(1)	O(1)
# Dequeue	O(1)	O(1)
# Peek	O(1)	O(1)



