# README — Flask Application Explanation

## 1. Overview

This project is a small Flask web application that behaves like a simple social-post website.

The application starts with a predefined list of posts. Each post has a user name, user image, post image, date text, and post content. The app displays those posts on the home page, shows an about page with developer information, allows users to view a single post, and processes a form for creating a new post.

The application uses Flask routes to decide what happens when a user visits different URLs.

---

## 2. What the Flask app does

The app performs these main tasks:

1. Creates a Flask web server.
2. Stores example posts in a Python list called `posts`.
3. Displays all posts on the home page.
4. Displays developer information on an about page.
5. Displays one selected post using its ID.
6. Accepts new post form submissions.
7. Validates the submitted form data.
8. Saves an uploaded image into the `static/` folder.
9. Adds the new post to the in-memory `posts` list.
10. Runs the application on host `0.0.0.0`, port `3000`, with debug mode enabled.

Important note: the posts are stored only in memory. This means newly added posts disappear when the Flask server restarts. There is no database in this code.

---

## 3. Project requirements

To run this app, you need Python and Flask installed.

Example installation command:

```bash
pip install flask
```

Example run command:

```bash
python app.py
```

Then open this URL in the browser:

```text
http://localhost:3000
```

---

## 4. Imported modules

```python
from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import date, datetime
```

### Explanation

`Flask` is the main Flask class. It is used to create the web application object.

`render_template` is used to load and render HTML files from the `templates/` folder.

`request` is used to access data sent by the browser, such as form fields and uploaded files.

`redirect` is used to send the user to another route.

`flash` is imported but not used in this code. Normally, it is used to show temporary messages to users, such as error or success messages.

`url_for` is used to generate route URLs by using the route function name. For example, `url_for("home")` generates the URL for the `home()` route.

`date` is imported from the `datetime` module and is used to get today’s date.

`datetime` is imported from the `datetime` module and is used to convert a string date into a real Python date object.

---

## 5. Creating the Flask application

```python
app = Flask(__name__)
```

### Explanation

This line creates the Flask application object.

`app` is the main object used to define routes and run the server.

`__name__` tells Flask where the application is located. Flask uses this information to find related folders such as `templates/` and `static/`.

---

## 6. The `posts` list

```python
posts = [
    {
        "id": 0,
        "usrname": "@juan",
        "usrimg": "user.jpg",
        "img": "img1.jpg",
        "date": "1 giorno fa",
        "post": "Lorem ipsum ...",
    },
    ...
]
```

### Explanation

`posts` is a list of dictionaries.

Each dictionary represents one post.

Each post contains these fields:

| Field     | Meaning                                          |
| --------- | ------------------------------------------------ |
| `id`      | A numeric identifier for the post.               |
| `usrname` | The username of the person who created the post. |
| `usrimg`  | The profile image of the user.                   |
| `img`     | The image attached to the post.                  |
| `date`    | A text description of when the post was made.    |
| `post`    | The written content of the post.                 |

The starting data contains three example posts:

1. Post ID `0`, created by `@juan`.
2. Post ID `1`, created by `@luigi`.
3. Post ID `2`, created by `@alberto`.

The text `Lorem ipsum...` is placeholder text. It is commonly used when the real content is not important yet.

Because this data is stored in a normal Python list, it is temporary. It is not saved permanently.

---

## 7. Home page route

```python
@app.route("/")
def home():
    users = [d["usrname"] for d in posts]
    return render_template("home.html", posts=posts, users=users)
```

### Explanation line by line

```python
@app.route("/")
```

This decorator connects the URL `/` to the function below it.

The `/` URL is the home page of the website.

```python
def home():
```

This defines the function that runs when the user visits the home page.

```python
users = [d["usrname"] for d in posts]
```

This creates a new list called `users`.

It loops through every dictionary inside the `posts` list.

For each post dictionary, it takes the value stored in `"usrname"`.

The result is a list like this:

```python
["@juan", "@luigi", "@alberto"]
```

This list can be used in the HTML template, probably to let the user choose an existing username when creating a new post.

```python
return render_template("home.html", posts=posts, users=users)
```

This loads the `home.html` file from the `templates/` folder.

It sends two variables to the template:

* `posts`, containing all post data.
* `users`, containing all usernames.

The template can then display posts and user options dynamically.

---

## 8. About page route

```python
@app.route("/about")
def about():
    p_developers = [
        {
            "id": 1234,
            "name": "Juan Pablo Sáenz",
            "devimg": "user.jpg",
            "quote": "A well-known quote, contained in a blockquote element",
            "quoteAuthor": "First quote author",
        },
        ...
    ]
    return render_template("about.html", developers=p_developers)
```

