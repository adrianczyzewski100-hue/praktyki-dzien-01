from flask import Flask, render_template, request, redirect, url_for
from helpdesk import Helpdesk
from database import DatabaseError

# inicjalizacja aplikacji webowej oraz pojedynczej instancji logiki biznesowej
app = Flask(__name__)
helpdesk = Helpdesk()

@app.route("/")
def home():
    # przekierowanie ze strony głównej bezpośrednio do widoku listy zgłoszeń
    return redirect(url_for("list_tickets"))

@app.route("/tickets")
def list_tickets():
    try:
        # pobranie zgłoszeń z bazy przez warstwę logiki (bez bezpośredniego SQL)
        tickets = helpdesk.get_all_tickets()
        return render_template("tickets.html", tickets=tickets)
    except DatabaseError:
        # bezpieczny komunikat dla użytkownika w przypadku awarii bazy
        return "Błąd bazy danych.", 500

@app.route("/tickets/new", methods=["GET", "POST"])
def new_ticket():
    if request.method == "POST":
        # pobranie i oczyszczenie danych z formularza HTTP
        user_id_raw = request.form.get("user_id")
        description = request.form.get("description", "").strip()
        priority = request.form.get("priority", "medium").strip().lower()

        # walidacja obecności wymaganych pól po stronie serwera
        if not user_id_raw or not description:
            users = helpdesk.get_users()
            return render_template("new_ticket.html", users=users, error="Użytkownik i opis są wymagani.")

        try:
            user_id = int(user_id_raw)
            # przekazanie danych do istniejącej metody biznesowej
            helpdesk.add_ticket(user_id, description, priority)
            # wzorzec Post/Redirect/Get chroni przed ponownym wysłaniem danych przy odświeżeniu
            return redirect(url_for("list_tickets"))
        except (ValueError, DatabaseError) as e:
            # ponowne wyrenderowanie formularza z powiadomieniem o błędzie
            users = helpdesk.get_users()
            return render_template("new_ticket.html", users=users, error=str(e))

    # obsługa GET: pobranie listy użytkowników do rozwijanego menu w formularzu
    users = helpdesk.get_users()
    return render_template("new_ticket.html", users=users)

if __name__ == "__main__":
    app.run(debug=True, port=5000)