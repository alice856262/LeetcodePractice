# Given two arrays of strings list1 and list2, find the common strings with the 
# least index sum. 
# 
#  A common string is a string that appeared in both list1 and list2. 
# 
#  A common string with the least index sum is a common string such that if it 
# appeared at list1[i] and list2[j] then i + j should be the minimum value among 
# all the other common strings. 
# 
#  Return all the common strings with the least index sum. Return the answer in 
# any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = [
# "Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only common string is "Shogun".
#  
# 
#  Example 2: 
# 
#  
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = [
# "KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The common string with the least index sum is "Shogun" with 
# index sum = (0 + 1) = 1.
#  
# 
#  Example 3: 
# 
#  
# Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
# Output: ["sad","happy"]
# Explanation: There are three common strings:
# "happy" with index sum = (0 + 1) = 1.
# "sad" with index sum = (1 + 0) = 1.
# "good" with index sum = (2 + 2) = 4.
# The strings with the least index sum are "sad" and "happy".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= list1.length, list2.length <= 1000 
#  1 <= list1[i].length, list2[i].length <= 30 
#  list1[i] and list2[i] consist of spaces ' ' and English letters. 
#  All the strings of list1 are unique. 
#  All the strings of list2 are unique. 
#  There is at least a common string between list1 and list2. 
#  
# 
#  Related Topics Array Hash Table String 👍 2019 👎 410


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ### 1. Dictionary Lookup Approach
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Create a mapping from each string in list1 to its index
        index_map = {s: i for i, s in enumerate(list1)}
        min_sum = float('inf')
        result = []

        # Iterate over list2 and check for common strings
        for j, s in enumerate(list2):
            if s in index_map:
                # Calculate the sum of indices for the common string
                i = index_map[s]
                idx_sum = i + j
                # If a smaller index sum is found, update min_sum and reset result list
                if idx_sum < min_sum:
                    min_sum = idx_sum
                    result = [s]
                # If the same index sum is found, add the string to the result list
                elif idx_sum == min_sum:
                    result.append(s)

        return result

    ### 2. Nested Loop Approach
    # def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    #     common = {}
    #     for i in range(len(list1)):
    #         for j in range(len(list2)):
    #             if list1[i] == list2[j]:
    #                 common[list1[i]] = i + j
    #
    #     min_sum = float('inf')
    #     for key, value in common.items():
    #         min_sum = min(min_sum, value)
    #
    #     return [key for key, value in common.items() if value == min_sum]
# leetcode submit region end(Prohibit modification and deletion)
