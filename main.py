from flask import Flask, request, render_template
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('form.html')

@app.route("/", methods=['POST'])
def encrypt():
    rot_number = int(cgi.escape(request.form['rot']))
    input_text = request.form['text']
    input_text = cgi.escape(input_text)
    encrypted_text = ''
    encrypted_text += rotate_string(input_text, rot_number)

    return render_template('form.html', text = encrypted_text)

app.run()