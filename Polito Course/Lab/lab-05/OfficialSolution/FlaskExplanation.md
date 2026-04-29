# README — Complete Explanation of the Flask Web App

## 1. Project overview

This project is a small Flask web application that works like a simple social-network demo. It has:

* A **Home** page that displays a list of posts.
* An **About us** page that displays developer profile cards.
* A **single post** page that shows one selected post.
* A shared base layout using **Jinja template inheritance**.
* Static images and CSS stored inside the `static/` folder.

The application does **not** use a database. All posts and developer information are hard-coded directly in `app.py` as Python lists of dictionaries.

---

## 2. Folder structure

```text
OfficialSolution/
├── app.py
├── static/
│   ├── img1.jpg
│   ├── img2.jpg
│   ├── img3.jpg
│   ├── style.css
│   └── user.jpg
└── templates/
    ├── about.html
    ├── base.html
    ├── home.html
    └── post.html
```

### Meaning of each part

* `app.py`: Main Flask application. It defines the Flask app, sample data, routes, and server startup.
* `templates/base.html`: Main reusable HTML layout used by all pages.
* `templates/home.html`: Home page that lists all posts.
* `templates/about.html`: About page that lists developers.
* `templates/post.html`: Single-post page.
* `static/style.css`: Custom CSS styles.
* `static/img1.jpg`, `img2.jpg`, `img3.jpg`: Post images.
* `static/user.jpg`: User/developer profile image.

---

## 3. How the app works overall

When a user opens the website, the browser sends an HTTP request to Flask. Flask matches the requested URL to one of the route functions in `app.py`.

The important routes are:

```text
/              -> home()
/about         -> about()
/posts/<id>    -> single_post(id)
```

Each route returns an HTML page using `render_template()`.

Flask loads the selected template from the `templates/` folder. The templates use Jinja syntax such as `{{ variable }}`, `{% for ... %}`, `{% block ... %}`, and `{% extends ... %}` to insert dynamic data into HTML.

---

## 4. Runtime behavior

### Home page flow

1. User visits `/`.
2. Flask calls `home()`.
3. `home()` sends the `posts` list to `home.html`.
4. `home.html` loops through the list and displays each post.
5. Each post image links to `/posts/<id>`.

### About page flow

1. User visits `/about`.
2. Flask calls `about()`.
3. `about()` creates a list called `p_developers`.
4. Flask sends that list to `about.html` as `developers`.
5. `about.html` loops through the developers and displays cards.

### Single post flow

1. User clicks a post on the home page.
2. Browser goes to `/posts/0`, `/posts/1`, or `/posts/2`.
3. Flask calls `single_post(id)`.
4. The function uses `posts[id]` to select the correct post.
5. Flask sends that post to `post.html`.
6. `post.html` displays only that one post.

---

## 5. Important limitations

This is a learning/demo app, not a production app.

* There is no database.
* There is no login system.
* There is no real post creation, even though a `+` button is displayed.
* `/posts/<id>` depends directly on list indexes. If the user opens `/posts/99`, the app will crash with an `IndexError` because there is no post at index `99`.
* `debug=True` is enabled, which is useful during development but unsafe in production.

---

# 6. `app.py` — line-by-line explanation

Original empty lines and comment-only lines are skipped.

## Line 2

```python
from flask import Flask, render_template
```

Imports two Flask tools:

* `Flask`: used to create the web application object.
* `render_template`: used to render HTML files from the `templates/` folder.

## Line 4

```python
app = Flask(__name__)
```

Creates the Flask application instance. `__name__` tells Flask where the current Python file is located, so Flask can correctly find folders such as `templates/` and `static/`.

## Line 6

```python
posts = [
```

Starts a Python list named `posts`. This list stores all posts shown on the home page.

## Line 7

```python
{'id': 0, 'usrname': '@juan', 'usrimg': 'user.jpg', 'img': 'img1.jpg',
```

Starts the first post dictionary. It contains:

* `id: 0`: identifier/index for the post.
* `usrname: '@juan'`: username shown beside the post.
* `usrimg: 'user.jpg'`: profile image file.
* `img: 'img1.jpg'`: main post image.

## Line 8

```python
'date': '1 day ago', 'post': 'Lorem ipsum dolor sit amet, ...'}
```

Completes the first post dictionary by adding:

