# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#     def remove_3(head):
#         current = head
#         while current.next and current.next.next:
#             if current.next.value == 3:
#                 current.next = current.next.next
#                 break
#             else:
#                 current = current.next
#         return head
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# node6 = Node(6)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6
    
# def traverse(head):
#     current = head
#     while current:
#         print(current.value)
#         current = current.next
#     print("null")
#     pass
# node1 = remove_3(node1)
# traverse(node1)
dicct = {4: 5, 6: 7}
k = dicct.keys()
print(k)