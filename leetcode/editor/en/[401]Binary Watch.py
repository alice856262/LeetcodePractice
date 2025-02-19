# A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 
# LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or 
# one, with the least significant bit on the right. 
# 
#  
#  For example, the below binary watch reads "4:51". 
#  
# 
#  
# 
#  Given an integer turnedOn which represents the number of LEDs that are 
# currently on (ignoring the PM), return all possible times the watch could represent. 
# You may return the answer in any order. 
# 
#  The hour must not contain a leading zero. 
# 
#  
#  For example, "01:00" is not valid. It should be "1:00". 
#  
# 
#  The minute must consist of two digits and may contain a leading zero. 
# 
#  
#  For example, "10:2" is not valid. It should be "10:02". 
#  
# 
#  
#  Example 1: 
#  Input: turnedOn = 1
# Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00
# "]
#  
#  Example 2: 
#  Input: turnedOn = 9
# Output: []
#  
#  
#  Constraints: 
# 
#  
#  0 <= turnedOn <= 10 
#  
# 
#  Related Topics Backtracking Bit Manipulation 👍 1464 👎 2676


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = []
        # Iterate over all possible hours (0-11)
        for hour in range(12):
            # Iterate over all possible minutes (0-59)
            for minute in range(60):
                # Count the number of 1s in the binary representation of the hour and minute
                if (bin(hour).count("1") + bin(minute).count("1")) == turnedOn:
                    # Format the time string: hour is printed as-is (no leading zero) and minute is formatted with 2 digits (with leading zero if needed)
                    times.append(f"{hour}:{minute:02d}")
        return times
# leetcode submit region end(Prohibit modification and deletion)
