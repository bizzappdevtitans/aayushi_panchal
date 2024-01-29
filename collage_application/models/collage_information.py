from odoo import fields, models


class CollegeLocation(models.Model):
    _name = "college.information"
    _description = "College information"
    _rec_name = "country_id"

    college_name=fields.Char(string="Collage name")
    country_id = fields.Char(string="Country")
    description = fields.Text(string="Description")
    image = fields.Image(string="Image")
    location = fields.Char(string="Location")
    phone = fields.Char(string="Phone")
    email = fields.Char(
        string="Email"
    )
    about_us = fields.Text(string="About Us")
