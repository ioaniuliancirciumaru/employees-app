from flask import Flask, render_template, request, redirect, url_for, flash
import queries

app = Flask(__name__)


@app.route('/')
def index():
    data = queries.data()
    return render_template("index.html", data=data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        queries.insert(name, email, phone)
        flash("Employee inserted successfully")
        return redirect(url_for('index'))

@app.route('/edit/<id>', methods= ['GET', 'POST'])
def edit(id):
    # if request.method == 'GET':
    #     data = queries.get_by_id(id)
    #     return render_template('index.html')
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        queries.edit(id,name,email,phone)
        return redirect(url_for('index'))

@app.route('/delete/<id>', methods = ['GET', 'POST'])
def delete(id):
    queries.delete_user(id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)