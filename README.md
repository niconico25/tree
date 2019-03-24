# Python tree utilities
This code was written to help your understanding binary search trees and binary heaps.

An expected working directory is `tree`.
```
$ git clone https://github.com/niconico25/tree
$ cd tree  # <- expected working directory
```

## 1. heapq
Python standard libary provides `heapq`, 
so I just wrote a code to show how `heapq` works.
### 1.1. Display heap.
```python
from heapq import heapify
from tree.binary_heap import BinaryHeap

lst = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(lst)
print(BinaryHeap(lst))
```
```
>>> print(BinaryHeap(lst))
               00              
       01              02      
   06      03      05      04  
 07  08  09  
>>>
```

### 1.2. Check how heapq works.
#### heappop and heappush
You can see how heapq works.
```python
from heapq import heappush
from heapq import heappop
from tree.binary_heap.heapq import heappush as heappush_print
from tree.binary_heap.heapq import heappush as heappop_print

heap = [] 
heappush(heap, 6)
heappush(heap, 5)
heappush(heap, 4)
heappush(heap, 3)
heappush(heap, 2)
heappush(heap, 1)
heappush_print(heap, 0)
heappop_print(heap)
```
```
>>> heappush_print(heap, 0)

heappush
      01      
  03      02  
06  04  05    

_shiftdown 0 -> 1 要素 0 から 1 に向けてバブルアップ
_shiftdown: before
      01      
  03      02  
06  04  05  00
_shiftdown: in progress
      01      
  03      02  
06  04  05  02
_shiftdown: in progress
      01      
  03      01  
06  04  05  02
_shiftdown: after
      00      
  03      01  
06  04  05  02
>>> 
```
```
>>> heappop_print(heap)

heappop
      00      
  03      01  
06  04  05  02

_shiftup 2 -> leaf 要素 2 から葉に向けてバブルダウン
_shiftup: before
      02      
  03      01  
06  04  05    
_shiftup: in progress
      01      
  03      01  
06  04  05    
_shiftup: in progress
      01      
  03      05  
06  04  05    
_shiftup: after
      01      
  03      05  
06  04  02    

_shiftdown 2 -> 1 要素 2 から 1 に向けてバブルアップ
_shiftdown: before
      01      
  03      05  
06  04  02    
_shiftdown: in progress
      01      
  03      05  
06  04  05    
_shiftdown: after
      01      
  03      02  
06  04  05    
0
>>> 
```

#### heapify

```python
from tree.binary_heap.heapq import heapify

heap = [6, 5, 4, 3, 2, 1, 0]
heapify(heap)
```
```
>>> heapify(heap)



heapify: looping

_shiftup 4 -> leaf
_shiftup: before
      06      
  05      04  
03  02  01  00
_shiftup: in progress
      06      
  05      00  
03  02  01  00
_shiftup: after
      06      
  05      00  
03  02  01  04

_shiftdown 4 -> 0
_shiftdown: before
      06      
  05      00  
03  02  01  04
_shiftdown: after
      06      
  05      00  
03  02  01  04



heapify: looping

_shiftup 5 -> leaf
_shiftup: before
      06      
  05      00  
03  02  01  04
_shiftup: in progress
      06      
  02      00  
03  02  01  04
_shiftup: after
      06      
  02      00  
03  05  01  04

_shiftdown 5 -> 2
_shiftdown: before
      06      
  02      00  
03  05  01  04
_shiftdown: after
      06      
  02      00  
03  05  01  04



heapify: looping

_shiftup 6 -> leaf
_shiftup: before
      06      
  02      00  
03  05  01  04
_shiftup: in progress
      00      
  02      00  
03  05  01  04
_shiftup: in progress
      00      
  02      01  
03  05  01  04
_shiftup: after
      00      
  02      01  
03  05  06  04

_shiftdown 6 -> 0
_shiftdown: before
      00      
  02      01  
03  05  06  04
_shiftdown: after
      00      
  02      01  
03  05  06  04
>>> 
```





## 2. binary search tree
Usually, we can use `bisect` module instead of binary search tree.
But for just understanding, I implemented binary search tree.


### 2.1. type of node implementations
`sequencial.py` implements BinarySearchNode by while statement.
`parental.py` implements BinarySearchNode by while statement
and its attribute has a reference to his parental node. 
```
 tree
 └── binary_search_tree
     ├── __init__.py      Tree
     ├── recursive.py     Node
     ├── sequencial.py    Node
     └── parental.py      Node
```
```python
from tree.binary_search_tree.recursive import BinarySearchNode
# from tree.binary_search_tree.sequencial import BinarySearchNode
# from tree.binary_search_tree.parental import BinarySearchNode
bst = BinarySeachTree(BinarySearchTree)
```

### 2.2. usage
```python
from tree.binary_search_tree import BinarySearchTree
from tree.binary_search_tree.recursive import BinarySearchNode



bst = BinarySearchTree(BinarySearchNode)


#
# 1. insert
#
bst.insert(8)
bst.insert(3)
bst.insert(1)
bst.insert(6)
bst.insert(10)
bst.insert(4)
bst.insert(7)
bst.insert(14)
bst.insert(13)
print(bst)
#               08
#       03              10
#   01      06              14
#         04  07          13


#
# 2. search
#
bst.search(13).value
# 13

bst.search(11).value
# ValueError



#
# 3. list
#
bst.list()
# [1, 3, 4, 6, 7, 8, 10, 13, 14]

list(bst)
# [1, 3, 4, 6, 7, 8, 10, 13, 14]




#
# 4. delete
#

# 4.1. 右下の子の最大値を上に持ってくる。
bst.delete_right(8)
print(bst)
#               10
#       03              14
#   01      06      13
#         04  07


# 4.2. 左下の子の最小値を上に持ってくる。
bst.delete_left(10)
print(bst)
#               07
#       03              14
#   01      06      13
#         04
```
