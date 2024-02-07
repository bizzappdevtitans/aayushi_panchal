from odoo import fields, models


class CollegeInformation(models.Model):
    _name = "college.information"
    _description = "college information"
    _rec_name = "college_name"

    college_name = fields.Char(string="Collage name :")
    country_id = fields.Char(string="Country :")
    description = fields.Text(string="Description :")
    image = fields.Image(string="Image :")
    location = fields.Char(string="Location :")
    phone = fields.Char(string="Phone :")
    email = fields.Char(string="Email :")
    about_us = fields.Text(string="About Us :")
