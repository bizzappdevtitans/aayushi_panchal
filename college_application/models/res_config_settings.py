from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = ["res.config.settings"]

    cancel_admission = fields.Integer(
        string="Show Cancel Admission",
        config_parameter="college_application.cancel_admission",
    )

    # @api.model
    # def get_values(self):
    #     res = super(ResConfigSettings, self).get_values()

    #     res["cancel_admission"] = int(
    #         self.env["ir.config_parameter"]
    #         .sudo()
    #         .get_param("college_application.cancel_admission", default=0)
    #     )

    #     return res

    # @api.model
    # def set_values(self):
    #     self.env["ir.config_parameter"].sudo().set_param(
    #         "college_application.cancel_admission", self.cancel_admission
    #     )

    #     super(ResConfigSettings, self).set_values()
