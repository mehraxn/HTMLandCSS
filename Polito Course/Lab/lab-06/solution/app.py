import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)

# Allowed image extensions for upload
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}

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


def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def get_usernames():
    """Return the list of unique usernames currently in the posts list."""
    seen = set()
    usernames = []
    for post in posts:
        if post["username"] not in seen:
            seen.add(post["username"])
            usernames.append(post["username"])
    return usernames


@app.route("/", methods=["GET", "POST"])
def index():
    errors = []
    form_data = {}  # preserve form values on validation error

    if request.method == "POST":
        # --- Collect raw form values ---
        username = request.form.get("username", "").strip()
        text = request.form.get("text", "").strip()
        date_str = request.form.get("date", "").strip()
        image_file = request.files.get("image")

        # Preserve values so the modal can re-open with them on error
        form_data = {"username": username, "text": text, "date": date_str}

        # --- Validate username ---
        valid_usernames = get_usernames()
        if not username or username not in valid_usernames:
            errors.append("Please select a valid username.")

        # --- Validate text ---
        if not text:
            errors.append("Post content is required.")
        elif len(text) < 30:
            errors.append(
                f"Post content is too short ({len(text)} chars). Minimum is 30 characters."
            )
        elif len(text) > 200:
            errors.append(
                f"Post content is too long ({len(text)} chars). Maximum is 200 characters."
            )

        # --- Validate date ---
        if not date_str:
            errors.append("Please select a publication date.")
        else:
            try:
                datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                errors.append("Invalid date format.")

        # --- Validate image (optional but must be a valid type if provided) ---
        post_image_path = None
        if image_file and image_file.filename:
            if not allowed_file(image_file.filename):
                errors.append(
                    "Unsupported image format. Allowed: png, jpg, jpeg, gif, webp."
                )
            else:
                filename = secure_filename(image_file.filename)
                save_dir = os.path.join(app.static_folder, "images")
                os.makedirs(save_dir, exist_ok=True)
                image_file.save(os.path.join(save_dir, filename))
                post_image_path = f"/static/images/{filename}"

        # --- If all validations pass, add the post and redirect ---
        if not errors:
            new_post = {
                "username": username,
                "publication_date": date_str,
                "text": text,
                "profile_image": "/static/images/user.jpg",
                "post_image": post_image_path,
            }
            posts.insert(0, new_post)  # newest post shown first
            return redirect(url_for("index"))

    return render_template(
        "index.html",
        posts=posts,
        usernames=get_usernames(),
        active_page="home",
        errors=errors,
        form_data=form_data,
    )


@app.route("/about")
def about():
    return render_template("about.html", developers=developers, active_page="about")


if __name__ == "__main__":
    app.run(debug=True)