### Explanation line by line

```python
@app.route("/about")
```

This decorator connects the `/about` URL to the `about()` function.

When the user visits `/about`, Flask runs this function.

```python
def about():
```

This defines the function for the about page.

```python
p_developers = [ ... ]
```

This creates a list called `p_developers`.

It contains dictionaries, and each dictionary represents one developer.

Each developer dictionary contains:

| Field         | Meaning                              |
| ------------- | ------------------------------------ |
| `id`          | A numeric ID for the developer.      |
| `name`        | The developer’s full name.           |
| `devimg`      | The image used for the developer.    |
| `quote`       | A quote displayed for the developer. |
| `quoteAuthor` | The person who said the quote.       |

The code defines three developers:

1. Juan Pablo Sáenz
2. Luigi De Russis
3. Alberto Monge Roffarello

```python
return render_template("about.html", developers=p_developers)
```

This loads the `about.html` template.

It passes the `p_developers` list into the template using the variable name `developers`.

Inside `about.html`, the template can loop over `developers` and display each developer’s information.

---

## 9. Single post route

```python
@app.route("/posts/<int:id>")
def single_post(id):
    post = posts[id]
    return render_template("post.html", post=post)
```

### Explanation line by line

```python
@app.route("/posts/<int:id>")
```

This decorator creates a dynamic route.

The route accepts a number inside the URL.

Examples:

```text
/posts/0
/posts/1
/posts/2
```

The part `<int:id>` means Flask expects an integer value and stores it in the variable `id`.

```python
def single_post(id):
```

This defines the function that runs when the user visits a post URL.

The `id` parameter receives the number from the URL.

For example, if the user visits `/posts/1`, then `id` becomes `1`.

```python
post = posts[id]
```

This selects one post from the `posts` list using the numeric ID.

For example:

* `posts[0]` returns the first post.
* `posts[1]` returns the second post.
* `posts[2]` returns the third post.

Important note: this works only because the post IDs match their positions in the list. If IDs and list positions become different, this line may show the wrong post or cause an error.

```python
return render_template("post.html", post=post)
```

This loads the `post.html` template.

It passes the selected post to the template using the variable name `post`.

The template can then display the details of that single post.

---

## 10. New post route

```python
@app.route("/posts/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        ...
    return redirect(url_for("home"))
```

### Explanation

This route handles the creation of a new post.

It supports both `GET` and `POST` requests.

A `GET` request normally happens when the user opens a page in the browser.

A `POST` request normally happens when the user submits a form.

In this code, the real work only happens if the request method is `POST`.

At the end, the user is redirected to the home page.

---

## 11. New post route — route decorator

```python
@app.route("/posts/new", methods=["GET", "POST"])
```

### Explanation

This decorator connects the `/posts/new` URL to the `new_post()` function.

`methods=["GET", "POST"]` means the route accepts both GET and POST requests.

Without this argument, Flask routes usually accept only GET requests by default.

---

## 12. New post route — function definition

```python
def new_post():
```

### Explanation

This defines the function that handles requests sent to `/posts/new`.

It is responsible for processing the new post form.

---

## 13. Checking if the form was submitted

```python
if request.method == "POST":
```

### Explanation

This checks whether the current request is a POST request.

If the user submitted a form, the method is usually POST.

If the condition is true, the app starts reading and validating form data.

If the condition is false, the function skips the form-processing code and redirects to the home page.

---

## 14. Reading form data

```python
post = request.form.to_dict()
```

### Explanation

`request.form` contains the text fields submitted by the HTML form.

`.to_dict()` converts the submitted form data into a normal Python dictionary.

For example, the dictionary might look like this:

```python
{
    "usrname": "@juan",
    "date": "2026-05-10",
    "post": "This is my new post"
}
```

The dictionary is stored in the variable `post`.

This `post` variable will later become the new post added to the `posts` list.

---

## 15. Validating the username

```python
if post["usrname"] not in [d["usrname"] for d in posts]:
    app.logger.error("The user does not exist!")
    return redirect(url_for("home"))
```

### Explanation line by line

```python
if post["usrname"] not in [d["usrname"] for d in posts]:
```

This checks whether the submitted username exists in the current list of posts.

`[d["usrname"] for d in posts]` creates a list of all existing usernames.

For the original data, that list is:

```python
["@juan", "@luigi", "@alberto"]
```

If the submitted username is not in that list, the user is considered invalid.

```python
app.logger.error("The user does not exist!")
```

This writes an error message to the Flask server log.

