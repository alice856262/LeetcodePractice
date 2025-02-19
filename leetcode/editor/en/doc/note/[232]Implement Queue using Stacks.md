## Algorithm Description
### Key Idea
- Implement a queue using two stacks: ```stack_in``` for incoming elements and ```stack_out``` for outgoing elements.
- Elements are pushed to ```stack_in```, and when ```stack_out``` is empty, elements from ```stack_in``` are transferred to ```stack_out``` in reverse order.
- This approach ensures that the oldest element (front of the queue) is at the top of ```stack_out```, enabling FIFO behavior.

### Step-by-Step Algorithm
- Initialization:
  - Create two empty stacks: ```stack_in``` and ```stack_out```.
- Push Operation:
  - Add the new element to the top of ```stack_in```.
- Pop Operation:
  - If ```stack_out``` is empty, transfer all elements from ```stack_in``` to ```stack_out``` by popping from ```stack_in``` and pushing to ```stack_out```.
  - Pop the top element from ```stack_out``` (the front of the queue).
- Peek Operation:
  - If ```stack_out``` is empty, transfer all elements from ```stack_in``` to ```stack_out``` as described in the pop operation.
  - Return the top element of ```stack_out``` without removing it.
- Empty Operation:
  - Return ```True``` if both ```stack_in``` and ```stack_out``` are empty; otherwise, return ```False```.

## Algorithmic Complexity
- Time Complexity:
  - Push: O(1) - Appending to a stack is constant time.
  - Pop: **Amortized O(1)** - Each element is transferred from ```stack_in``` to ```stack_out``` **at most once**. After the transfer, pops from ```stack_out``` are O(1).
  - Peek: **Amortized O(1)** - Same logic as pop; elements are transferred only when ```stack_out``` is empty. After the transfer, peeks from ```stack_out``` are O(1).
  - Empty: O(1) - Checking emptiness of two stacks is constant time.
- Space Complexity: O(n)
  - ```n``` is the total number of elements. Both ```stack_in``` and ```stack_out``` can hold up to ```n``` elements combined.

## Notes on Solving Process
- The key insight is to use two stacks to mimic the behavior of a queue by **reversing the order** of elements in ```stack_in``` when **transferring to ```stack_out```**.
- The amortized O(1) time complexity for ```pop``` and ```peek``` comes from the fact that **each element is moved between stacks at most once**, ensuring efficient performance.
  - E.g., when performing multiple pop/peek operations, only the first pop/peek requires transferring elements from ```stack_in``` to ```stack_out``` (if ```stack_out``` is empty). Once the elements are in ```stack_out```, subsequent pop/peek operations simply remove/return elements directly from ```stack_out```, which takes O(1) per operation.