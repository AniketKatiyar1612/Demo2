import random
import string
from datetime import datetime, timedelta


# class TaskManager:
#     def __init__(self):
#         self.tasks = []

#     def create_random_task(self):
#         titles = ["Write report", "Fix bug", "Email client", "Database backup", "Update docs"]
#         priority = random.choice(["Low", "Medium", "High"])
#         due = datetime.now() + timedelta(days=random.randint(1, 10))
#         task = Task(random.choice(titles), priority, due)
#         self.tasks.append(task)

#     def generate_tasks(self, n=10):
#         for _ in range(n):
#             self.create_random_task()

