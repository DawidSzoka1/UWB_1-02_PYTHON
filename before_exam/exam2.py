import pickle


class Logowanie:
    count = 0

    def __init__(self, haslo, login='admin'):
        self._pin = '0000'
        self.login = login
        self.haslo = haslo
        Logowanie.count += 1

    def __str__(self):
        return f"login = {self.login}, haslo = {self.haslo}, pin= {self._pin}"

    def _zmienpin(self, nowypin):
        self._pin = nowypin

    @classmethod
    def amount(cls):
        return cls.count


class LogowanieStudenta(Logowanie):
    def __init__(self, login, imie, nazwisko):
        super().__init__(haslo=None, login=login)
        self.imie = imie
        self.nazwisko = nazwisko

    def zmiendane(self, login, haslo, imie, nazwisko):
        """
            
        Args:
            login:
            haslo:
            imie:
            nazwisko:

        Returns:

        """
        self.imie = imie
        self.nazwisko = nazwisko
        self.login = login
        self.haslo = haslo
        with open("data.pkl", 'wb') as f:
            pickle.dump(f"{imie}, {nazwisko}, {haslo}", f)

