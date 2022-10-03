from .base import BaseParser

class HW(BaseParser):
    def parse(self):
        container = self._html.select_one("#yDmH0d > c-wiz.SSPGKf.glB9Ve.K1b9Kc > div > div > div.N4FjMb.Z97G4e > c-wiz > div")   
        items = container.select('.hP61id')
        for item in items:
            name_box = item.select_one('.Epkrse ')
            price_box = item.select('.VfPpfd ')
            self._date.append({"name": name_box.text, "price": [lesson_box.text for lesson_box in price_box]})
        