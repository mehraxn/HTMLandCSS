# Campus Stories - Image Path Problem and Fix

## Project context

This project is a static front-end web application for the midterm assignment. The assignment asks us to redesign a social network  blog-style application using HTML, CSS, and Bootstrap.

The project is called Campus Stories. It is a student story-sharing website inspired by the clean card-based style of the Google Workspace “50 States, 50 Stories” page.

The project includes pages such as

 `index.html`
 `explore.html`
 `post.html`
 `profile.html`

It also includes CSS and images.

---

## The problem

At first, the images were not showing in the browser.

The reason was that the project structure and the image paths were not matching correctly.

The earlier project was organized more like a Flask project

```text
campus-stories
│
├── templates
│   ├── index.html
│   ├── explore.html
│   ├── post.html
│   └── profile.html
│
├── static
│   ├── css
│   │   └── style.css
│   └── images
│       ├── campus-hero.png
│       ├── library-vibes.png
│       ├── first-day-vibes.png
│       ├── all-nighter-stories.png
│       ├── tech-fest-2024.png
│       ├── quiet-study-corner.png
│       ├── avatar-maya.png
│       ├── avatar-aj.png
│       └── sketch.jpg
│
└── README.md
```

This structure is common when using Flask because Flask normally reads HTML files from the `templates` folder and static files from the `static` folder.

However, the midterm assignment does not require Flask. It asks for a front-end project made with

```text
HTML + CSS + Bootstrap
```

So the project should work as a normal static website when we open the HTML files in the browser.

---

## Why the images did not show

Some image paths were written in a way that only works with Flask, for example

```html
img src={{ url_for('static', filename='imagesquiet-study-corner.png') }} alt=Campus study corner
```

This syntax is called Jinja syntax. It works only when Flask is running the website.

If we open the file directly in the browser, like this

```text
file...templatespost.html
```

then the browser does not understand this part

```html
{{ url_for(...) }}
```

Because of that, the image path becomes invalid and the image does not appear.

Another problem was the folder location. If an HTML file is inside the `templates` folder and the image is inside `staticimages`, the image path needs to go one folder back first

```html
img src=..staticimagesquiet-study-corner.png alt=Campus study corner
```

But this kind of path can become confusing for a simple static midterm project.

---

## The main decision

Because the assignment is about HTML, CSS, and Bootstrap, we decided to make the final project a fully static website.

That means

 no Flask is needed
 no `templates` folder is needed
 no `url_for()` is needed
 no Jinja syntax is needed
 the HTML files can be opened directly in the browser

This is simpler and safer for the midterm assignment.

---

## The final fixed structure

The project was reorganized into a simpler static structure

```text
campus_stories_final_static
│
├── index.html
├── explore.html
├── post.html
├── profile.html
├── README.md
│
├── css
│   └── style.css
│
└── images
    ├── campus-hero.png
    ├── library-vibes.png
    ├── first-day-vibes.png
    ├── all-nighter-stories.png
    ├── tech-fest-2024.png
    ├── quiet-study-corner.png
    ├── avatar-maya.png
    ├── avatar-aj.png
    └── sketch.jpg
```

This structure is easier because all main HTML pages are in the root project folder.

So from `index.html`, `post.html`, `explore.html`, or `profile.html`, the image folder is easy to access

```html
img src=imagesquiet-study-corner.png alt=Campus study corner
```

And the CSS file is easy to access

```html
link rel=stylesheet href=cssstyle.css
```

---

## What we changed

### 1. Moved HTML files out of `templates`

Before

```text
templatesindex.html
templatesexplore.html
templatespost.html
templatesprofile.html
```

After

```text
index.html
explore.html
post.html
profile.html
```

This makes the project work like a normal static website.

---

### 2. Moved CSS out of `staticcss`

Before

```text
staticcssstyle.css
```

After

```text
cssstyle.css
```

The CSS link became simpler

```html
link rel=stylesheet href=cssstyle.css
```

---

### 3. Moved images out of `staticimages`

Before

```text
staticimages
```

After

```text
images
```

The image paths became simpler

```html
img src=imagescampus-hero.png alt=Campus students
```

---

### 4. Removed FlaskJinja paths

Before

```html
img src={{ url_for('static', filename='imagesquiet-study-corner.png') }} alt=Campus study corner
```

After

```html
img src=imagesquiet-study-corner.png alt=Campus study corner
```

This is important because the final project is static HTML, not Flask.

---

### 5. Replaced placeholder boxes with real images

Some parts of the website had placeholder image boxes instead of real images.

For example, the post page showed a design-like box instead of a real image.

We replaced those placeholder parts with real image tags

```html
img src=imagesquiet-study-corner.png class=post-header-img mb-5 alt=Campus study corner
```

This allowed the real imported images to appear on the page.

---

### 6. Kept the same visual design

The design style was kept the same

 clean Google-inspired layout
 large hero section
 rounded story cards
 categoryfilter buttons
 responsive Bootstrap grid
 modern spacing
 simple student project style

The goal was not to redesign everything again. The goal was to fix the structure and paths so the images show correctly in the browser.

---

## Example of the correct image path

Because the final files are organized like this

```text
post.html
imagesquiet-study-corner.png
```

The correct image path inside `post.html` is

```html
img src=imagesquiet-study-corner.png alt=Campus study corner
```

Not this

```html
img src=..staticimagesquiet-study-corner.png alt=Campus study corner
```

And not this

```html
img src={{ url_for('static', filename='imagesquiet-study-corner.png') }} alt=Campus study corner
```

---

## How to open the final project

After extracting the final ZIP file, open

```text
campus_stories_final_staticindex.html
```

You can double-click `index.html`, or open it with a browser.

The project should work without running Flask.

The images should show because the paths now point directly to the local `images` folder.

---

## Final result

The problem was caused by using a Flask-style folder structure and FlaskJinja image paths in a project that needed to work as a static HTMLCSSBootstrap website.

We fixed it by converting the project to a static structure and changing the paths.

Final result

 HTML files are in the main folder
 CSS is inside `cssstyle.css`
 images are inside the `images` folder
 image paths use normal HTML paths
 no Flask is required
 no `url_for()` is used
 pages can be opened directly in the browser
 images display correctly

This final structure is better for the midterm because it clearly matches the assignment requirement HTML, CSS, and Bootstrap.
