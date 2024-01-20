from datetime import date
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StudentSubjectDetails(models.Model):
    _name = "course.details"
    _description = "Information about subject which student give exam"

    students = fields.Char(string="Student")
    course_name = fields.Selection(
        [
            ("mca", "MCA"),
            ("mscit", "MSCIT"),
            ("mba", "MBA"),
            ("llb", "LLB"),
        ],
        "Select course",
    )
