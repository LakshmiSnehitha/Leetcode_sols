# Last updated: 9/3/2025, 11:24:23 AM
import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents: int) -> float:
        # Function to calculate the gain of adding one student
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t

        # Create a max-heap with (-gain, pass, total)
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        # Assign extra students
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        # Compute final average
        total_ratio = sum(p / t for _, p, t in heap)
        return total_ratio / len(classes)
