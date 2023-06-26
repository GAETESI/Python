from flask import Flask  
app = Flask(__name__)    
@app.route('/')        
def hola_mundo():
    return 'Hola Mundo!' 

@app.route('/Dojo')        
def dojo():
    return 'Dojo!' 

@app.route('/say/<name>')        
def hola(name):
    try:
        return f"Hola {name}" 
    except ValueError:
        print("Lo siento! No hay respuesta. Inténtalo otra vez.")


@app.route('/say/<int:num>/<string:name>')
def repeat(num, name):
    try:
        return f"{num * name}"
    except ValueError:
        print("Lo siento! No hay respuesta. Inténtalo otra vez.")
       
if __name__=="__main__":       
    app.run(debug=True) 
    
