from flask import Flask, render_template, redirect, session

app = Flask(__name__)   
app.secret_key = "esto es secreto"

@app.route('/contador')          
def contador_flask():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 0
    return render_template ("index.html")  

@app.route('/incrementar', methods=['POST'])
def increment():
    counter = session.get('counter', 0)
    counter += 1
    session['counter'] = counter
    return redirect('/contador')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect('/contador')
    
if __name__=="__main__":
    app.run(debug=True)