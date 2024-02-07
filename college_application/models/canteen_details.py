from odoo import fields, models


class CanteenMenu(models.Model):
    _name = "canteen.details"
    _description = "canteen_menu"
    _rec_name = "item"

    item = fields.Char("Item name :")
    price = fields.Float("Price :")
    quntity = fields.Integer("Quantity :")
    image = fields.Image("Photo :")
    table_no = fields.Integer("Table No :")
    note = fields.Text("Notes :")
    category = fields.Selection(
        [("veg", "Veg"), ("non-veg", "Non-veg")], "Select item category"
    )

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, "%s - %s" % (rec.item, rec.price)))
        return result
