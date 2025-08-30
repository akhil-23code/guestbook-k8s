from flask import Flask, render_template, request, redirect
import redis

app = Flask(__name__)
# Connect to redis-leader service inside cluster
r = redis.Redis(host="redis-leader", port=6379, decode_responses=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            r.lpush("guestbook", name)
        return redirect("/")
    entries = r.lrange("guestbook", 0, -1)
    return render_template("index.html", entries=entries)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

