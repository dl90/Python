from abc import ABCMeta, abstractmethod


class AbstractArt(metaclass=ABCMeta):
    isArt = False

    def __init__(self, color, medium):
        self.color = color
        self.medium = medium
        print("AbstractArt instantiated...")

    @classmethod
    def is_art(cls):
        return (f"Is this abstract art art? {cls.isArt}!")

    def change_medium(self, value):
        self.medium = value
        print("AbstractArt medium changed")

    @abstractmethod
    def sale_price(self):
        print("AbstractArt sale_price called")
        pass


class ModernArt(AbstractArt):
    modern = True

    def __init__(self, color, medium, price, artist):
        super().__init__(color, medium)
        self.price = price
        self.artist = artist
        print("ModernArt instianted...")

    def sale_price(self):
        super().sale_price()
        return self.price * 20

    @classmethod
    def is_modern_art(cls):
        return(f"Is modern art art? {cls.modern}, but still... {cls.is_art()}\n")


new_art = ModernArt("BLACKEST BLACK", "Graffiti", 1000000, "NoName")
print(new_art.is_art(), "\n")

x = new_art.sale_price()
print(x, "\n")

print(new_art.medium)
new_art.change_medium("Air")
print(new_art.medium, "\n")

print(new_art.is_modern_art())
