from flask import Flask
from helpdesk import Helpdesk
from database import DatabaseError

app = Flask(__name__)
helpdesk = Helpdesk()

@app.route("/")
def home():
    return "<h1>Helpdesk Lite Web v0.7</h1>"

@app.route("/tickets")
def list_tickets():
    try:
        tickets = helpdesk.get_all_tickets()
        if not tickets:
            return "<h1>Helpdesk Lite</h1><p>brak zgłoszeń w bazie.</p>"

        rows = ""
        for t in tickets:
            rows += f"""
            <tr>
                <td>{t['id']}</td>
                <td>{t['user_name']}</td>
                <td>{t['department']}</td>
                <td>{t['priority']}</td>
                <td>{t['status']}</td>
                <td>{t['description']}</td>
                <td>{t['created_at']}</td>
            </tr>
            """

        html = f"""
        <h1>Lista zgłoszeń</h1>
        <table border="1" cellpadding="6" cellspacing="0">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Użytkownik</th>
                    <th>Dział</th>
                    <th>Priorytet</th>
                    <th>Status</th>
                    <th>Opis</th>
                    <th>Data utworzenia</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
        """
        return html
    except DatabaseError:
        return "<h1>Błąd bazy danych</h1><p>szczegóły zostały zapisane w logu.</p>", 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)