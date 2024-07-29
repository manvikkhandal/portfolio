from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')   #http://127.0.0.1:5000  
def homee():                                    
     return render_template('homee.html')

@app.route('/aboutp')   
def aboutp():                                   
     return render_template('aboutp.html')

@app.route('/contactp')   
def contactp():                                   
     return render_template('contactp.html')

@app.route('/pf')   
def pf():                                   
     return render_template('pf.html')

@app.route('/learnmore')   
def learnmore():                                   
     return render_template('learnmore.html')

@app.route('/github')   
def github():                                   
     return render_template('github.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)