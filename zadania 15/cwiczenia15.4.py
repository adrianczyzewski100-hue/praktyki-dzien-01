import logging

logging.basicConfig(level=logging.INFO)

def utworz_zgloszenie(tytul_zgloszenia):
    logging.info(f"utworzono nowe zgłoszenie: {tytul_zgloszenia}")
    return {"tytul": tytul_zgloszenia, "status": "nowe"}