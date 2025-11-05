import typer
from rich import print
from typing import Optional

import database as db
from models import Task, Prio

app = typer.Typer()

@app.command()
def add(task: str, prio: Optional[str] = None):
  priority: Prio = Prio.MEDIUM
  match prio:
    case "LOW" | "l":
      priority = Prio.LOW
    case "MEDIUM" | "m":
      priority = Prio.MEDIUM
    case "HIGH" | "h":
      priority = Prio.HIGH
    case _:
      print("Not a valid priority! [LOW, MEDIUM, HIGH]")
      return
    
  print(f"Added task '{task}' to list with prio {priority.name}")
  db.add_task(Task(task, priority))

@app.command()
def list(archived: bool = False):
  db.print_all_tasks(archived)

@app.command()
def archive(task_id: int):
    print(f"Archived task {task_id}")

@app.command()
def remove(task_id: int):
  print(f"Removed task {task_id} :(")

if __name__ == "__main__":
  db.init_db()
  app()


