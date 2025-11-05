import typer
from rich import print
from typing import Optional

from database import Task    # type: ignore
from database import init_db # type: ignore

app = typer.Typer()

@app.command()
def add(entry: str, prio: Optional[str] = None):
  print(f"Added todo '{entry}' to list with prio {prio}")
  entry = Task(entry)

@app.command()
def list(done: bool = False):
  pass

@app.command()
def remove():
  pass

@app.command()
def marked_done():
  pass

if __name__ == "__main__":
  init_db()
  app()


