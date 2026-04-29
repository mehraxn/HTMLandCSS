# README: Flask `app.py` Explanation Only

This README explains **only the Flask Python file**, `app.py`.

It does not explain the HTML files or the CSS file. It only explains what the Flask app does in Python.

---

# Purpose of `app.py`

`app.py` is the main Python file of the Flask application.

Its job is to:

1. Create the Flask app.
2. Store the data used by the app.
3. Create the website routes.
4. Send data from Python to the correct page.
5. Start the Flask development server.

---

# Line-by-line explanation

## Line 1

```python
from flask import Flask, render_template
```

This line imports two tools from Flask.

`Flask` is used to create the web application.

`render_template` is used to return an HTML template from a Flask route.

So this line means:

> Get the Flask tools that this app needs.

---

## Line 3

```python
app = Flask(__name__)
```

This line creates the Flask application object.

`app` is the name of the Flask application.

`Flask(__name__)` tells Flask to create an app based on this Python file.

`__name__` helps Flask know where the project is located.

So this line means:

> Create the Flask app.

---

## Line 5

```python
# The data below is sent from Flask to the HTML pages.
```

This is a Python comment.

It does not run.

It only explains that the data written below will be sent from Flask to the pages.

---

## Line 6

```python
# Each dictionary is one post.
```

This is another comment.

It explains that every dictionary inside the `posts` list represents one post.

---

## Line 7

```python
posts = [
```

This line creates a list called `posts`.

This list stores the data for the posts shown in the app.

The `[` means the list starts here.

---

## Lines 8–14

```python
    {
        "username": "luigi",
        "publication_date": "2 days ago",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tristique lobortis molestie. Donec laoreet iaculis nibh sed viverra. Nunc condimentum tincidunt mollis. Curabitur gravida aliquam urna, ac vulputate felis condimentum at. Sed sapien lectus, aliquam ac ornare sed, dapibus pulvinar ligula.",
        "profile_image": "/static/images/user.jpg",
        "post_image": "/static/images/img1.jpg",
    },
```

This is the first post dictionary.

A dictionary stores data as key-value pairs.

For example:

```python
"username": "luigi"
```

means the key is `username` and the value is `luigi`.

This first post has:

* username: `luigi`
* publication date: `2 days ago`
* post text
* profile image path
* post image path

The comma after the dictionary means more posts will come after it.

---

## Lines 15–21

```python
    {
        "username": "alberto",
        "publication_date": "4 days ago",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tristique lobortis molestie. Donec laoreet iaculis nibh sed viverra. Nunc condimentum tincidunt mollis. Curabitur gravida aliquam urna, ac vulputate felis condimentum at. Sed sapien lectus, aliquam ac ornare sed, dapibus pulvinar ligula.",
        "profile_image": "/static/images/user.jpg",
        "post_image": "/static/images/img2.jpg",
    },
```

This is the second post dictionary.

It has the same kind of information as the first post, but with different values.

This post belongs to `alberto`.

Its post image is:

```python
"/static/images/img2.jpg"
```

---

## Lines 22–28

```python
    {
        "username": "juan",
        "publication_date": "1 week ago",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tristique lobortis molestie. Donec laoreet iaculis nibh sed viverra. Nunc condimentum tincidunt mollis.",
        "profile_image": "/static/images/user.jpg",
        "post_image": None,
    },
```

This is the third post dictionary.

This post belongs to `juan`.

The important part is:

```python
"post_image": None
```

`None` means there is no value.

So this post does not have a post image.

---

## Line 29

```python
]
```

This closes the `posts` list.

So the `posts` list contains three post dictionaries.

---

## Line 31

```python
# Each dictionary is one developer shown on the about page.
```

This is a comment.

It explains that the next list stores developer information.

---

## Line 32

```python
developers = [
```

This line creates a list called `developers`.

This list stores information about the developers shown in the app.

---

## Lines 33–38

