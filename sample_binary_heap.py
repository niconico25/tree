"""Sample Code."""
import heapq  # noqa
from tree.binary_heap import BinaryHeap
from tree.display.text import str_tree


#
def exec_print(expression):
    exec(expression, globals())
    print(expression)
    print(BinaryHeap(heap))  # noqa
    print()


#
# 1) 単純に並べただけで
#    まだヒープではない。
#
exec_print('heap = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]')
#               01
#       03              05
#   07      09      02      04
# 06  08  00

#
# 2) heapify 関数でヒープにする。
#
exec_print('heapq.heapify(heap)')
#               00
#       01              02
#   06      03      05      04
# 07  08  09


#
# 3) heappop
#
exec_print('heapq.heappop(heap)')
#               01
#       03              02
#   06      09      05      04
# 07  08

exec_print('heapq.heappop(heap)')
#               02
#       03              04
#   06      09      05      08
# 07

exec_print('heapq.heappop(heap)')
#       03
#   06      04
# 07  09  05  08


#
# 4) heappush
#
exec_print('heapq.heappush(heap, 10)')
#               03
#       06              04
#   07      09      05      08
# 10

exec_print('heapq.heappush(heap,  1)')
#               01
#       03              04
#   06      09      05      08
# 10  07

exec_print('heapq.heappush(heap,  0)')
#               00
#       01              04
#   06      03      05      08
# 10  07  09
