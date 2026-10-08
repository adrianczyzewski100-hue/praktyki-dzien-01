import logging
logging.basicConfig(level=logging.INFO)
def utworz_zgloszenie(tytul_zgloszenia):
    if not tytul_zgloszenia or not tytul_zgloszenia.strip():
        logging.warning("proba utworzenia zgloszenia z pustym tytulem")
        return None

    logging.info(f"utworzono nowe zgłoszenie: {tytul_zgloszenia}")
    return {"tytul": tytul_zgloszenia, "status": "nowe"}