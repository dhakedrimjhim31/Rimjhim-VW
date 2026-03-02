from flask import Flask, render_template

app = Flask(__name__)

comments = [
    {
        "username": "Simran",
        "comment": "This product is really good!",
        "likes": 120,
        "flagged": False
    },
    {
        "username":"Amit",
        "comment": "This is a stupid product and dumb design.",
        "likes": 30,
        "flagged": True
    },
    {
        "username":"Priya",
        "comment": "Amazing quality!" * 20,
        "likes": 200,
        "flagged": False
    }
]

# Inappropriate words
bad_words = ["dumb", "stupid"]

@app.route("/comments")
def show_comments():

    # Clean comments
    for c in comments:
        c["comment"] = c["comment"].strip()

        for word in bad_words:
            c["comment"] = c["comment"].replace(word, "***")

    total_comments = len(comments)
    total_flagged = len([c for c in comments if c["flagged"]])
    most_liked = max(comments, key=lambda x: x["likes"])
    all_usernames = ", ".join([c["username"].upper() for c in comments])

    return render_template(
        "comments.html",
        comments=comments,
        total_comments=total_comments,
        total_flagged=total_flagged,
        most_liked=most_liked,
        all_usernames=all_usernames
    )

if __name__ == "__main__":
    app.run(debug=True)