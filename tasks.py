import json
from datetime import datetime

class TaskManager:
  def __init__(self):
    self.file_path="C:/Users/Home/Desktop/Task Manager/tasks.json"
  
  # 1. Read file
  def read_tasks(self):
    try:
      with open(self.file_path,"r") as f:
        return json.load(f)
    except Exception as e:
      return []
    
  # 2. Write file
  def write_tasks(self,tasks):
    with open(self.file_path,"w") as f:
      json.dump(tasks,f,indent=4)
      
  # ------------------------ ADD TASK ----------------------------
      
  def add_tasks(self):
    tasks=self.read_tasks()
    
    task=input("Add task: ")
    
    # generate id
    if tasks:
        new_id = tasks[-1]["id"] + 1
    else:
      new_id=1
      
    new_task={
      "id":new_id,
      "task":task,
      "done":False,
      "created_at":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    tasks.append(new_task)
    
    self.write_tasks(tasks)
    
  # ------------------------ VIEW TASK ----------------------------
    
  def view_tasks(self):
    tasks=self.read_tasks() 

    if not tasks:
      print("No Task Found")
      return
  
    # show task
    for task in tasks:
      status="Done" if task["done"] else "Not Done"      
      print(f"{task['id']}. {task['task']} - {status} ({task['created_at']}) ")
      
  # ------------------------ MARK TASK ----------------------------
    
  def mark_tasks(self):
    tasks=self.read_tasks()
    
    if not tasks:
      print("No Task Found")
      return
    
    # show task
    for task in tasks:
      status="Done" if task["done"] else "Not Done"
      print(f"{task['id']}. {task['task']} - {status}")
      
    try:
      task_id = int(input("\nEnter task ID you want to marked: "))
      
      for task in tasks:
        if task['id'] == task_id:
          
          if task["done"]:
            print("Task already completed ⚠️")
            return
          
          task["done"]=True
          self.write_tasks(tasks)
          print(f"Task marked as done ✅")
          return
      print("No Task id match...")
          
    except:
      print("Invalid input")
      
      
   # ------------------------ DELETE TASK ----------------------------
    
  def delete_tasks(self):
    tasks=self.read_tasks()
    
    if not tasks:
      print("No Task Found")
      return
    
    # show task
    for task in tasks:
      status="Done" if task["done"] else "Not Done"
      print(f"{task['id']}. {task['task']} - {status}")
      
    try:
      task_id=int(input("\nEnter task id you want to delete: "))
      
      for task in tasks:
        if task['id'] == task_id:
          tasks.remove(task)
          self.write_tasks(tasks)
          print("Task id deleted ❌")
          return
      print("No Task id match...")
      
    except:
      print("Invalid input")
      
  # ------------------------ EDIT TASK ----------------------------
    
  def edit_tasks(self):
    tasks=self.read_tasks()
    
    if not tasks:
      print("No Task found")
      return
    
    # show task
    for task in tasks:
      status = "Done" if task["done"] else "Not Done"
      print(f"{task['id']}. {task['task']} - {status}")
      
    try:
      task_id=int(input("\nEnter task id you want to edit: "))
      for task in tasks:
        if task["id"] == task_id:
          new_task=input("Enter new task: ")
          task['task']=new_task
          self.write_tasks(tasks)
          print("Task updated ✏️")
          return
      print("No Task id found")
    except:
      print("Invalid input")
      
  # ------------------------ FILTER TASK ----------------------------
    
  def filter_tasks(self):
    tasks=self.read_tasks()
    
    if not tasks:
      print("No Task found")
      return
    
    print("\n1. Show Completed Task")
    print("2. Show Pending Task")
    
    try:
      choice=int(input("\nEnter choice to filter task: "))
      
      if choice==1:
        filtered = [t for t in tasks if t["done"]]
      elif choice==2:
        filtered = [t for t in tasks if not t["done"]]
      else:
        print("Invalid choice")
        return
      
      if not filtered:
        print("No matching task...")
        return
        
      for task in filtered:
        status="Done" if task["done"] else "Not Done"
        print(f"{task['id']}. {task['task']} - {status}")
    except:
      print("Invalid input")
      
   # ------------------------ SEARCH TASK ----------------------------
    
  def search_tasks(self):
    tasks=self.read_tasks()
    
    if not tasks:
      print("No Task found")
      return
    
    # show task
    for task in tasks:
      status = "Done" if task["done"] else "Not Done"
      print(f"{task['id']}. {task['task']} - {status}")
    
    try:  
      keyword=input("\nEnter keyword you want to search: ").lower()
      
      results = [t for t in tasks if keyword in t['task'].lower()]
      
      if not results:
        print("No Match Found...")
        return
      
      for task in results:
        status="Done" if task['done'] else "Not Done"
        print(f"{task['id']}. {task['task']} - {status}")
        
    except:
      print("Invalid input")
  
if __name__=="__main__":
  t1=TaskManager()

  while True:
    print("\n1. Add Tasks")
    print("2. View Tasks")
    print("3. Mark Tasks")
    print("4. Delete Tasks")
    print("5. Edit Tasks")
    print("6. Filter Tasks")
    print("7. Search Tasks")
    print("8. Exit")
  
    try:
      choice=int(input("\nEnter your choice: "))
    except:
      print("Invalid input")
      continue
  
    if choice==1:
      t1.add_tasks()
    elif choice==2:
      t1.view_tasks()
    elif choice==3:
      t1.mark_tasks()
    elif choice==4:
      t1.delete_tasks()
    elif choice==5:
      t1.edit_tasks()
    elif choice==6:
      t1.filter_tasks()
    elif choice==7:
      t1.search_tasks()
    elif choice==8:
      exit()
    else:
      print("Invalid choice")
    
