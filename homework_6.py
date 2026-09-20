class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки! "

    def earn(self):
        return "Заработал 500 донатов за 2 часа "

class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца! "

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки! "

class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб... "

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз "


class GlowStreamer(Streamer, Mutant):
    def ultimate_content(self):
        return (self.live() + self.earn() + self.superpower())

class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
        return self.live() + self.viral() + self.superpower()

class DonateMage(Streamer, TikToker):
    def ultimate_content(self):
        return self.live() + self.earn() + self.viral()

glow_streamer = GlowStreamer()
viral_cyborg = ViralCyborg()
donate_mage = DonateMage()

print(GlowStreamer.mro())
print(ViralCyborg.mro())
print(DonateMage.mro())
print()
print(glow_streamer.live())
print(viral_cyborg.live())
print(donate_mage.live())
print()
print(glow_streamer.ultimate_content())
print(viral_cyborg.ultimate_content())
print(donate_mage.ultimate_content())