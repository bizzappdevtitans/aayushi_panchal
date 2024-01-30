from datetime import date
from odoo import fields, models

class CanteenMenu(models.Model):
    _name = "canteen.details"
    _description = "canteen_menu"

    item = fields.Char("Item name")
    price = fields.Float("Price")
    quntity=fields.Integer("Quantity")
    image = fields.Image("Photo")
    table_no=fields.Integer("Table No")
