class KiraEngine:

    def balance(self, nums, patterns):
        nums = sorted(nums)
        nums = [min(max(n, 1), 37) for n in nums]

        hot = patterns["hot"]

        if sum(1 for n in nums if n in hot) > 4:
            candidates = patterns["mid"] or patterns["cold"]
            if candidates:
                nums[-1] = candidates[0]

        nums = sorted(list(set(nums)))
        while len(nums) < 6:
            nums.append(nums[-1] + 1)

        return sorted([min(max(n, 1), 37) for n in nums])
