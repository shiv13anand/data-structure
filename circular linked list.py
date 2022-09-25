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
#Line 18 i.e. while(temp->next!=head) establishes that the traversing element/variable has reached the first element.
#We Know that in circular linked list last node of linked list points to head of that linked list, hence we can check if any node points to head of linked list then that node is the end of circular linked list.



		


# In[ ]:




