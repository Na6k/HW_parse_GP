from .base import BaseParser


class Book(BaseParser):
    def parse(self):
        container = self.html.select_one(
            "#yDmH0d > c-wiz.SSPGKf.glB9Ve.K1b9Kc > div > div > div.N4FjMb.Z97G4e > c-wiz > div"
        )
        items = container.select(".hP61id")
        for item in items:
            name_box = item.select_one(".Epkrse ")
            price_box = item.select(".VfPpfd ")
            self.date.append(
                {"name": name_box.text, "price": [lesson_box.text for lesson_box in price_box]}
            )


class Games(BaseParser):
    def parse(self):
        container = self.html.select_one(
            "#yDmH0d > c-wiz.SSPGKf.glB9Ve > div > div > div.N4FjMb.Z97G4e > c-wiz > div > c-wiz"
        )
        items = container.select(".cXFu1")
        for item in items:
            name_box = item.select_one(".ubGTjb")
            options_box = item.select(".w2kbF")
            self.date.append(
                {"name": name_box.text, "options": [tool_box.text for tool_box in options_box]}
            )


class Films(BaseParser):
    def parse(self):
        conteiner = self.html.select_one(
            "#yDmH0d > c-wiz.SSPGKf.glB9Ve > div > div > div.N4FjMb.Z97G4e > c-wiz > div > c-wiz"
        )
        items = conteiner.select(".hP61id")
        for item in items:
            name_box = item.select_one(".Epkrse ")
            price_box = item.select(".VfPpfd ")
            self.date.append({"name": name_box.text, "price": [price.text for price in price_box]})
