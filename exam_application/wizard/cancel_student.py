from odoo import models, fields, api


class CreateStudentwizard(models.Model):
    _name = "cancel.student.wizard"
    _description = "cancel student wizard"

    name = fields.Char(string="name")

    def action_cancel(self):
        print("cancel student.....!!!")

