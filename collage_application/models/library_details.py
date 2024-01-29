from datetime import date
from odoo import fields, models


class Library(models.Model):
    _name = "library"
    _description = "library"

    library_name = fields.Char(string="library name")
    student_name =fields.Char(string="Student Name")
    library_date = fields.Datetime("Date time")
    library_image = fields.Binary("Library Image")
