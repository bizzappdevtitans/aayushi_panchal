from odoo import fields, models


class ClgArea(models.Model):
    _name = "clg.area"
    _description = "Diffrent Collage Areas"

    name = fields.Char(string="Area Name")
    image1 = fields.Image(string="Our Canteen")
