import logging

logging.basicConfig(level=logging.DEBUG)

dane =[10,20,30]
for liczba in dane:
    logging.debug(f"sprawdzana liczba: {liczba}")
    wynik = liczba * 2
    logging.info(f"wynik: {wynik}")
    logging.debug("zakonczono iterację")