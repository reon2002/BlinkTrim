# from flask import Flask, render_template, request, redirect, url_for
# import random
# import string
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# # Configure the PostgreSQL database URI
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Reon@2002@5432/blinktrim'

# # Create a SQLAlchemy database instance
# db = SQLAlchemy(app)

# # Generate a random 8-character code for short URLs
# def generate_short_code():
#     code = ''.join(random.choice(string.digits) for _ in range(8))
#     return code

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         # Process the submitted URL and generate a short URL
#         submitted_url = request.form.get('url')

#         # Generate a random 8-digit code for the short URL
#         random_code = generate_short_code()

#         # Construct the short URL
#         short_url = f'short.bt/{random_code}'

#         # Redirect to the 'result' page with the generated short URL and submitted URL
#         return redirect(url_for('result', short_url=short_url, submitted_url=submitted_url))

#     return render_template('upload.html')



# @app.route('/result')
# def result():
#     # Retrieve the short URL and submitted URL from the query parameters
#     short_url = request.args.get('short_url')
#     submitted_url = request.args.get('submitted_url')
#     return render_template('result.html', short_url=short_url, submitted_url=submitted_url)


# if __name__ == '__main__':
#     app.run(debug=True)

from Project import app  # Update this import statement to match your package name

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)