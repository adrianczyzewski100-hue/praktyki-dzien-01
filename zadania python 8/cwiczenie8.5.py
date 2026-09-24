from datetime import datetime
created_at = datetime.now()
text = created_at.isoformat(timespec="seconds")
print(text)