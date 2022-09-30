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
    if request.form:
        new_project = Project(title=request.form["title"],
                              completion=request.form["date"],description=request.form["desc"],
                              skills=request.form["skills"], link=request.form["github"])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("projectform.html")

@app.route("/projects/<id>")
def detail(id):
    project_detail = Project.query.get(id)
    return render_template("detail.html", project_detail = project_detail)

@app.route("/projects/<id>/edit", methods= ["GET", "POST"])
def edit(id):
    project_detail = Project.query.get(id)
    if request.form:
        project_detail.title = request.form["title"]
        project_detail.completion = request.form["date"]
        project_detail.description = request.form["desc"]
        project_detail.skills = request.form["skills"]
        project_detail.link = request.form["github"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("editproject.html", project_detail=project_detail)

@app.route("/projects/<id>/delete")
def delete(id):
    project_detail = Project.query.get(id)
    db.session.delete(project_detail)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=8000, host="127.0.0.1")