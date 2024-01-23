from odoo import models, fields


class ClassDetails(models.Model):
    _name = "class.details"
    _description = "Class Information"
    _rec_name = "class_name"

    class_name = fields.Char(
        "Class name", help="Enter class name like -[10th-B]", default="10th-A"
    )
    class_faculty = fields.Many2one("faculty.details", string="Class facility")
    strenth_of_class = fields.Integer(string="strenth of a class")
    room_number = fields.Integer("Room number")
    students = fields.One2many("student.details", "student_class", "Students")
    course = fields.One2many("course.details", "course_name", "Course")
