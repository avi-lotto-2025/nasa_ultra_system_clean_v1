from prediction_engine import PredictionEngine
from stats_engine import StatsEngine
from quantum_engine import QuantumEngine
from kira_engine import KiraEngine
from backup_engine import BackupEngine
from email_engine import EmailEngine
from auto_heal import AutoHealEngine
from package_engine import PackageEngine
from history_loader import HistoryLoader

from datetime import datetime

class EngineMaster:

    def __init__(self):
        self.history = HistoryLoader().load()
        self.stats = StatsEngine(self.history)
        self.quantum = QuantumEngine()
        self.kira = KiraEngine()
        self.prediction = PredictionEngine(
            self.history, self.stats, self.quantum, self.kira
        )
        self.backup = BackupEngine(self.prediction)
        self.mailer = EmailEngine()
        self.packager = PackageEngine()
        self.healer = AutoHealEngine()

    def generate_full(self):
        primary = self.prediction.generate()
        backups = self.backup.generate_backups(5)

        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "primary": primary,
            "backups": backups
        }

    def send_email(self, forecast):
        body = self.packager.pack(forecast)
        return self.mailer.send("NASA ULTRA FORECAST", body)

    def health(self):
        return self.healer.check()
