class StatsEngine:

    def __init__(self, history):
        self.history = history
        self.counts = self._count_numbers()
        self.bonus_counts = self._count_bonus()

    def _count_numbers(self):
        freq = {}
        for draw in self.history:
            for n in draw["main"]:
                if 1 <= n <= 37:
                    freq[n] = freq.get(n, 0) + 1
        return freq

    def _count_bonus(self):
        freq = {}
        for draw in self.history:
            b = draw["extra"]
            if 1 <= b <= 7:
                freq[b] = freq.get(b, 0) + 1
        return freq

    def get_weighted_numbers(self):
        if not self.counts:
            return {}

        max_hits = max(self.counts.values())
        weighted = {}

        for num, count in self.counts.items():
            w = (count / max_hits) + (0.1 if 10 <= num <= 30 else 0.05)
            weighted[num] = w

        return weighted

    def get_pattern_distribution(self):
        avg = sum(self.counts.values()) / len(self.counts)

        hot = [n for n, c in self.counts.items() if c > avg * 1.15]
        cold = [n for n, c in self.counts.items() if c < avg * 0.85]
        mid = [n for n, c in self.counts.items() if n not in hot and n not in cold]

        return {"hot": hot, "cold": cold, "mid": mid}

    def get_smart_bonus(self, primary):
        sorted_bonus = sorted(self.bonus_counts.items(), key=lambda x: x[1])
        for b, _ in sorted_bonus:
            if b not in primary and 1 <= b <= 7:
                return b
        return 1
