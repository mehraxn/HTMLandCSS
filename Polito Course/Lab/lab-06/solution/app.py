import os
from datetime import date, datetime

from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(app.static_folder, "images")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}

posts = [
    {
        "id": 0,
        "username": "luigi",
        "publication_date": "2 days ago",
        "text": "This is a sample English post for the EchoNet feed. It talks about sharing updates, connecting with friends, and posting ideas in a simple social web application for this lab exercise.",
        "profile_image": "/static/images/user.jpg",
        "post_image": "/static/images/img1.jpg",
    },
    {
        "id": 1,
        "username": "alberto",
        "publication_date": "4 days ago",
        "text": "Here is another example post written in English. The goal is to keep the same page structure while showing clear content that a user can easily read inside the feed.",
        "profile_image": "/static/images/user.jpg",
        "post_image": "/static/images/img2.jpg",
    },
    {
        "id": 2,
        "username": "juan",
        "publication_date": "1 week ago",
        "text": "This post has no image, so it shows how the card looks when only the profile photo, username, date, and message are displayed.",
        "profile_image": "/static/images/user.jpg",
        "post_image": None,
    },
]

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


def get_usernames():
    usernames = []

    for post in posts:
        if post["username"] not in usernames:
            usernames.append(post["username"])

    return usernames


def get_post(post_id):
    for post in posts:
        if post["id"] == post_id:
            return post

    return None


def get_next_id():
    biggest_id = 0

    for post in posts:
        if post["id"] >= biggest_id:
            biggest_id = post["id"] + 1

    return biggest_id


def get_profile_image(username):
    for post in posts:
        if post["username"] == username:
            return post["profile_image"]

    return "/static/images/user.jpg"


def allowed_file(filename):
    if "." not in filename:
        return False

    file_extension = filename.rsplit(".", 1)[1].lower()
    return file_extension in ALLOWED_EXTENSIONS


def show_home(errors=None, form_data=None):
    if errors is None:
        errors = []

    if form_data is None:
        form_data = {}

    return render_template(
        "index.html",
        posts=posts,
        usernames=get_usernames(),
        active_page="home",
        errors=errors,
        form_data=form_data,
        today=date.today().isoformat(),
    )


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return new_post()

    return show_home()


@app.route("/about")
def about():
    return render_template("about.html", developers=developers, active_page="about")


@app.route("/posts/<int:id>")
def single_post(id):
    post = get_post(id)

    if post is None:
        return redirect(url_for("index"))

    return render_template("post.html", post=post, active_page="home")


@app.route("/posts/new", methods=["GET", "POST"])
def new_post():
    if request.method == "GET":
        return redirect(url_for("index"))

    errors = []

    username = request.form.get("username", "").strip()
    if username == "":
        username = request.form.get("usrname", "").strip()
    username = username.lstrip("@")

    text = request.form.get("text", "").strip()
    if text == "":
        text = request.form.get("post", "").strip()

    selected_date = request.form.get("date", "").strip()
    image_file = request.files.get("image")

    form_data = {
        "username": username,
        "text": text,
        "date": selected_date,
    }

    if username not in get_usernames():
        errors.append("Please select a valid username.")

    if text == "":
        errors.append("Post content is required.")
    elif len(text) < 30:
        errors.append("Post content is too short (" + str(len(text)) + " characters). Minimum is 30 characters.")
    elif len(text) > 200:
        errors.append("Post content is too long (" + str(len(text)) + " characters). Maximum is 200 characters.")

    if selected_date == "":
        errors.append("Please select a publication date.")
    else:
        try:
            post_date = datetime.strptime(selected_date, "%Y-%m-%d").date()

            if post_date < date.today():
                errors.append("The publication date cannot be in the past.")
        except ValueError:
            errors.append("Invalid date format.")

    if image_file is not None and image_file.filename != "":
        if not allowed_file(image_file.filename):
            errors.append("Unsupported image format. Allowed: png, jpg, jpeg, gif, webp.")

    if len(errors) > 0:
        return show_home(errors, form_data)

    post_id = get_next_id()
    image_path = None

    if image_file is not None and image_file.filename != "":
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        filename = secure_filename(image_file.filename)
        name, extension = os.path.splitext(filename)
        filename = "post_" + str(post_id) + "_" + name + extension

        image_file.save(os.path.join(UPLOAD_FOLDER, filename))
        image_path = url_for("static", filename="images/" + filename)

    post = {
        "id": post_id,
        "username": username,
        "publication_date": selected_date,
        "text": text,
        "profile_image": get_profile_image(username),
        "post_image": image_path,
    }

    posts.append(post)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
