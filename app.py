# render_template --->> show message on screen + send data to HTML
# redirect --->> only takes URL/ does not send data or not contain template name (index.html)

from flask import Flask, render_template, redirect, request
from tasks import TaskManager

app = Flask(__name__)
t1 = TaskManager()


@app.route('/')
def home():
    tasks = t1.read_tasks()
    return render_template("index.html", tasks=tasks)


# ---------------------------------->> Add task
@app.route("/add", methods=["POST"])
def add():
    # request handling
    task_text = request.form.get("task").strip()

    if not task_text:
        return redirect("/")

    # input reading
    tasks = t1.read_tasks()

    for task in tasks:
        if task["task"].lower() == task_text.lower():
            return render_template("index.html", tasks=tasks, msg="Task already exist ⚠")

    if tasks:
        new_id = max(task["id"] for task in tasks)+1
    else:
        new_id = 1

    new_task = {
        "id": new_id,
        "task": task_text,
        "done": False
    }

    tasks.append(new_task)

    t1.write_tasks(tasks)
    return redirect("/")



# ---------------------------------->>  Delete task
@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks = t1.read_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            break

    t1.write_tasks(tasks)
    return redirect("/")



# ---------------------------------->> Mark Task
@app.route('/mark/<int:task_id>')
def mark(task_id):
    tasks = t1.read_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if task["done"]:
                return render_template("index.html", tasks=tasks, msg="Task already done ⚠")
            task["done"] = True
            break
    t1.write_tasks(tasks)
    return redirect('/')

# ---------------------------------->> Edit Task
@app.route('/edit/<int:task_id>')
def edit(task_id):
    tasks = t1.read_tasks()
    for task in tasks:
        if task["id"] == task_id:
                return render_template("edit.html", task=task)
    t1.write_tasks(tasks)
    return redirect('/')

# ---------------------------------->> Update Task
@app.route('/update/<int:task_id>',methods=["POST"])
def update(task_id):
    new_text=request.form.get("task")
    tasks = t1.read_tasks()
    
    for task in tasks:
        if task["id"] == task_id:
            task["task"]=new_text
            break
    t1.write_tasks(tasks)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
