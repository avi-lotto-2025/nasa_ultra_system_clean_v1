import random
from datetime import datetime

class PredictionEngine:

    def __init__(self, history, stats, quantum, kira):
        self.history = history
        self.stats = stats
        self.quantum = quantum
        self.kira = kira

    def generate(self):
        weighted = self.stats.get_weighted_numbers()
        patterns = self.stats.get_pattern_distribution()
        mc = self._monte_carlo(weighted)
        q = self.quantum.enhance(mc)
        final = self.kira.balance(q, patterns)
        bonus = self.stats.get_smart_bonus(final)

        return {
            "main": final,
            "extra": bonus,
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def _monte_carlo(self, weighted):
        freq = {}
        for _ in range(1500):
            picked = random.choices(
                population=list(weighted.keys()),
                weights=list(weighted.values()),
                k=6
            )
            for n in picked:
                freq[n] = freq.get(n, 0) + 1

        sorted_nums = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        nums = [n for n, _ in sorted_nums[:6]]

        return sorted([min(max(n, 1), 37) for n in nums])
