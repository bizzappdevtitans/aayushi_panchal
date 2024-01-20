from odoo import fields, api, models
from odoo.exceptions import ValidationError


class Admission(models.Model):
    _name = "admission.details"
    _description = "admission details"

    name = fields.Char(string="Name", copy="False")
    lastname = fields.Char(string="Last Name")
    contact_no = fields.Char(string="contact_no")
    course = fields.Char(string="Select Course:")
    pr_result = fields.Float(string="Previous Standard/Course Percentage%")

    _sql_constraints = [
        (
            "name_uniq",
            "check(Length(contact_no)=10)",
            "You can't enter less than 10 digits and more than 10 digits",
        )
    ]
