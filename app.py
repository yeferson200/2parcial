from flask import Flask, render_template, request, redirect, flash
from controllers import users

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



@app.get('/')
def parcial():
    return render_template('parcial.html')

app.run(debug=True)