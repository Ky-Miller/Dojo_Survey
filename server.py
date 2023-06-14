from flask import Flask, render_template,request,redirect,session
app = Flask(__name__)
app.secret_key='secret key'

@app.route('/')
def dojo_form():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def form():
        print(request.form)
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['gender'] = request.form['gender']
        session['text'] = request.form['text']
        return redirect('/result')

@app.route('/result')
def dojo_show():
        return render_template('index1.html')

if __name__=="__main__":
    app.run(debug=True)