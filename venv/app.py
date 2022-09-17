from flask import render_template, url_for, request, redirect

from models import db, Project, app

@app.route("/")
def index():
    projects = Project.query.all()
    return render_template("index.html", projects=projects)

## How do I add routes to anchor tags? Ex: index#contact

@app.route("/#about")
def about():
    return render_template("about.html")

@app.route("/projects/new", methods = ["GET", "POST"])
def new():
    if request.form:  #Unsure if these are actually being created.
        new_project = Project(title=request.form["title"],
                              completion=request.form["date"],description=request.form["desc"],
                              skills=request.form["skills"], link=request.form["github"])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("projectform.html")

@app.route("/projects/<id>")
def detail():
    return render_template("detail.html", project=project, projects=projects)

@app.route("/projects/<id>/edit")
def edit():
    pass

@app.route("/projects/<id>/delete")
def delete():
    pass

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=8000, host="127.0.0.1")