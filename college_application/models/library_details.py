from odoo import api, fields, models


class LibraryDetails(models.Model):
    _name = "library.details"
    _description = "library"

    library_name = fields.Char(string="library name :")
    student_name = fields.Char(string="Student Name :")
    library_date = fields.Datetime("Date time :")
    library_image = fields.Binary("Library Image :")

    @api.model
    def create(self, vals):
        vals = {"library_name": "gls collage library"}
        result = super(LibraryDetails, self).create(vals)
        return result
