from config import PRIORITIES

def validate_user(user):
    return user.strip() != ""

def validate_description(description):
    return description.strip() != ""

def validate_priority(priority):
    return priority.lower() in PRIORITIES
