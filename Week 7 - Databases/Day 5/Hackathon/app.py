import flask
import json
from flask_wtf import FlaskForm
import wtforms

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = "super_secret_key"

# Form for adding a class group to the DB
class Add_Class_Details(FlaskForm):
	name = wtforms.StringField("Class Name:", [wtforms.validators.required()])
	teacher = wtforms.StringField("Teacher:", [wtforms.validators.required()])
	year = wtforms.StringField("Year Group:", [wtforms.validators.required()])
	image = wtforms.StringField("Image URL:", [wtforms.validators.required()])

# Form for adding a pupil to the DB
class Add_Pupil_Details(FlaskForm):
	first_name = wtforms.StringField("First Name:", [wtforms.validators.required()])
	last_name = wtforms.StringField("Last Name:", [wtforms.validators.required()])
	birth_date = wtforms.StringField("Birth Date:", [wtforms.validators.required()])

# Form for adding IEP targets
class Add_Target(FlaskForm):
	area = wtforms.StringField("Subject Area:", [wtforms.validators.required()])
	target = wtforms.StringField("Target:", [wtforms.validators.required()])
	provision = wtforms.StringField("Provision:", [wtforms.validators.required()])
	status = wtforms.SelectField("Status:", [wtforms.validators.required()], choices=[('New Target', 'New Target'), ('Not Met', 'Not Met'), ('Partially Met', 'Partially Met'), ('Met', 'Met')])

# Form for adding a pupil to the DB
class Add_Achievement(FlaskForm):
	date = wtforms.StringField("Date:", [wtforms.validators.required()])
	title = wtforms.StringField("Title:", [wtforms.validators.required()])
	comment = wtforms.StringField("Comment:", [wtforms.validators.required()])

# Home page
@app.route('/')
def index():
	html = flask.render_template("index.html")
	return html

# Shows all class groups with links to details, Options to add/edit class.
@app.route('/classgroups', methods=['GET', 'POST'])
def class_groups():
	with open("db.json", "r") as f:
		data = json.load(f)
	add_class_form = Add_Class_Details()
	class_list = data["classes"]
	if add_class_form.validate_on_submit():
		new_class = {
			"class_name": add_class_form.name.data,
			"teacher": add_class_form.teacher.data,
			"year_group": add_class_form.year.data,
			"image": add_class_form.image.data,
			"pupils": []
		}
		class_list.append(new_class)
		with open('db.json', 'w') as f:
			json.dump(data, f)
			return flask.redirect(flask.url_for("class_groups"))
	html = flask.render_template("classgroups.html", data = data, add_class_form=add_class_form)
	return html

# Shows all pupils for a specific class group with links to pupil details / pathway plan. Option to add pupil.
@app.route('/classgroups/<class_name>', methods=['GET', 'POST'])
def classgroups(class_name):
	with open("db.json", "r") as f:
		data = json.load(f)
	add_pupil_form = Add_Pupil_Details()
	for index in data["classes"]:
		if index["class_name"] == class_name:
			class_index = index
	pupil_list = class_index["pupils"]
	if add_pupil_form.validate_on_submit():
		new_pupil = {
			"first_name": add_pupil_form.first_name.data,
			"last_name": add_pupil_form.last_name.data,
			"birth_date": add_pupil_form.birth_date.data,
			"targets": [],
			"notes": []
		}

		pupil_list.append(new_pupil)
		with open('db.json', 'w') as f:
			json.dump(data, f)
			return flask.redirect(flask.url_for("classgroups", class_name=class_name))

	html = flask.render_template("classpupils.html", class_index = class_index, data=data, add_pupil_form = add_pupil_form)
	return html


# Shows pupil pathway plan details
@app.route('/classgroups/<class_name>/<first_name><last_name>', methods=['GET', 'POST'])
def IEP(class_name, first_name, last_name):
	with open("db.json", "r") as f:
		data = json.load(f)
	add_target_form = Add_Target()
	add_achievement_form = Add_Achievement()
	for index in data["classes"]:
		if index["class_name"] == class_name:
			class_index = index
	for pupil in class_index["pupils"]:
		if pupil["first_name"] + pupil["last_name"] == first_name + last_name:
			pupil_index = pupil

	target_list = pupil_index["targets"]
	if add_target_form.validate_on_submit():
		new_target = {
			"target_id": len(target_list)+1,
			"area": add_target_form.area.data,
			"target": add_target_form.target.data,
			"provision": add_target_form.provision.data,
			"status": add_target_form.status.data
		}
		target_list.append(new_target)
		with open('db.json', 'w') as f:
			json.dump(data, f)
			return flask.redirect(flask.url_for("IEP", class_name = class_name, first_name = first_name, last_name = last_name))

	achievement_list = pupil_index["notes"]
	if add_achievement_form.validate_on_submit():
		new_achievement = {
			"date": add_achievement_form.date.data,
			"title": add_achievement_form.title.data,
			"comment": add_achievement_form.comment.data,
		}
		achievement_list.append(new_achievement)
		with open('db.json', 'w') as f:
			json.dump(data, f)
			return flask.redirect(flask.url_for("IEP", class_name = class_name, first_name = first_name, last_name = last_name))

	html = flask.render_template("IEP.html", class_index=class_index, pupil_index=pupil_index, data=data, add_target_form = add_target_form, add_achievement_form=add_achievement_form)
	return html

# DATA summary page
@app.route('/data')
def data():
	with open("db.json", "r") as f:
		data = json.load(f)

	for class_index in data["classes"]:
		class_index["stats"] = {}
		class_index["stats"]["pupil_count"] = len(class_index["pupils"])
		class_index["stats"]["target_count"] = 0
		class_index["stats"]["met_targets"] = 0
		class_index["stats"]["partially_met_targets"] = 0
		class_index["stats"]["unmet_targets"] = 0
		class_index["stats"]["new_targets"] = 0

		for pupil in class_index["pupils"]:
			pupil["stats"] = {}
			pupil["stats"]["target_count"] = len(pupil["targets"])
			class_index["stats"]["target_count"] += pupil["stats"]["target_count"]
			pupil["stats"]["met_targets"] = 0
			pupil["stats"]["partially_met_targets"] = 0
			pupil["stats"]["unmet_targets"] = 0
			pupil["stats"]["new_targets"] = 0
			for target in pupil ["targets"]:
				if target ["status"] == "Met":
					pupil["stats"]["met_targets"] += 1
					class_index["stats"]["met_targets"] += 1
				elif target["status"] == "Partially Met":
					pupil["stats"]["partially_met_targets"] += 1
					class_index["stats"]["partially_met_targets"] += 1
				elif target["status"] == " Unmet":
					pupil["stats"]["unmet_targets"] += 1
					class_index["stats"]["unmet_targets"] += 1
				elif target["status"] == "New Target":
					pupil["stats"]["new_targets"] += 1
					class_index["stats"]["new_targets"] += 1

	with open('db.json', 'w') as f:
		json.dump(data, f)

	html = flask.render_template("data.html", data = data)
	return html


# DELETE class details from DB (includes are you sure prompt alert within html element onclick)
@app.route('/classgroups/delete/<class_name>')
def delete(class_name):
    with open("db.json", "r") as f:
        data = json.load(f)
    for index in range (len(data["classes"])):
        if data["classes"][index]["class_name"] == class_name:
            data["classes"].pop(index)

    with open('db.json', 'w') as f:
        json.dump(data, f)
        return flask.redirect(flask.url_for("class_groups"))



if __name__ == "__main__":
	app.secret_key = "super_secret_key"
	app.run(debug=True)

