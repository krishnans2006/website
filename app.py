from flask import Flask, render_template, redirect, url_for, send_file

from data import get_projects

app = Flask(__name__)


@app.route("/health")
@app.route("/2024kshankar/health")
def health():
    return "OK"


@app.route("/")
@app.route("/2024kshankar/")
def index():
    return redirect(url_for("portfolio"))


@app.route("/linkedin/")
@app.route("/2024kshankar/linkedin/")
def linkedin():
    return render_template("linkedin.html")


@app.route("/portfolio/")
@app.route("/2024kshankar/portfolio/")
def portfolio():
    return render_template("portfolio.html", projects=[[p.to_dict(), p.id] for p in get_projects()], desc="Test!")


@app.route("/resume/")
@app.route("/2024kshankar/resume/")
def resume():
    return send_file("static/resumes/Resume.pdf", download_name="Krishnan_Shankar_Resume.pdf")


@app.errorhandler(404)
def error404(e):
    return render_template("error.html", error=404, exception=e)


@app.errorhandler(500)
def error500(e):
    return render_template("error.html", error=500, exception=e)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
