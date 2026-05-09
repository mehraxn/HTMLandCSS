from flask import Flask, render_template, abort

app = Flask(__name__)

# This is our small fake database.
# In a bigger app, these posts would usually come from a real database.
posts = [
    {
        "id": 1,
        "username": "alberto",
        "publication_date": "April 27, 2025",
        "text": "Today I worked on the homepage layout and made the post cards easier to read.",
        "profile_image": "user.jpg",
        "post_image": "img1.jpg",
    },
    {
        "id": 2,
        "username": "luigi",
        "publication_date": "April 25, 2025",
        "text": "I tested the page on a smaller screen and changed the spacing between the sections.",
        "profile_image": "user.jpg",
        "post_image": "img2.jpg",
    },
    {
        "id": 3,
        "username": "juan",
        "publication_date": "April 25, 2025",
        "text": "I checked the images, profile pictures, and links between the feed and the post page.",
        "profile_image": "user.jpg",
        "post_image": "img3.jpg",
    },
]


def get_post(post_id):
    for post in posts:
        if post["id"] == post_id:
            return post
    return None


@app.route("/")
def index():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = get_post(post_id)

    if post is None:
        abort(404)

    return render_template("post.html", post=post)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
