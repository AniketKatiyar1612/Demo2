import random
import string
from datetime import datetime, timedelta

class Task:
    def __init__(self, title, priority, due_date):
        self.id = self.generate_id()
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def generate_id(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{self.id}] {self.title} | Priority: {self.priority} | Due: {self.due_date.date()} | {status}"


