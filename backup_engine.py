class BackupEngine:

    def __init__(self, prediction_engine):
        self.prediction = prediction_engine

    def generate_backups(self, count):
        return [self.prediction.generate() for _ in range(count)]