* `date`: text shown on the post, here `1 day ago`.
* `post`: the post body text.

## Line 9

```python
{'id': 1, 'usrname': '@luigi', 'usrimg': 'user.jpg', 'img': 'img2.jpg',
```

Starts the second post dictionary. This post belongs to `@luigi`, uses the same user profile image, and uses `img2.jpg` as the main image.

## Line 10

```python
'date': '4 days ago', 'post': 'Lorem ipsum dolor sit amet, ...'}
```

Completes the second post with its date and text content.

## Line 11

```python
{'id': 2, 'usrname': '@alberto', 'usrimg': 'user.jpg', 'img': 'img3.jpg',
```

Starts the third post dictionary. This post belongs to `@alberto` and uses `img3.jpg` as the main image.

## Line 12

```python
'date': '2 weeks ago', 'post': 'Lorem ipsum dolor sit amet, ...'}
```

Completes the third post with its date and text content.

## Line 13

```python
]
```

Closes the `posts` list.

## Line 18

```python
@app.route('/')
```

Registers the URL `/` as a Flask route. When the browser requests the home page, Flask runs the function immediately below this decorator.

## Line 19

```python
def home():
```

Defines the `home()` view function. A view function handles a web request and returns a response.

## Line 20

```python
return render_template('home.html', posts=posts)
```

Renders `templates/home.html` and sends the `posts` list into the template. Inside `home.html`, the template can access the list using the variable name `posts`.

## Line 25

```python
@app.route('/about')
```

Registers the `/about` URL. When the user visits `/about`, Flask runs the `about()` function.

## Line 26

```python
def about():
```

Defines the `about()` view function.

## Line 27

```python
p_developers = [
```

Creates a local list named `p_developers`. This list exists only inside the `about()` function and stores developer profile information.

## Line 28

```python
{'id': 1234, 'name': 'Juan Pablo Sáenz', 'devimg': 'user.jpg',
```

Starts the first developer dictionary. It stores the developer ID, name, and profile image.

## Line 29

```python
'quote': 'A well-known quote, contained in a blockquote element', 'quoteAuthor': 'First quote author'},
```

Completes the first developer entry by adding a quote and quote author.

## Line 30

```python
{'id': 5678, 'name': 'Luigi De Russis', 'devimg': 'user.jpg',
```

Starts the second developer dictionary.

## Line 31

```python
'quote': 'A well-known quote, contained in a blockquote element', 'quoteAuthor': 'Second quote author'},
```

Completes the second developer entry by adding quote information.

## Line 32

```python
{'id': 9012, 'name': 'Alberto Monge Roffarello', 'devimg': 'user.jpg',
```

Starts the third developer dictionary.

## Line 33

```python
'quote': 'A well-known quote, contained in a blockquote element', 'quoteAuthor': 'Third quote author'}
```

Completes the third developer entry by adding quote information.

## Line 34

```python
]
```

Closes the `p_developers` list.

## Line 35

```python
return render_template('about.html', developers=p_developers)
```

Renders `templates/about.html` and passes the developer list to it using the template variable name `developers`.

## Line 38

```python
@app.route('/posts/<int:id>')
```

Registers a dynamic route. `<int:id>` means Flask expects an integer in this part of the URL.

Examples:

```text
/posts/0
/posts/1
/posts/2
```

The integer is passed into the function as the parameter `id`.

## Line 39

```python
def single_post(id):
```

Defines the `single_post()` view function. It receives the post ID from the URL.

## Line 40

```python
post = posts[id]
```

Selects one post from the `posts` list using the given `id` as a list index.

For example:

* If `id` is `0`, it selects the first post.
* If `id` is `1`, it selects the second post.
* If `id` is `2`, it selects the third post.

Important: this works only because the post IDs match the list indexes.

## Line 41

```python
return render_template('post.html', post=post)
```

Renders `templates/post.html` and passes the selected post into the template using the variable name `post`.

## Line 44

```python
if __name__ == "__main__":
```

Checks whether this file is being run directly with `python app.py`. If yes, the server starts. If the file is imported by another Python file, the server does not automatically start.

## Line 45

```python
app.run(host='0.0.0.0', port=3000, debug=True)
```

Starts the Flask development server.

* `host='0.0.0.0'`: makes the app listen on all network interfaces.
* `port=3000`: runs the app on port `3000`.
* `debug=True`: enables debug mode and automatic reloads during development.

