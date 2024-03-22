
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application
app = Flask(__name__)

# Define the routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/articles/<category_id>')
def articles_by_category(category_id):
    return render_template('articles.html', category_id=category_id)

@app.route('/articles/<category_id>/<article_id>')
def article(category_id, article_id):
    return render_template('article.html', category_id=category_id, article_id=article_id)

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
