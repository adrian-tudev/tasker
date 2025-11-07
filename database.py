import sqlite3
from models import Task, Prio
from rich import print

DB_PATH = '.todo.db'

def init_db():
  with sqlite3.connect(DB_PATH) as conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    prio INTEGER NOT NULL,
    archived INTEGER DEFAULT 0
    )""")

def add_task(task: Task):
  with sqlite3.connect(DB_PATH) as conn:
    conn.execute("""
        INSERT INTO tasks (task, prio, archived)
        VALUES (?, ?, ?)
    """, (task.task, int(task.prio), int(task.archived)))

def remove_task(task_id: int):
  with sqlite3.connect(DB_PATH) as conn:
    conn.execute("DELETE FROM tasks where id=?", (task_id,))

def print_all_tasks(show_archived: bool = False):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, task, prio, archived FROM tasks")

        items = cur.fetchall()
        if len(items) == 0:
          print("Nothing to do!")
        for id, task_name, prio, archived in items:
            if show_archived and not archived:
                continue

            priority: Prio = Prio(prio)
            sign: str = '🟨'
            match priority:
                case Prio.LOW:
                    sign = '🟩'
                case Prio.MEDIUM:
                    sign = '🟨'
                case Prio.HIGH:
                    sign = '🟥'

            print(f"{id}: [{priority.name}{sign}] '{task_name}' " + ("✅" if show_archived and archived else ""))