---

# 7. `templates/base.html` — line-by-line explanation

`base.html` is the main layout file. Other templates extend it instead of repeating the same HTML structure.

## Line 1

```html
<!doctype html>
```

Declares that this is an HTML5 document.

## Line 2

```html
<html lang="en">
```

Starts the HTML document and says the page language is English.

## Line 4

```html
<head>
```

Starts the metadata section of the HTML document.

## Line 5

```html
<meta charset="utf-8">
```

Sets the character encoding to UTF-8, allowing the page to correctly display many characters, including accented names.

## Line 6

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Makes the layout responsive on mobile devices by matching the page width to the device width.

## Line 7

```html
<title>My Cool Social Network - {% block title %}{% endblock %}</title>
```

Sets the browser tab title. The `{% block title %}` part can be filled by child templates such as `home.html`, `about.html`, and `post.html`.

## Lines 8–9

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
  integrity="..." crossorigin="anonymous">
```

Loads Bootstrap CSS from a CDN. Bootstrap provides ready-made responsive layout classes such as `container-fluid`, `row`, `col-lg-3`, `navbar`, and `btn`.

## Line 10

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

Loads the local CSS file from `static/style.css`. `url_for('static', filename='style.css')` asks Flask to generate the correct URL for the static file.

## Line 11

```html
</head>
```

Closes the head section.

## Line 13

```html
<body>
```

Starts the visible page body.

## Line 14

```html
<header id="myheader">
```

Starts the page header and gives it the ID `myheader`, which is styled in `style.css`.

## Line 15

```html
<nav class="navbar navbar-dark navbar-expand-lg mynavbar">
```

Creates a Bootstrap navigation bar. `mynavbar` is a custom class styled in the CSS file.

## Line 16

```html
<div class="container-fluid">
```

Creates a full-width Bootstrap container inside the navigation bar.

## Line 17

```html
<h1 class="display-5">My Cool Social Network</h1>
```

Displays the website title using Bootstrap's `display-5` typography class.

## Lines 18–19

```html
<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
  aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
```

Creates the mobile menu button. On smaller screens, Bootstrap uses this button to collapse and expand the navigation links.

## Line 20

```html
<span class="navbar-toggler-icon"></span>
```

Displays the hamburger icon inside the mobile menu button.

## Line 21

```html
</button>
```

Closes the mobile menu button.

## Line 22

```html
<div class="collapse navbar-collapse" id="navbarSupportedContent">
```

Creates the collapsible area that contains the navigation links.

## Line 23

```html
<ul class="navbar-nav ms-auto">
```

Starts the navigation list. `ms-auto` pushes the navigation links to the right side.

## Line 24

```html
<li class="nav-item">
```

Starts the first navigation item.

## Line 25

```html
<a class="nav-link {%block home_active%}{% endblock %}" aria-current="page" href="/">Home</a>
```

Creates the Home link. The `{% block home_active %}` block allows child templates to add the class `active` when the current page is the Home page.

## Line 26

```html
</li>
```

Closes the first navigation item.

## Line 27

```html
<li class="nav-item">
```

Starts the second navigation item.

## Line 28

```html
<a class="nav-link {%block about_active%}{% endblock %}" href="{{ url_for('about') }}">About us</a>
```

Creates the About us link. `url_for('about')` generates the URL for the Flask route handled by the `about()` function.

## Line 29

```html
</li>
```

Closes the second navigation item.

## Line 30

```html
</ul>
```

Closes the navigation list.

## Line 31

```html
</div>
```

Closes the collapsible navbar content.

## Line 33

```html
</div>
```

Closes the navbar container.

## Line 34

```html
</nav>
```

Closes the navigation bar.

## Line 35

```html
</header>
```

Closes the header.

## Line 36

```html
<div class="container-fluid mt-4">
```

Creates the main full-width page container. `mt-4` adds top margin.

## Line 37

```html
<div class="row">
```

Starts a Bootstrap row for page content.

## Line 38

```html
{%block content %}{% endblock %}
```

Defines the main content block. Child templates replace this block with their own page-specific content.

## Line 39

```html
<button type="button" class="btn btn-lg mybutton">+</button>
```

Creates a floating `+` button. It is styled by the custom `.mybutton` CSS class. In this version of the app, it is only visual and does not submit anything.

## Line 40

```html
</div>
```

Closes the Bootstrap row.

## Line 41

```html
</div>
```

Closes the main page container.

## Lines 44–46

```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
  integrity="..."
  crossorigin="anonymous"></script>
