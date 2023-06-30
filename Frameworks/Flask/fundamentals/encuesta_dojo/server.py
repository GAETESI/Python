from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__) 
app.secret_key="Clave secreta"
  
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process',methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    if name and language:
        session['name'] = name
        session['location'] = location
        session['language'] = language
        session['comments'] = request.form['comments']
        return redirect('/success')
    else:
        if not name:
            flash('Please enter a name.')
        if not location:
            flash('Please enter a location.')
        if not language:
            flash('Please enter a language.')
        return render_template("index.html")

@app.route('/success')
def success():
    return render_template("success.html")
    
if __name__=="__main__":
    app.run(debug=True)

