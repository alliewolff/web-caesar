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
                background-color: #eeeeee;
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
        <form action="/" method="post">
            <label> Rotate by: </label>
            <input type="text" name="rot" value="0"/>
            <textarea class="text" name="text">{0}</textarea>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rotation = request.form['rot']
    text_input = request.form['text']
    x = int(rotation)
    y = str(text_input)
    new_text = rotate_string(y, x)
    #final = '<h1>' + new_text + '</h1>'
    return form.format(new_text)

#@app.route("/rotate", methods=['POST'])
#def rotate_pages():
    #encrypted = encrypt(form)
    #
    #return final

app.run()