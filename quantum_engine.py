import random

class QuantumEngine:

    def enhance(self, nums):
        nums = set(nums)

        if random.random() < 0.25:
            nums.add(random.randint(1, 37))

        nums = sorted(list(nums))

        while len(nums) > 6:
            nums.pop()

        while len(nums) < 6:
            candidate = random.randint(1, 37)
            if candidate not in nums:
                nums.append(candidate)

        return sorted(nums)
