from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)
app.secret_key = 'bigsecrets'

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def read():
    users = User.get_all_users()
    return render_template('read.html', users = users)

@app.route('/process', methods=['POST'])
def process():
    User.create_user(request.form)
    return redirect('/')

@app.route('/users/create')
def create_user():
    return render_template('form.html', name=request.form)

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    data = {
        'id': user_id
    }
    User.delete_user(data)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)