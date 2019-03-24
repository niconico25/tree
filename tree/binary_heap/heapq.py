from . import BinaryHeap


def heappush(heap, item):
    print('')
    print('heappush')
    print(BinaryHeap(heap))

    heap.append(item)
    _siftdown(heap, 0, len(heap) - 1)


def heappop(heap):
    print('')
    print('heappop')
    print(BinaryHeap(heap))

    lastelt = heap.pop()
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt


def heapify(x):
    n = len(x)
    for i in reversed(range(n // 2)):
        print('')
        print('')
        print('')
        print('heapify: looping')
        _siftup(x, i)


def _siftup(heap, pos):
    print('')
    print('_shiftup', heap[pos], '-> leaf')
    print('_shiftup: before')
    print(BinaryHeap(heap))

    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]

    # Bubble up the smaller child until hitting a leaf.
    childpos = 2 * pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos:
            if heap[childpos] >= heap[rightpos]:
                childpos = rightpos

        # Move the smaller child up.
        heap[pos] = heap[childpos]
        print('_shiftup: in progress')
        print(BinaryHeap(heap))

        pos = childpos
        childpos = 2 * pos + 1

    # The leaf at pos is empty now.  Put newitem there,
    heap[pos] = newitem
    print('_shiftup: after')
    print(BinaryHeap(heap))

    # and bubble it up
    # to its final resting place (by sifting its parents down).
    _siftdown(heap, startpos, pos)


def _siftdown(heap, startpos, pos):
    print('')
    print('_shiftdown', heap[pos], '->', heap[startpos])
    print('_shiftdown: before')
    print(BinaryHeap(heap))

    newitem = heap[pos]
    # Follow the path to the root,
    # moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            print('_shiftdown: in progress')
            print(BinaryHeap(heap))
            pos = parentpos
            continue
        break

    heap[pos] = newitem
    print('_shiftdown: after')
    print(BinaryHeap(heap))
