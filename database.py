from enum import Enum
import sqlite3
from pathlib import Path
from dataclasses import dataclass

DB_PATH = '.todo.db'

class Prio(Enum):
  HIGH = 1
  MEDIUM = 2
  LOW = 3

@dataclass
class Task:
    task: str
    prio: Prio = Prio.MEDIUM
    archived: bool = False

def init_db():
  with sqlite3.connect(DB_PATH) as con:
    con.execute("""
      CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        prio TEXT NOT NULL,
        archived INTEGER DEFAULT 0
    )""")

