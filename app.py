from flask import Flask, render_template, request, redirect
import database

app=Flask(__name__)

# create db when app starts
database.create_table()

# ----> HOME ROUTE (show task)
@app.route('/')
def index():
  filter_type=request.args.get('filter','all')
  
  if filter_type == 'completed':
    tasks=database.get_completed_task()
  elif filter_type == 'pending':
    tasks=database.get_pending_task()
  else:
    tasks=database.get_data()
    
  total,completed,remaining=database.count_task()
  
  return render_template("index.html",tasks=tasks,total=total,completed=completed,remaining=remaining)


# ----> ADD TASK
@app.route('/add',methods=["POST"])
def add():
  title=request.form.get('title')
  database.add_task(title)
  return redirect('/')


# ----> DELETE TASK
@app.route('/delete/<int:id>')
def delete(id):
  database.delete_task(id)
  return redirect('/')


# ----> MARK TASK
@app.route('/toggle/<int:id>')
def toggle(id):
  database.toggle_task(id)
  return redirect('/')


# ----> EDIT TASK
@app.route('/edit/<int:id>')
def edit(id):
  tasks=database.get_data()
  task=None
  for t in tasks:
    if t[0]==id:
      task=t
      break

  return render_template("edit.html",task=task)


# ----> UPDATE TASK
@app.route('/update/<int:id>',methods=["POST"])
def update(id):
  new_task=request.form['title']
  database.update_task(id,new_task)
  return redirect('/')

if __name__=="__main__":
  app.run(debug=True)