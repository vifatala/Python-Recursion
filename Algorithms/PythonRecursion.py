# EXERCISE 1:

# Alex is a gemstone collector who recently placed an order for an assortment of ambers, jades, pearls, and sapphires. 
# When he opened the delivery package, Alex found that his list of gemstones was mixed up.
# Alex is particularly fond of a certain type of gemstone and wants to move them to the end of his gallery display. Let’s design a recursive algorithm to help Alex set up his gallery:

def move_to_end(lst, val):
  result = []
  # base case:
  if not len(lst):
    return result
  # recursive step:
  if lst[0] == val:
    result += move_to_end(lst[1:], val)
    result.append(lst[0])
  else:
    result.append(lst[0])
    result += move_to_end(lst[1:], val)
  
  return result


gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EXERCISE 2 (not working due to lack of LinkedList class. Conceptual only):

# Now that Alex’s gallery display is organized in the correct order, we can use a linked list to represent the series of gemstones.
# The linked list class has been implemented for you behind the scene.
# A friend asks Alex if she could buy a gemstone from his gallery. Alex agrees to remove any gemstone and sell it to her. How can he delete the i-th node from the linked list recursively?

import LinkedList

# Definition for singly-linked list node.
# class ListNode:
#     def __init__(self, value, next_node=None):
#         self.value = value
#         self.next_node = next_node

def remove_node(head, i):
  if i < 0:
    return head
  if head is None:
    return None
  if i == 0:
    return head.next_node

  head.next_node = remove_node(head.next_node, i - 1)
  return head

# Test code - do not edit
gemstones = LinkedList.LinkedList(["Amber", "Sapphire", "Jade", "Pearl"])
head = remove_node(gemstones.head, 1)
print(head.flatten())

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EXERCISE 3:

# Alex has picked out the gemstone that caught his friend’s fancy.
#  He needs to wrap this fragile gemstone in wrapping paper before shipping it off to her.
#  For our purpose, we will represent each layer of wrapping paper as "<>", so a pearl wrapped in 3 layers would be "<<<Pearl>>>".
#  Let’s define a recursive function that wraps up a specified string in n layers of wrapping paper.

# define wrap_string() here
def wrap_string(string, num):
  result = string
  # edge case:
  if num < 0:
    print("Needs to be at least 0.")
  # base case:
  if num == 0:
    return result
  # recursive step:
  return wrap_string("<" + result + ">", num-1)

# Test code - do not edit
wrapped = wrap_string("Pearl", 3)
print(wrapped)


