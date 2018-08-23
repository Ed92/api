import requests, todo

def _url(parth):
  return "https://todo.example.com" + path


def get_tasks():
  return requests.get(_url("/tasks/"))

def describe_task(task_id):
  return requests.get(_url("/tasks/{:d}/".format(task_id)))

def add_task(summary, descrption=""):
  return requests.post(_url("/tasks/"), json={
    "summary": summary,
    "description": description,
    })

def task_done(task_id):
  return requests.delete(_url("/tasks/{:d}/".format(task_id)))

def update_task(task_id, summary, descrption):
  url = _url("/tasks/{:d}".format(task_id))
  return requests.put(url, json={
    "summary": summary,
    "descrption": descrption,
    })

resp = todo.get_tasks()
if resp.status_code != 200:
  raise ApiError("Cannot fetch all tasks: {}".format(resp.status_code))
for todo_item in resp.json():
  print("{} {}".format(todo_item["id"], todo_item["summary"]))
