# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('Chart.html')

if __name__ == '__main__':
    app.run()
