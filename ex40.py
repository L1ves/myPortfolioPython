class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
happy_bday = Song(["He могу я тебе в день рождения",
                                " Дорогие подарки дарить,",
                                " Но зато в эти ночи весенние"])
bulls_on_parade = Song(["Далеко-далеко на лугу пасется кто?",
                            "Пейте, дети, молоко, будете здоровы!"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

class Skorogovrki(object):
    def __init__(self,forkids):
        self.forkids = forkids
    def tell_me(self):
        for skorogovor in self.forkids:
            print(skorogovor)
na_dvore_trava = Skorogovrki(["\nНа дворе трава, на траве дрова",
                                "Не руби дрова на траве двора."])
karl_u_klari = Skorogovrki(["\nКарл у Клары украл кораллы",
                            "Клара у Карла украла кларнет."])
korabli_lavirovali = Skorogovrki(["\nКорабли лавировали, лавировали, да не вылавировали."])

na_dvore_trava.tell_me()
karl_u_klari.tell_me()
korabli_lavirovali.tell_me()
