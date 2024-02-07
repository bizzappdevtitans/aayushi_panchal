from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Admission(models.Model):
    _name = "admission.details"
    _description = "admission details"
    _rec_name = "full_name"

    enrollment_num = fields.Integer(string="Enrollment number", store=True)
    start_date = fields.Date(string="From Fillup Date", default=fields.Date.today())
    full_name = fields.Char(string="Full Name :")
    name = fields.Char(string="Name :", copy="False")
    lastname = fields.Char(string="Last Name")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")], string="Gender :"
    )
    contact_no = fields.Char(string="contact_no")
    date_of_birth = fields.Date("Date of Birth")
    course = fields.Char(string="Select Course:")
    pr_result = fields.Float(string="Previous Standard/Course Percentage%")
    course_name = fields.Selection(
        [
            ("mca", "MCA"),
            ("mscit", "MSCIT"),
            ("mba", "MBA"),
            ("llb", "LLB"),
        ],
        "Select course",
    )
    admisiion_no = fields.Char(
        string="Admisiion Reference",
        required=True,
        readonly=True,
        copy=False,
        index=True,
        default=lambda self: _("New"),
    )
    _sql_constraints = [
        (
            "contact_no_len",
            "check(Length(contact_no)=10)",
            "You can't enter less than 10 digits and more than 10 digits",
        ),
        (
            "unique_full_name_",
            "unique (full_name)",
            "Student name must be unique, this name is already exist.",
        ),
    ]

    @api.model
    def create(self, vals):
        if vals.get("admisiion_no", "New") == "New":
            vals["admisiion_no"] = (
                self.env["ir.sequence"].next_by_code("admission.details") or "New"
            )
        result = super(Admission, self).create(vals)
        start_date = vals.get("start_date")
        end_date = self.env["ir.config_parameter"].get_param(
            "college_application.admission_end_date"
        )
        if end_date < start_date:
            raise ValidationError(
                _("Sorry.....Admission is close,You can't get admission")
            )
        return result
