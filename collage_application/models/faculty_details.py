from odoo import models, fields, api


class TeacherDetails(models.Model):
    _name = "faculty.details"
    _description = "faculty information"

    faculty_name = fields.Char(string="Faculty name")
    mobile_no = fields.Char(string="Mobile No")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")
    email = fields.Char(string="Email id")
    image = fields.Binary("Profile photo")
    experience = fields.Char("experience")
    document = fields.Binary("Upload your document")

    faculty_id = fields.Many2one(comodel_name="student.details", string="Student name")
    student_id = fields.One2many("student.details", "faculty", "StudentName")
    # name_ids = fields.Many2many(comodel_name="student", string="Students")

    _sql_constraints = [
        (
            "unique_faculty_name_",
            "unique (faculty_name)",
            "Faculty name must be unique, this name is already exist."
        )
    ]

