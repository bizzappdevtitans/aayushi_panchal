from datetime import date
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StudentDetails(models.Model):
    _name = "student.details"
    _description = "student information"
    _inherit = ["mail.thread", "mail.activity.mixin"]
