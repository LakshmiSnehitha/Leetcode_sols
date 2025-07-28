# Last updated: 7/28/2025, 3:29:26 PM
# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#          freq_map = {}
#          for num in arr:
#             if num in freq_map:
#                 freq_map[num] += 1
#             else:
#                 freq_map[num] = 1
#             frequencies = list(freq_map.values())
#             # return frequencies
#             return len(frequencies) == len(set(arr))

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_map = {}
        for num in arr:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        frequencies = list(freq_map.values())
        # return len(set(frequencies))
        # return len(frequencies)
        return len(frequencies) == len(set(frequencies))
        # return frequencies

        # c={}
        # for i in  arr:
        #     if i in c:
        #         c[i]+=1
        #     else:
        #         c[i]=1
        # s=list(c.values())
        # return len(c)==len(set(c))


        