from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = "wtf_secret_key"

class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Submit")

@app.route("/", methods=["GET", "POST"])
def index():
    form = UserForm()
    msg = ""
    if form.validate_on_submit():
        msg = f"Valid submission for {form.name.data} ({form.email.data})"
    return render_template("wtf_form.html", form=form, msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
