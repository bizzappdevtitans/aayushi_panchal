from datetime import date
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class CourseDetails(models.Model):
    _name = "course.details"
    _description = "Information about subject which student give exam"
    _rec_name = "course_name"

    faculty_course = fields.Many2one("faculty.details", "Course faculty")
    course_class = fields.Many2one("class.details", "Class course")
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
    year = fields.Integer(string="Course year")

    course_no = fields.Char(
        string="Course Reference",
        required=True,
        readonly=True,
        copy=False,
        index=True,
        default=lambda self: _("New"),
    )

    @api.model
    def create(self, vals):
        if vals.get("course_no", "New") == "New":
            vals["course_no"] = (
                self.env["ir.sequence"].next_by_code("course.details") or "New"
            )

        result = super(CourseDetails, self).create(vals)
        return result
