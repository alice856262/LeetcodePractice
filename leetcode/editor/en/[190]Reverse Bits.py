# Reverse bits of a given 32 bits unsigned integer. 
# 
#  Note: 
# 
#  
#  Note that in some languages, such as Java, there is no unsigned integer type.
#  In this case, both input and output will be given as a signed integer type. 
# They should not affect your implementation, as the integer's internal binary 
# representation is the same, whether it is signed or unsigned. 
#  In Java, the compiler represents the signed integers using 2's complement 
# notation. Therefore, in Example 2 above, the input represents the signed integer -3
#  and the output represents the signed integer -1073741825. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 
# represents the unsigned integer 43261596, so return 964176192 which its binary 
# representation is 00111001011110000010100101000000.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 
# represents the unsigned integer 4294967293, so return 3221225471 which its binary 
# representation is 10111111111111111111111111111111.
#  
# 
#  
#  Constraints: 
# 
#  
#  The input must be a binary string of length 32 
#  
# 
#  
#  Follow up: If this function is called many times, how would you optimize it? 
# 
# 
#  Related Topics Divide and Conquer Bit Manipulation 👍 5269 👎 1533


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Bitwise Manipulation
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):  # Process 32 bits
            # Extract the least significant bit
            bit = n & 1
            # Shift the bit to its reversed position and add to result
            result = (result << 1) | bit
            # Shift n to process the next bit
            n >>= 1
        return result

    ### 2. String-Based Reversal
    # def reverseBits(self, n: int) -> int:
    #     bits = int(str(n))
    #     reverse_bits = ''
    #     for i in range(32):
    #         if bits > 0:
    #             remainder = str(bits % 2)
    #             bits = bits // 2
    #             reverse_bits += remainder
    #         else:
    #             reverse_bits += '0'
    #
    #     reverse_bits = reverse_bits[::-1]
    #     reverse = 0
    #     for i in range(31, -1, -1):
    #         reverse += int(reverse_bits[i]) * (2 ** i)
    #
    #     return reverse
# leetcode submit region end(Prohibit modification and deletion)
