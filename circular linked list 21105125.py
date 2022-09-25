#!/usr/bin/env python
# coding: utf-8

# In[3]:


# [Question.1] While traversing a single-circular linked list, which condition establishes that the traversing element/variable has reached the first element? */


#Ans 1
#Lets take an example and create a basic circular linked list
# circular linked list traversal

# Structure for a Node
class Node:
	
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.next = None

class CircularLinkedList:
	
	# Constructor to create a empty circular linked list
	def __init__(self):
		self.head = None

	# Function to insert a node at the beginning of a
	# circular linked list
	def push(self, data):
		ptr1 = Node(data)
		temp = self.head
		
		ptr1.next = self.head

		# If linked list is not None then set the next of
		# last node
		if self.head is not None:
			while(temp.next != self.head):#This condition establishes that the traversing element(temp) has reached the first element
				temp = temp.next
			temp.next = ptr1

		else:
			ptr1.next = ptr1 # For the first node

		self.head = ptr1

	# Function to print nodes in a given circular linked list
	def printList(self):
		temp = self.head
		if self.head is not None:
			while(True):
				print (temp.data, end=" ")
				temp = temp.next
				if (temp == self.head):
					break


# Driver program to test above function

# Initialize list as empty
cllist = CircularLinkedList()

# Created linked list will be 11->2->56->12
cllist.push(9)
cllist.push(6)
cllist.push(9)
cllist.push(6)

print ("Contents of circular Linked List")
cllist.printList()


#With reference to above example of circular linked list.
#Line 39 i.e. while(temp->next!=head) establishes that the traversing element/variable has reached the first element.
#We Know that in circular linked list last node of linked list points to head of that linked list, hence we can check if any node points to head of linked list then that node is the end of circular linked list.



		


# In[4]:


#[Question.2]  What are the practical applications of a circular linked list? (Try to find applications in your respective fields).

#ans 2 ; practical applications are:-
1.games:-
  #A ludo game has to come back give turn to first player after 4th player so it has to be circular.

  #The one I always think of is the Snake game on your phone.The circular linked list stores the x,y position of each point in the snake's body.The head of the list is the snake's head.The tail is its tail.And the really nice property is that as you advance the head to a new position, the list wraps around because it is circular. This erases the tail, and leaves all other body parts as they are
    
2. computer applications:-
    #Computer Networking:Circular linked list is also used in computer networking for token scheduling.
    
    #Implementation of Data Structure: Data structures such as stacks and queues are implemented with the help of the circular linked 
    
    #A good example of an application where circular linked list should be used is a timesharing problem solved by the operating system.In a timesharing environment, the operating system must maintain a list of present users and must alternately allow each user to use a small slice of CPU time, one user at a time. The operating system will pick a user, let him/her use a small amount of CPU time and then move on to the next user, etc.For this application, there should be no NULL pointers unless there is absolutely no one requesting CPU time.
    
    # Circular linked list is also used in audio and video streaming,for ex. when one copmlete audio list finishes playing in music player then it again starts playing from start.
    
    #In our keyboard we have alt+tab key this is circular linked list it goes back on to first tab after last tab and we can go back also.
    
    #It is also used in computer networking for token scheduling.
    
3. In my field:-(ece)
    # as my field is electronics and communication it was very difficult to think of practical applications but ther are some for eg if we build a mechatronics system like escalators we can make use of circular linked list in circular escalators.
    #Allocating CPU to resources


# In[ ]:




