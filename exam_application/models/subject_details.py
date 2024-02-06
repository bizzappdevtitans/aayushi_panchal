from datetime import date
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StudentSubjectDetails(models.Model):
    _name = "student.subject.details"
    _description = "Information about subject which student give exam"
    _rec_name = "subject_name"

    students = fields.Many2many("student.details", string="Student")
    subject_name = fields.Selection(
        [
            ("maths", "Maths"),
            ("english", "English"),
            ("science", "Science"),
            ("gujrati", "Gujrati"),
        ],
        "Select Subject",
    )
