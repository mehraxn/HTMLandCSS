# Why the HTML is Styled Only When Running `app.py`

## Important standalone point

In a Flask web app, the files inside the `templates` folder are not meant to be opened directly by double-clicking them.

They are template files, not normal standalone HTML files.

That means they often contain FlaskJinja code such as

```html
{{ url_for('static', filename='cssstyle.css') }}
```

or

```html
{% extends base.html %}
{% block content %}
{% endblock %}
```

A normal browser does not understand this code.

The browser only understands normal HTML, CSS, and JavaScript.

So when you open a template file directly, like this

```text
file...templatesindex.html
```

Flask is not running. Because of that

 `url_for()` is not converted into the real CSS path.
 `{% extends base.html %}` is not processed.
 `{% block content %}` is not processed.
 `{{ variable }}` values are not replaced.
 The CSS file may not be found.
 The page may appear unstyled or broken.

But when you run

```bash
python app.py
```

and open the page from the Flask server, for example

```text
http127.0.0.15000
```

Flask processes the template first.

For example, Flask changes this

```html
link rel=stylesheet href={{ url_for('static', filename='cssstyle.css') }}
```

into this

```html
link rel=stylesheet href=staticcssstyle.css
```

Now the browser can understand the path and load the CSS correctly.

## Simple rule

If an HTML file uses FlaskJinja syntax like

```html
{{ ... }}
```

or

```html
{% ... %}
```

then do not open that HTML file directly.

Instead, run the Flask app

```bash
python app.py
```

and open the website using the Flask URL

```text
http127.0.0.15000
```

## Short explanation

Opening the HTML directly means

```text
Browser → raw template file → no Flask → no Jinja processing → CSS may not load
```

Running the app means

```text
Browser → Flask server → template processed → CSS path generated → styled page shown
```

## Final idea

Your styled page appears only when running `app.py` because Flask must process the template and generate the correct final HTML before the browser can display it properly.
