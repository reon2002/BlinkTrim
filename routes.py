from flask import render_template, request, redirect, url_for
from Project import app, db
from Project.models import Url
import random
import string

# Generate a random 8-character code for short URLs
def generate_short_code():
    code = ''.join(random.choice(string.digits) for _ in range(8))
    return code

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Process the submitted URL and generate a short URL
        submitted_url = request.form.get('url')

        # Generate a random 8-digit code for the short URL
        random_code = generate_short_code()

        # Construct the short URL
        short_url = f'short.bt/{random_code}'

        # Store the URL in the database
        url_entry = Url(long_url=submitted_url, short_code=random_code)
        db.session.add(url_entry)
        db.session.commit()

        # Redirect to the 'result' page with the generated short URL and submitted URL
        return redirect(url_for('result', short_url=short_url, submitted_url=submitted_url))

    return render_template('upload.html')

@app.route('/result')
def result():
    # Retrieve the short URL and submitted URL from the query parameters
    short_url = request.args.get('short_url')
    submitted_url = request.args.get('submitted_url')
    return render_template('result.html', short_url=short_url, submitted_url=submitted_url)
