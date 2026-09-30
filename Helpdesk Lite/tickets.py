from validators import validate_priority, validate_status

class Ticket:

    def __init__(self, id, user_id, description, status="open", priority="medium", created_at=None, closed_at=None, user_name="", department=""):
        self.id = id
        self.user_id = user_id
        self.description = description
        self.status = validate_status(status)
        self.priority = validate_priority(priority)
        self.created_at = created_at
        self.closed_at = closed_at
        self.user_name = user_name
        self.department = department

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            user_id=data.get("user_id"),
            description=data.get("description"),
            status=data.get("status", "open"),
            priority=data.get("priority", "medium"),
            created_at=data.get("created_at"),
            closed_at=data.get("closed_at"),
            user_name=data.get("user_name", ""),
            department=data.get("department", "")
        )