## Algorithm Description
### Key Idea
- Determine whether the poison effect from an attack is fully effective or partially cut short by the next attack, and adjust the poisoned duration accordingly.
- Sum the effective poisoned duration from each attack interval, and finally add the full duration for the last attack.

### Step-by-Step Algorithm
- Step 1: Initialize a variable ```total``` to keep track of the cumulative poisoned time.
- Step 2: If the number of attacks in ```timeSeries``` is less than ```2```, return ```duration``` immediately, since there is only one attack.
- Step 3: Iterate over ```timeSeries```:
  - For each attack at index ```i```, check if the poison effect (lasting ```duration``` seconds) ends before the next attack begins.
  - If ```timeSeries[i] + duration - 1 < timeSeries[i + 1]```, the full duration is effective, so add ```duration``` to ```total```.
  - Otherwise, the poison effect is cut short by the next attack, so add the gap between the current and next attack (```timeSeries[i + 1] - timeSeries[i]```) to ```total```.
- Step 4: After the loop, add the full ```duration``` for the last attack (since it is always fully effective).

## Algorithmic Complexity
- Time Complexity: O(n)
  - The algorithm processes each attack in the ```timeSeries``` once.
- Space Complexity: O(1)
  - Only a constant amount of extra space is used.

## Notes on Solving Process
- By comparing the ending time of the poison effect of the current attack with the start time of the next, the algorithm accurately calculates the effective poisoned duration for each interval.
- The final addition of the full duration for the last attack ensures that the last attack's effect is fully captured.