The message is visible in the terminal, not necessarily on the webpage.

```python
return redirect(url_for("home"))
```

This sends the browser back to the home page.

Because `return` is used, the function stops immediately and the invalid post is not added.

---

## 16. Validating that the post text is not empty

```python
if post["post"] == "":
    app.logger.error("The post cannot be empty!")
    return redirect(url_for("home"))
```

### Explanation line by line

```python
if post["post"] == "":
```

This checks whether the submitted post content is empty.

An empty string means the user did not type anything in the post field.

```python
app.logger.error("The post cannot be empty!")
```

This writes an error message to the server log.

```python
return redirect(url_for("home"))
```

This redirects the user to the home page and stops the function.

The empty post is not added.

---

## 17. Validating that a date was selected

```python
if post["date"] == "":
    app.logger.error("You must select a date")
    return redirect(url_for("home"))
```

### Explanation line by line

```python
if post["date"] == "":
```

This checks whether the date field is empty.

If the user did not select a date, the value is an empty string.

```python
app.logger.error("You must select a date")
```

This logs an error message in the terminal.

```python
return redirect(url_for("home"))
```

This sends the user back to the home page and stops the function.

The post is not added.

---

## 18. Validating that the date is not in the past

```python
if datetime.strptime(post["date"], "%Y-%m-%d").date() < date.today():
    app.logger.error("Invalid date")
    return redirect(url_for("home"))
```

### Explanation line by line

```python
if datetime.strptime(post["date"], "%Y-%m-%d").date() < date.today():
```

This converts the submitted date string into a Python date object.

`post["date"]` is expected to be in this format:

```text
YYYY-MM-DD
```

For example:

```text
2026-05-10
```

`datetime.strptime(post["date"], "%Y-%m-%d")` parses the string into a `datetime` object.

`.date()` converts that `datetime` object into a `date` object.

`date.today()` returns today’s date.

The condition checks whether the submitted date is earlier than today.

If the submitted date is in the past, it is invalid.

```python
app.logger.error("Invalid date")
```

This logs an error message.

```python
return redirect(url_for("home"))
```

This sends the user back to the home page and stops the function.

The post is not added.

Important note: this code allows today’s date and future dates, but rejects past dates.

---

## 19. Reading the uploaded image

```python
post_image = request.files["image"]
```

### Explanation

`request.files` contains files uploaded through the form.

`request.files["image"]` gets the uploaded file from the form field named `image`.

The uploaded file is stored in the variable `post_image`.

This requires the HTML form to have:

```html
<input type="file" name="image">
```

The form must also use:

```html
<form enctype="multipart/form-data">
```

Without `multipart/form-data`, file upload will not work correctly.

---

## 20. Saving the uploaded image

```python
if post_image:
    post_image.save("static/" + post_image.filename)
    post["img"] = post_image.filename
```

### Explanation line by line

```python
if post_image:
```

This checks whether a file was uploaded.

If a file exists, the app saves it.

```python
post_image.save("static/" + post_image.filename)
```

This saves the uploaded image into the `static/` folder.

For example, if the uploaded file is named `photo.jpg`, it is saved as:

```text
static/photo.jpg
```

The `static/` folder is the standard Flask folder for static files such as images, CSS, and JavaScript.

```python
post["img"] = post_image.filename
```

This adds the image filename to the new post dictionary.

The template can use this filename to display the image.

Important security note: saving files directly with `post_image.filename` can be unsafe because filenames can contain unwanted characters. A safer version would use `secure_filename` from `werkzeug.utils`.

---

## 21. Creating a new post ID

```python
post["id"] = posts[-1]["id"] + 1
```

### Explanation

`posts[-1]` gets the last post in the list.

`posts[-1]["id"]` gets the ID of the last post.

`+ 1` creates the next ID number.

For example, if the last post has ID `2`, the new post gets ID `3`.

This new ID is added to the `post` dictionary.

Important note: this works only if the `posts` list is not empty. If the list were empty, `posts[-1]` would cause an error.

---

## 22. Copying the user profile image

```python
post["usrimg"] = [
    p["usrimg"] for p in posts if p["usrname"] == post["usrname"]
][0]
```

### Explanation

This line finds the profile image of the submitted username.

The list comprehension does this:

```python
[p["usrimg"] for p in posts if p["usrname"] == post["usrname"]]
```

It loops through every post in `posts`.

For each post, it checks this condition:

```python
p["usrname"] == post["usrname"]
```

That means: find posts created by the same username as the submitted post.

For matching posts, it collects the value of `p["usrimg"]`.

The result might be:

