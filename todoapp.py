from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#list to store To Do items
todo_items = []

@app.route('/')
  def index():
    # Display the list of To Do items and the form
    return render_template('index.html', todo_items=todo_items)

@app.route('/submit', methods=['POST'])
def submit():
  
    # Get the data from the form
    email = request.form.get('email')
    task = request.form.get('task')
    priority = request.form.get('priority')

    #validation
    if task and email and priority in ['Low', 'Medium', 'High']:
        todo_items.append({'task': task, 'email': email, 'priority': priority})
    
    #Redirect back to the home page
    return redirect('/')

@app.route('/clear')
def clear():
    # Clear the To Do list
    todo_items.clear()

    # Redirect back to the home page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
