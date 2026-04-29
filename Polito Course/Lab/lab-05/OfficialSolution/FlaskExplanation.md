# Flask Social Network — app.py Explained

A complete line-by-line breakdown of the Flask back-end for the social network lab.

---

## 1. Imports

```python
from flask import Flask, render_template
```

| Symbol | What it does |
|---|---|
| `Flask` | The class that creates and runs the web application |
| `render_template` | Loads an HTML file from the `templates/` folder and fills in Jinja variables |

---

## 2. Creating the Application Object

```python
app = Flask(__name__)
```

- `Flask(__name__)` creates the application instance.
- `__name__` is a built-in Python variable that holds the name of the current module (`"__main__"` when run directly).
- Flask uses it to locate the `templates/` and `static/` folders **relative to this file**.

> ⚠️ **Important**: This line must come before any routes are defined.

---

## 3. The Posts Data Structure

```python
posts = [
    {'id': 0, 'usrname': '@juan', 'usrimg': 'user.jpg', 'img': 'img1.jpg',
     'date': '1 day ago', 'post': 'Lorem ipsum ...'},
    {'id': 1, 'usrname': '@luigi', 'usrimg': 'user.jpg', 'img': 'img2.jpg',
     'date': '4 days ago', 'post': 'Lorem ipsum ...'},
    {'id': 2, 'usrname': '@alberto', 'usrimg': 'user.jpg', 'img': 'img3.jpg',
     'date': '2 weeks ago', 'post': 'Lorem ipsum ...'}
]
```

- `posts` is a Python **list** of **dictionaries** — the in-memory "database" for this app.
- Each dictionary represents one post with these keys:

| Key | Type | Description |
|---|---|---|
| `id` | `int` | Unique numeric identifier (used in the URL) |
| `usrname` | `str` | The author's username |
| `usrimg` | `str` | Filename of the profile picture in `static/images/` |
| `img` | `str` | Filename of the post image in `static/images/` |
| `date` | `str` | Human-readable publication date |
| `post` | `str` | The body text of the post |

> ⚠️ **Important**: The `id` values match the **list index** (0, 1, 2). This is relied upon in the `single_post` route — see Section 6.

---

## 4. The Homepage Route

```python
@app.route('/')
def home():
    return render_template('home.html', posts=posts)
```

### How routes work

- `@app.route('/')` is a **decorator** — it tells Flask: *"when a browser requests the URL `/`, call the function below it"*.
- `def home():` is the **view function** — the logic that runs for that URL.
- `render_template('home.html', posts=posts)` does two things:
  1. Loads `templates/home.html`
  2. Passes the `posts` list into the template as a Jinja variable also called `posts`

Inside `home.html` you can then iterate with:
```jinja2
{% for post in posts %}
  <p>{{ post.usrname }}</p>
{% endfor %}
```

---

## 5. The About Page Route

```python
@app.route('/about')
def about():
    p_developers = [
        {'id': 1234, 'name': 'Juan Pablo Sáenz', 'devimg': 'user.jpg',
            'quote': 'A well-known quote...', 'quoteAuthor': 'First quote author'},
        {'id': 5678, 'name': 'Luigi De Russis', 'devimg': 'user.jpg',
            'quote': 'A well-known quote...', 'quoteAuthor': 'Second quote author'},
        {'id': 9012, 'name': 'Alberto Monge Roffarello', 'devimg': 'user.jpg',
            'quote': 'A well-known quote...', 'quoteAuthor': 'Third quote author'}
    ]
    return render_template('about.html', developers=p_developers)
```

- URL `/about` maps to the `about()` function.
- `p_developers` is a **local** list of dicts — it's defined inside the function because it only belongs to this page.
- Each developer dict has: `id`, `name`, `devimg`, `quote`, `quoteAuthor`.
- The list is passed to `about.html` as the variable `developers`.

---

## 6. The Dynamic Post Route ⭐ (Lab 5 Core Feature)

```python
@app.route('/posts/<int:id>')
def single_post(id):
    post = posts[id]
    return render_template('post.html', post=post)
```

This is the most important new concept in Lab 5.

### Breaking it down

```
/posts/<int:id>
       ^^^^^^^^
       Dynamic segment — a variable part of the URL
```

| Part | Meaning |
|---|---|
| `/posts/` | Fixed, literal part of the URL |
| `<int:id>` | A **URL variable** — Flask captures whatever integer is here |
| `int:` | A **converter** — Flask automatically converts the captured string to a Python `int` |

- When a user visits `/posts/0`, Flask calls `single_post(id=0)`.
- When a user visits `/posts/2`, Flask calls `single_post(id=2)`.
- `post = posts[id]` retrieves the dictionary at index `id` from the global `posts` list.
- Only the matching post is passed to the template.

### URL converters available in Flask

| Converter | Type |
|---|---|
| `<int:x>` | Integer |
| `<float:x>` | Float |
| `<string:x>` | String (default) |
| `<path:x>` | String including slashes |

> ⚠️ **Limitation**: If someone visits `/posts/99` and there is no index 99, Python raises an `IndexError`. A production app should add error handling:
> ```python
> from flask import abort
> if id >= len(posts):
>     abort(404)
> ```

---

## 7. Running the Application

```python
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
```

| Part | Meaning |
|---|---|
| `if __name__ == "__main__"` | Only run the server if this file is executed directly (not imported) |
| `host='0.0.0.0'` | Listen on all network interfaces (makes it reachable on your local network) |
| `port=3000` | Serve the app on port 3000 — visit `http://localhost:3000` |
| `debug=True` | Enables the debugger and **auto-reloads** the server when you save a file |

> ⚠️ **Important**: Never use `debug=True` in a production deployment — it exposes internals.

---

## 8. Folder Structure Required

```
project/
├── app.py                     ← this file
├── templates/
│   ├── base.html              ← base template (navbar + aside)
│   ├── home.html              ← extends base, shows post feed
│   ├── post.html              ← extends base, shows one post
│   └── about.html             ← extends base, shows developers
└── static/
    ├── css/
    │   └── style.css
    └── images/
        ├── user.jpg
        ├── img1.jpg
        ├── img2.jpg
        └── img3.jpg
```

Flask automatically looks for templates in `templates/` and static files in `static/`.

---

## 9. How the Pieces Connect — Request Flow

```
Browser visits /posts/1
        │
        ▼
Flask matches @app.route('/posts/<int:id>')
        │
        ▼
single_post(id=1) is called
        │
        ▼
post = posts[1]  →  {'id':1, 'usrname':'@luigi', ...}
        │
        ▼
render_template('post.html', post=post)
        │
        ▼
Jinja fills {{ post.usrname }}, {{ post.img }}, etc.
        │
        ▼
Finished HTML is sent back to the browser
```

---

## 10. Key Flask Concepts Summary

| Concept | Syntax | Purpose |
|---|---|---|
| App creation | `Flask(__name__)` | Creates the app |
| Static route | `@app.route('/about')` | Fixed URL |
| Dynamic route | `@app.route('/posts/<int:id>')` | URL with variable |
| Render template | `render_template('file.html', key=value)` | Serve HTML with data |
| Template folder | `templates/` | Where Flask looks for HTML |
| Static folder | `static/` | Where CSS, images, JS live |
| Debug mode | `debug=True` | Auto-reload + error pages |