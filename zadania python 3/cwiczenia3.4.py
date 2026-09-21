def get_non_emppty_text(prompt):
    while True:
        text = input(prompt)
        if text.strip():
            return text
        print("Nie podano żadnego tekstu. Spróbuj ponownie.")

get_non_emppty_text("Podaj tekst: ")