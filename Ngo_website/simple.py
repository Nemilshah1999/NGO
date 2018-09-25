from flask import Flask,render_template,request,redirect
import sqlite3 as sql

app=Flask(__name__, template_folder="")
con = sql.connect("ngo.db",check_same_thread=False)
cur = con.cursor()

@app.route('/')
def first_page():
	return render_template("first_page.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/issue')
def issue():
	return render_template("issue.html")

@app.route('/project')
def project():
	return render_template("project.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route('/donate',methods=['GET','POST'])
def donate():
	if request.method=='GET':
		return render_template("donate.html")
	else:
		name=request.form['Name']
		email=request.form['Email']
		phone=request.form['Phone']
		add=request.form['Addr']
		aadhar=request.form['Aadhar']
		cur.execute("INSERT INTO Donate (name,email,phone,address,aadhar) VALUES (?,?,?,?,?)",(name,email,phone,add,aadhar))
		con.commit()
		cur.close()
		return render_template("new.html",name=name)