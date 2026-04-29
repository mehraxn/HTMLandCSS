from flask import Flask, render_template

app = Flask(__name__)

# The data below is sent from Flask to the HTML pages.
# Each dictionary is one post.
posts = [
    {
        "username": "luigi",
        "publication_date": "2 days ago",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tristique lobortis molestie. Donec laoreet iaculis nibh sed viverra. Nunc condimentum tincidunt mollis. Curabitur gravida aliquam urna, ac vulputate felis condimentum at. Sed sapien lectus, aliquam ac ornare sed, dapibus pulvinar ligula.",
        "profile_image": "/static/images/user.jpg",
        "post_image": "/static/images/img1.jpg",
    },
    {
        "username": "alberto",
        "publication_date": "4 days ago",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tristique lobortis molestie. Donec laoreet iaculis nibh sed viverra. Nunc condimentum tincidunt mollis. Curabitur gravida aliquam urna, ac vulputate felis condimentum at. Sed sapien lectus, aliquam ac ornare sed, dapibus pulvinar ligula.",
        "profile_image": "/static/images/user.jpg",
        "post_image": "/static/images/img2.jpg",
    },
    {
        "username": "juan",
        "publication_date": "1 week ago",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tristique lobortis molestie. Donec laoreet iaculis nibh sed viverra. Nunc condimentum tincidunt mollis.",
        "profile_image": "/static/images/user.jpg",
        "post_image": None,
    },
]

# Each dictionary is one developer shown on the about page.
developers = [
    {
        "name": "Luigi Verdi",
        "role": "Front-end Developer",
        "bio": "Passionate about design and usability, Luigi works on the user interface and the visual experience of the application.",
        "photo": "/static/images/img1.jpg",
    },
    {
        "name": "Alberto Rossi",
        "role": "Back-end Developer",
        "bio": "Skilled in Python and Flask, Alberto manages the server-side logic and the data architecture of the project.",
        "photo": "/static/images/img2.jpg",
    },
]


@app.route("/")
def index():
    return render_template("index.html", posts=posts, active_page="home")


@app.route("/about")
def about():
    return render_template("about.html", developers=developers, active_page="about")


if __name__ == "__main__":
    app.run(debug=True)