```

Loads Bootstrap's JavaScript bundle from a CDN. This is needed for interactive Bootstrap components, especially the responsive navbar toggler.

## Line 48

```html
</body>
```

Closes the visible page body.

## Line 50

```html
</html>
```

Closes the HTML document.

---

# 8. `templates/home.html` — line-by-line explanation

`home.html` builds the home page and displays all posts.

## Line 1

```jinja2
{% extends "base.html" %}
```

Tells Jinja that this template uses `base.html` as its parent layout.

## Line 2

```jinja2
{% block title %}Home{% endblock %}
```

Fills the `title` block from `base.html` with `Home`, so the browser title becomes `My Cool Social Network - Home`.

## Line 3

```jinja2
{% block home_active %}active{% endblock %}
```

Adds the Bootstrap `active` class to the Home navigation link.

## Line 5

```jinja2
{% block content %}
```

Starts the page-specific content that will be inserted into the `content` block of `base.html`.

## Line 6

```html
<aside id="myaside" class="col-lg-3 col-md-12">
```

Creates a sidebar. On large screens it takes 3 columns; on medium screens it takes the full width.

## Line 7

```html
<ul>
```

Starts the sidebar list.

## Line 8

```html
<li>
```

Starts the first list item.

## Line 9

```html
<a class="link-primary" href="#">Today</a>
```

Creates a placeholder link labeled `Today`. It currently links to `#`, so it does not navigate to a real page.

## Line 10

```html
</li>
```

Closes the first list item.

## Line 11

```html
<li>
```

Starts the second list item.

## Line 12

```html
<a class="link-primary" href="#">This week</a>
```

Creates a placeholder link labeled `This week`.

## Line 13

```html
</li>
```

Closes the second list item.

## Line 14

```html
<li>
```

Starts the third list item.

## Line 15

```html
<a class="link-primary" href="#">This month</a>
```

Creates a placeholder link labeled `This month`.

## Line 16

```html
</li>
```

Closes the third list item.

## Line 17

```html
</ul>
```

Closes the sidebar list.

## Line 18

```html
</aside>
```

Closes the sidebar.

## Line 19

```html
<main class="col-lg-9 col-md-12">
```

Starts the main content area. On large screens it takes 9 columns; on medium screens it takes the full width.

## Line 20

```jinja2
{% for post in posts %}
```

Starts a Jinja loop. It repeats the following HTML once for every dictionary inside the `posts` list passed from `app.py`.

## Line 21

```html
<article class="row border p-2 mx-2 my-4">
```

Starts one post card. Bootstrap classes add row layout, border, padding, horizontal margin, and vertical margin.

## Line 22

```html
<div class="col-lg-3 col-md-6 col-sm-12 px-0">
```

Creates the image column for the post. The width changes based on screen size.

## Line 23

```jinja2
<a href="{{url_for('single_post', id=post.id)}}"><img class="w-100 p-2" src="{{ url_for('static', filename=post.img) }}" alt="..."></a>
```

Creates a clickable image. The link goes to the `single_post` route with the current post's ID. The image source is generated from the `static/` folder using the current post's `img` value.

## Line 24

```html
</div>
```

Closes the image column.

## Line 25

```html
<div class="col-lg-9 col-md-6 col-sm-12">
```

Starts the text/details column for the post.

## Line 26

```html
<section class="d-flex align-items-center mt-2 mb-4">
```

Creates a flexbox row for the profile image, username, and date. Bootstrap classes align items vertically and add margin.

## Lines 27–28

```jinja2
<div><img class="usrimg rounded-circle" src="{{ url_for('static', filename= post.usrimg ) }}"
    alt="This is the image of user {{ post.usrname |e }}"></div>
```

Displays the user's profile image. The image file comes from `post.usrimg`. The `|e` filter escapes the username in the alt text to protect the HTML from unsafe characters.

## Line 29

```html
<div>
```

Starts a container for the username.

## Line 30

```jinja2
<h4 class="username">{{ post.usrname |e }}</h4>
```

Displays the username and escapes it using `|e`.

## Line 31

```html
</div>
```

Closes the username container.

## Line 32

