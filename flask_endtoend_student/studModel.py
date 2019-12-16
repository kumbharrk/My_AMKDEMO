from flask_endtoend_student.studAppConfig import *


class student(db.Model):
    __tablename__='stud_info'
    studRoll=db.Column('studrn',db.Integer(),primary_key=True)
    studName=db.Column('studnm',db.String(100),nullable=False)
    studMark=db.Column('studmark',db.Integer())

    def __str__(self):
        self.__dict__.pop('_sa_instance_state')
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)

#if __name__ == '__main__':
    #db.create_all()