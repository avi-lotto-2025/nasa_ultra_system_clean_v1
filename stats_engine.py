import random

class StatsEngine:
    def __init__(self, history):
        self.history = history
        self.counts = self._build_counts()

    def _build_counts(self):
        counts = {}
        for draw in self.history:
            for num in draw:
                counts[num] = counts.get(num, 0) + 1
        return counts

    def get_pattern_distribution(self):
        # מנגנון הגנה מלא – לא נופל אף פעם
        if not self.counts or len(self.counts) == 0:
            return {
                "avg": 0,
                "max": 0,
                "min": 0,
                "hot_numbers": [],
                "cold_numbers": []
            }

        total = sum(self.counts.values())
        amount = len(self.counts)

        avg = total / amount
        max_val = max(self.counts.values())
        min_val = min(self.counts.values())

        # ניתוח חם/קר
        hot_numbers = [n for n, c in self.counts.items() if c > avg]
        cold_numbers = [n for n, c in self.counts.items() if c < avg]

        return {
            "avg": avg,
            "max": max_val,
            "min": min_val,
            "hot_numbers": hot_numbers,
            "cold_numbers": cold_numbers
        }
