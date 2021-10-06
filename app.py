from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route("/test", methods=["POST"])
def test():
    slider_value = request.form["slider"]

    # Send the data to the new route /test. 
    # Try changing it so it just moves a servo to the desired angle.
    # Make sure to validate degrees between 0 - 180.
       
    templateData ={

        'slider_value': slider_value
    }

    
    return render_template('index.html', **templateData) 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
