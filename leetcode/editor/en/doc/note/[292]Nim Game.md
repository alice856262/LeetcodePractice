## Algorithm Description
### Key Idea
- **Optimal Play Strategy**: The goal is to force your opponent into a position where the remaining number of stones is a multiple of 4.
- **Multiple of 4 Invariant**: If you always leave a multiple of 4 stones for your opponent, no matter how many stones (1 to 3) they remove, you can mirror their move (by removing ```4 - k``` stones) and keep the invariant. This forces a win because eventually, your opponent will be left with 4 stones on their turn.

### Step-by-Step Algorithm
- Step 1: Determine if the total number of stones ```n``` is a multiple of 4 by computing ```n % 4```.
- Step 2: Return the Result
  - Return ```False``` if ```n % 4 == 0```, then the position is losing for you because your opponent can always mirror your moves.
  - Return ```True``` if ```n % 4 != 0```, you can remove ```n % 4``` stones on your first move to leave a multiple of 4 for your opponent.

## Algorithmic Complexity
- Time Complexity: O(1)
  - The solution involves a simple modulus operation, which is constant time.
- Space Complexity: O(1)
  - No extra space is used beyond a few integer variables.

## Notes on Solving Process
- The problem is reduced to an arithmetic check based on the observation that having a multiple of 4 stones is a losing position if both players play optimally.
- The key insight is that by controlling the remainder of the total number of stones modulo 4, you can determine the outcome without simulating the entire game.
- This approach demonstrates how understanding the underlying structure of a game (in this case, the invariance of multiples of 4) can lead to a concise and efficient solution.