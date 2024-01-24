from odoo import fields, models


class CollegeLocation(models.Model):
    _name = 'college.information'
    _description = 'College information'
    _rec_name = 'country_id'

    country_id = fields.Char(string="Country",
                                 placeholder='Country Name')
    description = fields.Text(string='Description',
                              placeholder='Small description of the college')
    image = fields.Image(string='Image',placeholder='Image')
    location = fields.Char(string='Location',placeholder='Location')
    phone = fields.Char(string='Phone',
                        placeholder='Phone number to contact the college')
    email = fields.Char(string='Email',
                        placeholder='Email to contact the college')
    about_us = fields.Text(string='About Us',
                           placeholder='About the college')
