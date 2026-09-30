# Dokumentacja bazy danych Helpdesk Lite

Baza danych: `helpdesk.db` (SQLite3)

## Tabela: `tickets`

Przechowuje informacje o zgłoszeniach serwisowych.

### Kolumny:
- `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT): Unikalny identyfikator wpisu.
- `user` (TEXT, NOT NULL): Nazwa użytkownika zgłaszającego problem.
- `description` (TEXT, NOT NULL): Treść zgłoszenia.
- `status` (TEXT, NOT NULL, DEFAULT 'open'): Stan zgłoszenia (`open`, `closed`).
- `priority` (TEXT, NOT NULL, DEFAULT 'medium'): Priorytet (`low`, `medium`, `high`).
- `created_at` (TEXT, NOT NULL, DEFAULT CURRENT_TIMESTAMP): Data dodania zgłoszenia.
- `closed_at` (TEXT, NULL): Data zamknięcia zgłoszenia.