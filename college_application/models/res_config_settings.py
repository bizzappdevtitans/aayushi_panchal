from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = ["res.config.settings"]

    admission_end_date = fields.Datetime(
        string="Admisiion End Date",
        config_parameter="college_application.admission_end_date",
    )