```html
<div class="flex-grow-1 text-end">
```

Creates a container for the date. `flex-grow-1` takes remaining space, and `text-end` aligns the date to the right.

## Line 33

```jinja2
<p>{{ post.date |e }}</p>
```

Displays the post date and escapes it.

## Line 34

```html
</div>
```

Closes the date container.

## Line 35

```html
</section>
```

Closes the profile/date section.

## Line 36

```jinja2
<p>{{ post.post |e }}</p>
```

Displays the post text and escapes it.

## Line 37

```html
</div>
```

Closes the text/details column.

## Line 38

```html
</article>
```

Closes the post card.

## Line 39

```jinja2
{% endfor %}
```

Ends the loop over `posts`.

## Line 40

```html
</main>
```

Closes the main content area.

## Line 41

```jinja2
{% endblock %}
```

Ends the content block.

---

# 9. `templates/about.html` — line-by-line explanation

`about.html` displays the list of developers.

## Line 1

```jinja2
{% extends "base.html" %}
```

Uses `base.html` as the parent layout.

## Line 2

```jinja2
{% block title %}About{% endblock %}
```

Sets the browser tab title to `My Cool Social Network - About`.

## Line 3

```jinja2
{% block about_active %}active{% endblock %}
```

Adds the Bootstrap `active` class to the About navigation link.

## Line 5

```jinja2
{% block content %}
```

Starts the page-specific content block.

## Line 6

```html
<div class="row marketing text-center">
```

Creates a Bootstrap row and centers the text.

## Line 7

```jinja2
{% for dev in developers %}
```

Starts a loop over the `developers` list passed from `app.py`.

## Line 8

```html
<div class="col-lg-4">
```

Creates one developer column. On large screens, three columns fit in one row because each one takes 4 of Bootstrap's 12 columns.

## Lines 9–10

```jinja2
<div><img class="devimg rounded-circle" src="{{ url_for('static', filename= dev.devimg ) }}"
    alt="This is the image of user {{ dev.devimg |e }}"></div>
```

Displays the developer image from the `static/` folder. The image is styled as a circle using Bootstrap's `rounded-circle` class and the custom `.devimg` CSS class.

## Line 11

```jinja2
<h2 class="fw-normal my-4">{{ dev.name |e }}</h2>
```

Displays the developer name. `fw-normal` controls font weight, `my-4` adds vertical margin, and `|e` escapes the name.

## Line 12

```html
<figure class="text-center">
```

Starts a semantic figure element for the quote section.

## Line 13

```html
<blockquote class="blockquote">
```

Starts a Bootstrap-styled blockquote.

## Line 14

```jinja2
<p>{{ dev.quote |e }}</p>
```

Displays the developer quote and escapes it.

## Line 15

```html
</blockquote>
```

Closes the blockquote.

## Line 16

```html
<figcaption class="blockquote-footer">
```

Starts the quote author caption with Bootstrap footer styling.

## Line 17

```jinja2
{{ dev.quoteAuthor |e }}
```

Displays the quote author and escapes it.

## Line 18

```html
</figcaption>
```

Closes the caption.

## Line 19

```html
</figure>
```

Closes the figure.

## Line 20

```html
</div>
```

Closes one developer column.

## Line 21

```jinja2
{% endfor %}
```

Ends the developer loop.

## Line 22

```html
</div>
```

Closes the row.

## Line 23

```jinja2
{% endblock %}
```

Ends the content block.

---

# 10. `templates/post.html` — line-by-line explanation

`post.html` displays one selected post.

## Line 1

```jinja2
{% extends "base.html" %}
```

Uses `base.html` as the parent layout.

## Line 2

```jinja2
{% block title %}Post by {{post.usrname}}{% endblock %}
```

Sets the browser tab title dynamically using the selected post's username.

## Line 3

```jinja2
{% block home_active %}active{% endblock %}
```

Marks the Home navigation link as active. This makes sense because a single post is part of the home/post section.

## Line 5

```jinja2
{% block content %}
```

Starts the page-specific content block.

## Line 6

```html
<main class="col-lg-9 col-md-12">
```

Starts the main content area. Unlike the home page, there is no sidebar here.

## Line 7

```html
<article class="row border p-2 mx-2 my-4">
```

Starts the post card layout.

## Line 8

```html
<div class="col-lg-3 col-md-6 col-sm-12 px-0">
```

