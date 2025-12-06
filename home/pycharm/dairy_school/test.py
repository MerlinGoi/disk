from flask import Flask

app = Flask(__name__)

html_query = """<!DOCTYPE html>
                <html lang="pl">
                <head>
                    <meta charset="UTF-8">
                    <title>Przychodnia - podgląd bazy</title>
                </head>
                <body>
                    <form action="/aboout" method="POST">
                        <label for="fname">First name:</label>
                        <input type="text" id="fname" name="fname"><br><br>
                        <label for="lname">Last name:</label>
                        <input type="text" id="lname" name="lname"><br><br>
                        <input type="submit" value="Submit">
                    </form>
                </body>
                </html>"""

html_query__about = """<!DOCTYPE html>
                        <html lang="pl">
                        <head>
                            <meta charset="UTF-8">
                            <title>Przychodnia - podgląd bazy</title>
                        </head>
                        <body>
                            <p1> About Us!</p1>
                            <form action="/" method="get">
                                <input type="submit" value="Submit">
                            </form>
                        </body>
                        </html>
                        """

@app.route("/")
def mian():
    return html_query


@app.route("/aboout", methods=["GET", "POST"])
def about():
    return html_query__about

if __name__ == "__main__":
    app.run(debug=True)

