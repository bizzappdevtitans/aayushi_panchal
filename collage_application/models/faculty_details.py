from odoo import models, fields, api


class TeacherDetails(models.Model):
    _name = "faculty.details"
    _description = "faculty information"
    _rec_name = "faculty_name"

    faculty_name = fields.Char(string="Faculty name")
    mobile_no = fields.Char(string="Mobile No")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")
    email = fields.Char(string="Email id")
    image = fields.Binary("Profile photo")
    experience = fields.Char("experience")
    document = fields.Binary("Upload your document")

    course_count = fields.Integer(string="Course Count", compute="_compute_course")
    faculty_class =fields.Many2one("class.details",string="Class facility" )
    course = fields.One2many("course.details", "faculty_course", "Course given")

    _sql_constraints = [
        (
            "unique_faculty_name_",
            "unique (faculty_name)",
            "Faculty name must be unique, this name is already exist.",
        )
    ]

    def _compute_course(self):
        for rec in self:
            total_course = len(self.course)
            self.course_count = total_course

    def action_open_course_details(self):
        if self.course_count > 1:
            return{

                "type": "ir.actions.act_window",
                "name": ("faculty_course"),
                "res_model": "course.details",
                "view_mode": "tree,form",
                "domain": [("faculty_course", "=", self.id)],
                "target": "current",
            }
        else:
            return{

                "type": "ir.actions.act_window",
                "name": ("faculty_course"),
                "res_model": "course.details",
                "view_mode": "form",
                "domain": [("faculty_course", "=", self.id)],
                "target": "current",
            }
