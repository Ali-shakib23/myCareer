from time import strftime
from flask import Flask, render_template, request, redirect, url_for

import datetime
app = Flask(__name__)

from jobs.routes import jobs_bp
app.register_blueprint(jobs_bp)

app.secret_key = "this_is_my_random_key"  
@app.route('/')
def home():
    return redirect(url_for('jobs.list_jobs'))

if __name__ == "__main__":
    app.run(debug=True)
