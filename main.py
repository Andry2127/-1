
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.get("/")
def index():
    question = "Виберіть свій тур з України до:"
    fields = ["Турція","Греція","Англія","Іспанія","Америка","Бразилія","Щавельленд","Гаваїщькеря","Казахстан"]
    return render_template("index.html", question=question, fields=fields)


@app.get("/add_vote/")
def add_vote():
    vote = request.args.get("vote")
    with open("data/answers.txt", "a", encoding="utf-8") as file:
        file.write(vote + "\n")

    return redirect(url_for("answers"))



@app.get("/answers/")
def answers():
    with open("data/answers.txt", "r", encoding="utf-8") as file:
        fields = file.readlines()
    return render_template("answers.html", fields=fields)





if __name__ == "__main__":
    app.run(debug=True)