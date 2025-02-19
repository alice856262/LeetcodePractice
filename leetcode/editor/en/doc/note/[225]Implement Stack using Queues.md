## Algorithm Description
### Key Idea
- Use a single queue to simulate the behavior of a stack.
- To maintain the **LIFO (Last-In-First-Out) order**, the queue is rotated by repeatedly removing elements from the front and appending them to the end until the last added element is at the front.

### Step-by-Step Algorithm
- Initialization:
  - Create an empty queue ```self.queue``` using a deque.
- Push Operation:
  - Append the new element to the end of the queue.
- Pop Operation:
  - Rotate the queue by repeatedly **removing elements from the front** and **appending them to the end** until the last added element is at the front.
  - Remove and return the front element of the queue.
- Top Operation:
  - Directly return the last element of the queue using the ```[-1]``` index, which represents the "top" of the stack.
- Empty Operation:
  - Check if the queue is empty by verifying if its length is zero.

## Algorithmic Complexity
- Time Complexity:
  - Push: O(1) - Adding an element to the end of the queue is a constant-time operation.
  - Pop: O(n) - Rotating the queue to place the last element at the front requires ```n-1``` operations, where ```n``` is the number of elements in the queue.
  - Top: O(1) - Accessing the last element of the queue is a constant-time operation.
  - Empty: O(1) - Checking if the queue is empty is a constant-time operation.
- Space Complexity: O(n)
  - The queue stores all elements currently in the stack.

## Notes on Solving Process
- The key idea is to use the queue's FIFO (First-In-First-Out) nature and modify it with rotations to achieve LIFO behavior.
- This approach is optimal in terms of space, using only one queue, but incurs an O(n) cost for the ```pop``` operation due to the rotations.
- The ```top``` and ```empty``` operations are efficient, requiring only O(1) time.