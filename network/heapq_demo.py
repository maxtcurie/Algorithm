import heapq

def demonstrate_heapq_functions():
    # Initialize an empty priority queue
    pq = []

    # heappush: Insert elements into the priority queue with different priorities (costs)
    heapq.heappush(pq, (3, 'task 1'))
    heapq.heappush(pq, (1, 'task 2'))
    heapq.heappush(pq, (2, 'task 3'))
    heapq.heappush(pq, (4, 'task 4'))

    print("Priority queue after heappush operations:", pq)

    # heappop: Remove and return the smallest element from the priority queue
    smallest = heapq.heappop(pq)
    print("Popped element:", smallest)
    print("Priority queue after heappop operation:", pq)

    # heapify: Transform a list into a heap, in-place, in linear time
    unordered_list = [(5, 'task 5'), (3, 'task 6'), (4, 'task 7')]
    heapq.heapify(unordered_list)
    print("Unordered list after heapify:", unordered_list)

    # heappushpop: Push an element on the heap and then pop and return the smallest element
    result = heapq.heappushpop(pq, (0, 'task 8'))
    print("Result of heappushpop operation:", result)
    print("Priority queue after heappushpop operation:", pq)

# Run the demonstration
demonstrate_heapq_functions()
