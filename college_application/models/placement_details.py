from odoo import models, fields, api, _


class PlacementDetails(models.Model):
    _name = "placement.details"
    _description = "placement information"
    _rec_name="student_name"

    student_name = fields.Char(string="Student name")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")
    mobile_no = fields.Char(string="Mobile No")
    email = fields.Char(string="Email id")
    image = fields.Binary(string="Profile photo")
    company_name = fields.Char(string="Company Name")
    select_by = fields.Selection(
        [("in collage", "In Collage"),
        ("outside collage", "Outsaid Collage"),]
    )
    training_period = fields.Char(string="Training period ")
    document = fields.Binary(string="Upload your document")
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("in_progress", "In Progress"),
            ("complete", "Complete"),
            ("cancel", "Cancelled"),
            ("done placement", "Done Placement"),
        ],
        string="Status",
        required=True,
        default="draft",
    )
    technology=fields.Char(string="Technology")
    placement_no = fields.Char(
        string="Course Reference",
        required=True,
        readonly=True,
        copy=False,
        index=True,
        default=lambda self: _("New"),
    )

    @api.model
    def create(self, vals):
        if vals.get("placement_no", "New") == "New":
            vals["placement_no"] = (
                self.env["ir.sequence"].next_by_code("placement.details") or "New"
            )

        result = super(PlacementDetails, self).create(vals)
        return result

    _sql_constraints = [
        (
            "unique_student_name_",
            "unique (student_name)",
            "student_name name must be unique, this name is already exist.",
        )
    ]
