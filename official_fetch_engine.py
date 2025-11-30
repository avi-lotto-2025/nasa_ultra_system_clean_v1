import requests
from bs4 import BeautifulSoup

class OfficialFetcher:

    def fetch_latest(self):
        url = "https://www.pais.co.il/lotto/lottoresults.aspx"

        try:
            r = requests.get(url, timeout=8)
            if r.status_code != 200:
                return None

            soup = BeautifulSoup(r.text, "html.parser")

            main_nums = soup.select("span.ball")
            bonus = soup.select_one("span.strong")

            if not main_nums or not bonus:
                return None

            main = [int(n.text.strip()) for n in main_nums[:6]]
            extra = int(bonus.text.strip())

            if any(n < 1 or n > 37 for n in main):
                return None
            if extra < 1 or extra > 7:
                return None

            return {"main": main, "extra": extra}

        except:
            return None
