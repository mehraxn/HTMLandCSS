from flask import Flask, render_template

app = Flask(__name__)

# Data structure for homepage posts
posts = [
    {
        "username": "Alice",
        "publication_date": "2026-04-01",
        "text": "Welcome to our social network! This is our first post built with Flask and Jinja.",
        "profile_image": "images/profile1.jpg",
        "post_image": "images/post1.jpg",
    },
    {
        "username": "Marco",
        "publication_date": "2026-04-03",
        "text": "We are learning how to separate application data from HTML using Flask templates.",
        "profile_image": "images/profile2.jpg",
        "post_image": "",
    },
    {
        "username": "Sara",
        "publication_date": "2026-04-04",
        "text": "Bootstrap helps us style the interface, while Jinja lets us display dynamic content easily.",
        "profile_image": "images/profile3.jpg",
        "post_image": "images/post2.jpg",
    },
]


@app.route("/")
def home():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    developers = [
        {
            "name": "Alice",
            "role": "Front-end Developer",
            "bio": "Works on the layout, styles, and user experience of the social network.",
            "image": "images/dev1.jpg",
        },
        {
            "name": "Marco",
            "role": "Back-end Developer",
            "bio": "Builds the Flask application, routes, and post management logic.",
            "image": "images/dev2.jpg",
        },
        {
            "name": "Sara",
            "role": "UI Designer",
            "bio": "Designs the visual identity of the platform and improves usability.",
            "image": "images/dev3.jpg",
        },
    ]

    social_link = "https://example.com"

    return render_template(
        "about.html",
        developers=developers,
        social_link=social_link,
    )


if __name__ == "__main__":
    app.run(debug=True)