Creates the image column.

## Line 9

```jinja2
<img class="w-100 p-2" src="{{ url_for('static', filename=post.img) }}" alt="...">
```

Displays the selected post image from the `static/` folder.

## Line 10

```html
</div>
```

Closes the image column.

## Line 11

```html
<div class="col-lg-9 col-md-6 col-sm-12">
```

Starts the text/details column.

## Line 12

```html
<section class="d-flex align-items-center mt-2 mb-4">
```

Creates a flexbox row for profile image, username, and date.

## Lines 13–14

```jinja2
<div><img class="usrimg rounded-circle" src="{{ url_for('static', filename= post.usrimg ) }}"
    alt="This is the image of user {{ post.usrname |e }}"></div>
```

Displays the user's profile image and creates escaped alt text.

## Line 15

```html
<div>
```

Starts a container for the username.

## Line 16

```jinja2
<h4 class="username">{{ post.usrname |e }}</h4>
```

Displays the selected post's username and escapes it.

## Line 17

```html
</div>
```

Closes the username container.

## Line 18

```html
<div class="flex-grow-1 text-end">
```

Creates a right-aligned date container.

## Line 19

```jinja2
<p>{{ post.date |e }}</p>
```

Displays the selected post's date and escapes it.

## Line 20

```html
</div>
```

Closes the date container.

## Line 21

```html
</section>
```

Closes the profile/date section.

## Line 22

```jinja2
<p>{{ post.post |e }}</p>
```

Displays the selected post's text and escapes it.

## Line 23

```html
</div>
```

Closes the text/details column.

## Line 24

```html
</article>
```

Closes the post card.

## Line 25

```html
</main>
```

Closes the main content area.

## Line 26

```jinja2
{% endblock %}
```

Ends the content block.

---

# 11. `static/style.css` — line-by-line explanation

`style.css` contains custom styling on top of Bootstrap.

## Line 1

```css
.devimg {
```

Starts the CSS rule for developer images.

## Line 2

```css
display: inline;
```

Makes developer images behave like inline elements.

## Line 3

```css
height: 140px;
```

Sets developer image height to `140px`.

## Line 4

```css
vertical-align: middle;
```

Vertically aligns the image with nearby inline content.

## Line 5

```css
}
```

Closes the `.devimg` rule.

## Line 7

```css
.usrimg {
```

Starts the CSS rule for user profile images in posts.

## Line 8

```css
display: inline;
```

Makes user images inline.

## Line 9

```css
height: 50px;
```

Sets user profile image height to `50px`.

## Line 10

```css
vertical-align: middle;
```

Vertically aligns the image with surrounding content.

## Line 11

```css
margin: 0.5rem 0.5rem 0.5rem 0rem;
```

Adds margin around the image: top, right, bottom, and left.

## Line 12

```css
}
```

Closes the `.usrimg` rule.

## Line 14

```css
.mybutton {
```

Starts the custom style for the floating `+` button.

## Line 15

```css
background-color: #04AA6D;
```

Sets the button background color to green.

## Line 16

```css
border: none;
```

Removes the default button border.

## Line 17

```css
border-radius: 50%;
```

Makes the button circular.

## Line 18

```css
bottom: 30px;
```

Places the button `30px` above the bottom of the viewport.

## Line 19

```css
color: white;
```

Makes the `+` text white.

## Line 20

```css
height: 60px;
```

Sets the button height to `60px`.

## Line 21

```css
position: fixed;
```

Keeps the button fixed in the browser window even when the page scrolls.

## Line 22

```css
right: 30px;
```

Places the button `30px` from the right side of the viewport.

## Line 23

```css
text-align: center;
```

Centers the button text horizontally.

## Line 24

```css
text-decoration: none;
```

Removes text decoration such as underlines.

## Line 25

```css
vertical-align: middle;
```

Vertically aligns inline content.

## Line 26

```css
width: 60px;
```

Sets the button width to `60px`.

## Line 27

```css
}
```

Closes the `.mybutton` rule.

## Line 29

```css
.mynavbar {
```

Starts the custom navigation bar style.

## Line 30

```css
background-color: #04AA6D;
```

Sets the navbar background color to the same green used for the floating button.

## Line 31

```css
height: 10rem;
```

Sets the navbar height to `10rem`.

## Line 32

```css
}
```

