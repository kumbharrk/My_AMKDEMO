from flask import render_template,request
from flask_endtoend_student.studAppConfig import app
from flask_endtoend_student.studModel import*

def get_list_of_emps():
    T = student.query.all()
    #emps.sort(key=logic_sort,reverse=True)
    return T

@app.route('/')
def stud_info_loading():
    return render_template('studData.html')

'''@app.route('/save',methods=['POST'])
def stud_persist():
    #dictval = dict(**request.form)
    #dictval.pop('studRoll')
    #stud = student(**dictval)
    #stud = student(dictval)
    #db.session.add(stud)
    if request.method=='POST':
        stud=student(studRoll=request.form['studRoll'],
                     studName=request.form['studName'],
                     studMark=request.form['studMark'])

        db.session.add(stud)
        db.session.commit()

    return render_template('studData.html',X=get_list_of_emps())'''

@app.route('/delete',methods=['POST'])
def deletedata():
    if request.method=='POST':
        p1=request.form.get('studRoll')
        x1=student.query.filter_by(studRoll=p1).first()
        print(x1)
        db.session.delete(x1)
        db.session.commit()
        return render_template('studData.html',X=get_list_of_emps())
