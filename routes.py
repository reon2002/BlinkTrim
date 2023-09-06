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
        # Process the submitted URL and check if it already exists in the database
        submitted_url = request.form.get('url')
        
        # Check if the submitted URL already exists in the database
        url_entry = Url.query.filter_by(long_url=submitted_url).first()
        
        if url_entry:
            # If the URL already exists, return the existing short URL
            short_url = f'short.bt/{url_entry.short_code}'
        else:
            # If the URL does not exist, generate a new short URL
            random_code = generate_short_code()
            short_url = f'short.bt/{random_code}'
            
            # Store the new URL in the database
            url_entry = Url(long_url=submitted_url, short_code=random_code)
            db.session.add(url_entry)
            db.session.commit()

        # Redirect to the 'result' page with the generated short URL and submitted URL
        return redirect(url_for('result', short_url=short_url, submitted_url=submitted_url))

    return render_template('upload.html')


@app.route('/result')
def result():
    # Retrieve the short URL from the query parameters
    short_url = request.args.get('short_url')

    # Check if the short URL exists in the database
    url_entry = Url.query.filter_by(short_code=short_url.split("/")[-1]).first()
    
    if url_entry:
        submitted_url = url_entry.long_url
        return render_template('result.html', short_url=short_url, submitted_url=submitted_url)
    else:
        return render_template('error.html')  # Render the error page when the short URL is not found


@app.route('/<short_code>')
def redirect_to_original_url(short_code):
    # Query the database to find the original URL based on the short code
    url_entry = Url.query.filter_by(short_code=short_code).first()
    
    if url_entry:
        # Redirect the user to the original URL
        return redirect(url_entry.long_url)
    else:
        # Render an error page if the short code is not found
        return render_template('error.html')
