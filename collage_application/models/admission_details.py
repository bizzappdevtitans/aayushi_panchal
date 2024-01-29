from odoo import fields, api, models
from odoo.exceptions import ValidationError


class Admission(models.Model):
    _name = "admission.details"
    _description = "admission details"
    _rec_name = "full_name"

    enrollment_num = fields.Integer(string="Enrollment number", store=True)
    full_name = fields.Char(string="Full Name")
    name = fields.Char(string="Name", copy="False")
    lastname = fields.Char(string="Last Name")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")
    contact_no = fields.Char(string="contact_no")
    date_of_birth = fields.Date("Date of Birth")
    course = fields.Char(string="Select Course:")
    pr_result = fields.Float(string="Previous Standard/Course Percentage%")
    course_name = fields.Selection(
        [
            ("mca", "MCA"),
            ("mscit", "MSCIT"),
            ("mba", "MBA"),
            ("llb", "LLB"),
        ],
        "Select course",
    )

    # perform object button
    def action_test(self):
        print("hello student, welcome to collage campus!!!!")

    _sql_constraints = [
        (
            "name_uniq",
            "check(Length(contact_no)=10)",
            "You can't enter less than 10 digits and more than 10 digits",
        )
    ]
