
from flask import Flask, render_template_string, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'secret_key_for_demo'

# Фиктивные пользователи (в реальном проекте - из базы данных)
users = {
    "teacher": {"password": "teachpass", "role": "teacher"},
    "student": {"password": "studpass", "role": "student"}

}

# Простая "база данных" оценок
grades = {
    "math": {"student": 4}
}

# HTML шаблоны (упрощённо для демонстрации)
login_template = """
<h2>Login</h2>
<form method="post">
    Username: <input name="username"><br>
    Password: <input name="password" type="password"><br>
    <input type="submit" value="Login">
</form>
"""

dashboard_template = """
<h2>Dashboard ({{ role }})</h2>
<p>Logged in as: {{ username }}</p>
<a href="{{ url_for('logout') }}">Logout</a>
<h3>Grades</h3>
<ul>
{% for subject, grade in grades.items() %}
    <li>{{ subject }}: {{ grade }}</li>
{% endfor %}
</ul>
{% if role == 'teacher' %}
<h3>Change Grade</h3>
<form method="post" action="{{ url_for('change_grade') }}">
    Subject: <input name="subject"><br>
    Grade: <input name="grade" type="number"><br>
    <input type="submit" value="Change">
</form>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = users.get(username)
        if user and user["password"] == password:
            session["username"] = username
            session["role"] = user["role"]
            return redirect(url_for("dashboard"))
        else:
            return "Invalid credentials"
    return render_template_string(login_template)

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template_string(dashboard_template,
                                  username=session["username"],
                                  role=session["role"],
                                  grades={s: grades[s]["student"] for s in grades})

@app.route("/change_grade", methods=["POST"])
def change_grade():
    if "username" not in session or session["role"] != "teacher":
        return "Access denied", 403
    subject = request.form["subject"]
    grade = int(request.form["grade"])
    grades[subject] = {"student": grade}
    return redirect(url_for("dashboard"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
