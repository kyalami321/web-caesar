from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
       <form action="/encrypt" method="POST">
        Rotate by:<br>
        <input type="text" name="rot" value={0}><br>
        Text:<br>
        <input type="textarea" name="text" value={1}><br>
        <input type="submit" value="Submit Query">
    </form>
    {2}
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("","","")

@app.route('/encrypt', methods=['POST'])
def encrypt():    
    encryptStr = request.form['text']
    rot = int(request.form['rot'])
    encryptStr = rotate_string(encryptStr, rot)
    
    showString = ""
    showString += "<h1>" + encryptStr + "</h1>"
    
    return form.format(rot,encryptStr,showString)

app.run()