```python
    {
        "name": "Luigi Verdi",
        "role": "Front-end Developer",
        "bio": "Passionate about design and usability, Luigi works on the user interface and the visual experience of the application.",
        "photo": "/static/images/img1.jpg",
    },
```

This is the first developer dictionary.

It stores:

* developer name
* developer role
* short biography
* photo path

The developer is `Luigi Verdi`.

His role is `Front-end Developer`.

---

## Lines 39–44

```python
    {
        "name": "Alberto Rossi",
        "role": "Back-end Developer",
        "bio": "Skilled in Python and Flask, Alberto manages the server-side logic and the data architecture of the project.",
        "photo": "/static/images/img2.jpg",
    },
```

This is the second developer dictionary.

The developer is `Alberto Rossi`.

His role is `Back-end Developer`.

---

## Line 45

```python
]
```

This closes the `developers` list.

So the `developers` list contains two developer dictionaries.

---

## Line 48

```python
@app.route("/")
```

This is a Flask route decorator.

A route connects a browser URL to a Python function.

The route `/` means the home route.

So when the browser visits:

```text
http://127.0.0.1:5000/
```

Flask will run the function under this route.

---

## Line 49

```python
def index():
```

This defines a function called `index`.

This function belongs to the `/` route.

So when the user opens the home route, Flask runs `index()`.

---

## Line 50

```python
    return render_template("index.html", posts=posts, active_page="home")
```

This line returns the response for the home route.

`render_template("index.html")` tells Flask to render the `index.html` template.

`posts=posts` sends the Python `posts` list to that template.

The first `posts` is the name the template will use.

The second `posts` is the Python variable created earlier.

`active_page="home"` sends the value `home` to the template.

This is usually used to know which page is currently active.

So this line means:

> Show the home page and send it the posts data.

---

## Line 53

```python
@app.route("/about")
```

This is another Flask route decorator.

The route is `/about`.

So when the browser visits:

```text
http://127.0.0.1:5000/about
```

Flask will run the function under this route.

---

## Line 54

```python
def about():
```

This defines a function called `about`.

This function belongs to the `/about` route.

So when the user opens `/about`, Flask runs `about()`.

---

## Line 55

```python
    return render_template("about.html", developers=developers, active_page="about")
```

This line returns the response for the about route.

`render_template("about.html")` tells Flask to render the `about.html` template.

`developers=developers` sends the Python `developers` list to that template.

The first `developers` is the name the template will use.

The second `developers` is the Python variable created earlier.

`active_page="about"` sends the value `about` to the template.

So this line means:

> Show the about page and send it the developers data.

---

## Line 58

```python
if __name__ == "__main__":
```

This line checks whether this file is being run directly.

When you run this command:

```bash
python app.py
```

then `__name__` becomes `"__main__"`.

So the condition becomes true.

This is used to make sure the server starts only when this file is run directly.

---

## Line 59

```python
    app.run(debug=True)
```

This line starts the Flask development server.

`app.run()` runs the app.

`debug=True` turns on debug mode.

Debug mode is useful while developing because it shows better error messages and reloads the app after changes.

Important:

`debug=True` is good for learning and development, but it should not be used for a real public website.

---

# What this Flask app contains

This Flask file creates two routes:

```text
/       → home route
/about  → about route
```

It also creates two Python lists:

```python
posts
```

and:

```python
developers
```

The home route sends `posts` data.

The about route sends `developers` data.

---

# Simple Flask flow

When the user opens the home route:

```text
Browser asks for /
Flask runs index()
Flask sends posts data
Browser receives the response
```

When the user opens the about route:

```text
Browser asks for /about
Flask runs about()
Flask sends developers data
Browser receives the response
```

---

# Final summary

`app.py` is the Python controller of the project.

It controls:

* the Flask app creation
* the data
* the routes
* the server start

It does not control the visual design directly. The visual design is handled outside this Python file.

This file mainly answers three questions:

1. What data does the app have?
2. What URLs does the app have?
3. What should Flask send back when each URL is opened?
