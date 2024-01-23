from datetime import date
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StudentSubjectDetails(models.Model):
    _name = "course.details"
    _description = "Information about subject which student give exam"
    _rec_name="course_name"

    faculty_course = fields.Many2one("faculty.details", "Course faculty")
    students = fields.One2many("student.details", "student_course", "Students")
    course_name = fields.Selection(
        [
            ("mca", "MCA"),
            ("mscit", "MSCIT"),
            ("mba", "MBA"),
            ("llb", "LLB"),
        ],
        "Select course",
    )
    year=fields.Integer(string="Course year")

