from flask import Flask, request
from caesar import rotate_string
import cgi

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
      <form action="/" method="POST">
        <label for="rotate-by">Rotate by:
            <input id="rotate-by" type="text" name="rot" value="0"/>
        </label>
            <textarea input id="textarea" type="textarea" name="text">{0}</textarea>
        <input type="submit" />
      </form>
    </body>
</html>

"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot_number = int(cgi.escape(request.form['rot']))
    input_text = request.form['text']
    input_text = cgi.escape(input_text)
    encrypted_text = ''
    encrypted_text += rotate_string(input_text, rot_number)

    return form.format(encrypted_text)

app.run()