## Flask Application Design for Building a Marathi Website

### HTML Files

- `index.html`: The homepage of the website will welcome visitors and provide a brief overview of the site's content.
- `about.html`: This page will contain information about the purpose of the website, the team behind it, and contact details.
- `articles.html`: This page will display a list of articles written in Marathi, organized by categories.
- `article.html`: This page will show the detailed view of an article.

### Routes

- `/`: The root route will redirect to `index.html`.
- `/about`: This route will serve the `about.html` page.
- `/articles`: This route will display the `articles.html` page.
- `/articles/<category_id>`: This route will show articles belonging to a specific category.
- `/articles/<category_id>/<article_id>`: This route will display the details of a particular article.
- `/contact`: This route will handle user queries and provide contact information.