Closes the `.mynavbar` rule.

## Line 34

```css
.username {
```

Starts the username styling rule.

## Line 35

```css
font-weight: 100;
```

Makes usernames very light/thin.

## Line 36

```css
}
```

Closes the `.username` rule.

## Line 38

```css
#myaside li {
```

Targets list items inside the element with ID `myaside`.

## Line 39

```css
padding-bottom: 5px;
```

Adds space below each sidebar list item.

## Line 40

```css
}
```

Closes the `#myaside li` rule.

## Line 42

```css
#myaside ul {
```

Targets unordered lists inside the element with ID `myaside`.

## Line 43

```css
list-style-type: none;
```

Removes default bullet points.

## Line 44

```css
padding: 0rem 1rem;
```

Adds horizontal padding and removes vertical padding.

## Line 45

```css
}
```

Closes the `#myaside ul` rule.

## Line 47

```css
#myheader h1 {
```

Targets the `h1` inside the element with ID `myheader`.

## Line 48

```css
color: white;
```

Makes the main header title white.

## Line 49

```css
}
```

Closes the `#myheader h1` rule.

## Line 51

```css
@media (max-width: 991.98px) {
```

Starts a responsive media query. The rules inside apply only when the screen width is `991.98px` or smaller.

## Line 53

```css
#myaside ul {
```

Targets the sidebar list on smaller screens.

## Line 54

```css
display: flex;
```

Changes the sidebar list into a flex container.

## Line 55

```css
justify-content: space-between;
```

Spreads the sidebar links evenly across the available width.

## Line 56

```css
list-style-type: none;
```

Keeps bullet points removed on smaller screens.

## Line 57

```css
padding: 0rem 1rem;
```

Sets responsive sidebar padding.

## Line 58

```css
}
```

Closes the responsive `#myaside ul` rule.

## Line 60

```css
aside li {
```

Targets list items inside any `aside` element on smaller screens.

## Line 61

```css
display: inline;
```

Displays sidebar list items inline.

## Line 62

```css
list-style-type: none;
```

Removes list markers.

## Line 63

```css
padding: 0em;
```

Removes padding from the sidebar list items.

## Line 64

```css
width: fit-content;
```

Makes each list item only as wide as its content.

## Line 65

```css
}
```

Closes the responsive `aside li` rule.

## Line 66

```css
}
```

Closes the media query.

---

# 12. Template inheritance summary

The templates use this inheritance structure:

```text
base.html
├── home.html
├── about.html
└── post.html
```

`base.html` defines the repeated page structure:

* HTML document skeleton
* Bootstrap CSS and JS imports
* Navbar
* Main container
* Floating `+` button

The child templates only fill blocks:

* `title`
* `home_active`
* `about_active`
* `content`

This avoids duplicating the same navbar and HTML setup in every page.

---

# 13. Jinja features used

## `{{ ... }}`

Outputs a value into HTML.

Example:

```jinja2
{{ post.usrname |e }}
```

This displays the username.

## `{% ... %}`

Runs template logic.

Example:

```jinja2
{% for post in posts %}
```

This loops through all posts.

## `|e`

Escapes content before inserting it into HTML. This helps prevent unsafe HTML injection.

## `url_for()`

Generates URLs safely.

Examples:

```jinja2
{{ url_for('about') }}
{{ url_for('static', filename='style.css') }}
{{ url_for('single_post', id=post.id) }}
```

---

# 14. How to run the app

From inside the `OfficialSolution` folder:

```bash
pip install flask
python app.py
```

Then open:

```text
http://localhost:3000
```

Because the app uses:

```python
app.run(host='0.0.0.0', port=3000, debug=True)
```

it listens on port `3000`.

---

# 15. Suggested improvements

For a more complete or production-ready version, you could add:

* A database instead of hard-coded lists.
* Error handling for invalid post IDs.
* A real post creation form for the `+` button.
* Separate data models.
* User authentication.
* A `requirements.txt` file.
* Environment-based configuration.
* `debug=False` in production.

A safer version of the single-post route would check whether the post exists before rendering it.

Example idea:

```python
@app.route('/posts/<int:id>')
def single_post(id):
    if id < 0 or id >= len(posts):
        abort(404)
    post = posts[id]
    return render_template('post.html', post=post)
```

This prevents the app from crashing when a user opens a URL such as `/posts/99`.
