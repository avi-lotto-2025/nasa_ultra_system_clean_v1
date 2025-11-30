class PackageEngine:

    def pack(self, forecast):
        text = "תחזית ראשית:\n"
        text += f"{forecast['primary']['main']}  (+{forecast['primary']['extra']})\n\n"

        text += "סטי גיבוי:\n"
        for i, b in enumerate(forecast["backups"], 1):
            text += f"{i}) {b['main']} (+{b['extra']})\n"

        return text
