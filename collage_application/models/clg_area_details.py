from datetime import date
from odoo import fields, models


class ClgArea(models.Model):
    _name = "clg.area"
    _description = "Diffrent Collage Areas"

    name= fields.Char(string="Area Name")
    image1 = fields.Image(string="Our Canteen")


# class Lab(models.Model):
#     _name = "lab"
#     _description = "lab"

#     lab_no = fields(string="Lab No")
#     lab_name = fields(string="Lab Name")
#     lab_date = fields.Datetime("Sport_date_time")





# class Sports(models.Model):
#     _name = "sports"
#     _description = "sports"

#     sport_name = fields.Selection(
#         [
#             ("cricket", "Cricket"),
#             ("volleyball", "Volleyball"),
#             ("tennis", "Tennis"),
#             ("golf", "Golf"),
#         ],
#         string="Sorts",
#     )
#     sport_date = fields.Datetime("Sport_date_time")


# class SmartClass(models.Model):
#     _name = "smart_class"
#     _description = "smart_class"

#     smart_class_name = fields.Char(string="Smart class name")
#     lecturer_name =fields.Char(string="Lecturer Name")


# class CanteenMenu(models.Model):
#     _name = "canteen_menu"
#     _description = "canteen_menu"

#     item = fields.Char("Item name")
#     price = fields.Float("Price")
#     image = fields.Image("Photo")