```python
["user.jpg"]
```

Then `[0]` takes the first result from that list.

Finally, that profile image filename is assigned to:

```python
post["usrimg"]
```

This means the new post uses the same profile image as previous posts by the same user.

Important note: the username was already validated earlier, so the code expects that this list will contain at least one image.

---

## 23. Adding the new post

```python
posts.append(post)
```

### Explanation

This adds the new post dictionary to the end of the `posts` list.

After this line, the home page can display the new post along with the original posts.

Again, this change is temporary because the app does not use a database.

---

## 24. Redirecting to the home page

```python
return redirect(url_for("home"))
```

### Explanation

This redirects the browser to the home page.

`url_for("home")` generates the URL for the `home()` function.

Since the `home()` function is connected to `/`, this produces:

```text
/
```

`redirect(...)` tells the browser to go to that URL.

This line runs after processing the POST request, and it also runs if the user visits `/posts/new` with a GET request.

---

## 25. Running the Flask app

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
```

### Explanation line by line

```python
if __name__ == "__main__":
```

This checks whether the file is being run directly.

If you run:

```bash
python app.py
```

then `__name__` becomes `"__main__"`, so the code inside the `if` block runs.

If this file is imported by another Python file, the code inside the `if` block does not run automatically.

```python
app.run(host="0.0.0.0", port=3000, debug=True)
```

This starts the Flask development server.

`host="0.0.0.0"` means the app listens on all available network interfaces. This can make it accessible from outside the local machine, depending on the environment.

`port=3000` means the app runs on port 3000.

The local URL is usually:

```text
http://localhost:3000
```

`debug=True` enables debug mode.

Debug mode gives helpful error messages and automatically reloads the server when code changes.

Important warning: debug mode should not be used in production because it can expose sensitive debugging tools.

---

## 26. Route summary

| Route             | Method    | Function          | Purpose                                         |
| ----------------- | --------- | ----------------- | ----------------------------------------------- |
| `/`               | GET       | `home()`          | Shows the home page with all posts.             |
| `/about`          | GET       | `about()`         | Shows developer information.                    |
| `/posts/<int:id>` | GET       | `single_post(id)` | Shows one selected post.                        |
| `/posts/new`      | GET, POST | `new_post()`      | Processes the new-post form and redirects home. |

---

## 27. Data flow when creating a post

1. The user fills in a form on the website.
2. The browser sends the form to `/posts/new` using POST.
3. Flask checks that the request method is POST.
4. The app converts form fields into a dictionary.
5. The app checks whether the username exists.
6. The app checks whether the post text is not empty.
7. The app checks whether a date was selected.
8. The app checks whether the date is today or in the future.
9. The app reads the uploaded image.
10. The app saves the uploaded image into `static/`.
11. The app assigns a new ID.
12. The app assigns the correct user profile image.
13. The app appends the new post to the `posts` list.
14. The app redirects the user back to the home page.

---

## 28. Important limitations

### No database

The app stores posts in a Python list. This means new posts are lost when the server restarts.

A real application would normally use a database such as SQLite, PostgreSQL, or MySQL.

### No user accounts

The app checks usernames against existing posts, but it does not have a real user system.

There is no login, password, registration, or session management.

### Weak file-upload security

The app saves uploaded files using the original filename.

A safer version should use `secure_filename` and should check allowed file extensions.

### Possible route error

The single post route uses `posts[id]`. If a user visits a URL such as `/posts/99`, the app will likely crash because there is no post at index `99`.

A safer version should search for a post by ID and show a 404 page if it does not exist.

### Imported but unused `flash`

The `flash` function is imported but never used. The app logs errors to the terminal instead of showing them to the user.

A better version could use `flash()` to display validation messages on the page.

---

## 29. Possible improvements

1. Add a database to store posts permanently.
2. Add real user authentication.
3. Use `flash()` to show validation errors to users.
4. Use `secure_filename()` before saving uploaded files.
5. Validate image file extensions.
6. Handle invalid post IDs with a 404 error page.
7. Add a default image if the user does not upload one.
8. Separate routes, models, and configuration into multiple files for a larger project.

---

## 30. Simple explanation in one paragraph

This Flask application creates a small social-post website. It starts with three predefined posts, displays them on the home page, shows information about developers on an about page, allows users to open individual posts, and processes a form for adding new posts. When a new post is submitted, the app checks that the username exists, the post text is not empty, the date is selected, and the date is not in the past. If an image is uploaded, it saves the image in the `static/` folder. Then it gives the new post an ID, copies the user’s profile image, adds the post to the list, and redirects the user back to the home page.
