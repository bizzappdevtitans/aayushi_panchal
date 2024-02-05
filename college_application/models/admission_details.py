from odoo import fields, api, models, _
from odoo.exceptions import ValidationError


class Admission(models.Model):
    _name = "admission.details"
    _description = "admission details"
    _rec_name = "full_name"

    enrollment_num = fields.Integer(string="Enrollment number", store=True)
    start_date = fields.Date(
        size=15, string="From Fillup Date", required=True, default=fields.Date.today()
    )
    end_date = fields.Date(
        size=15, string="Admission End Date", required=True, onchange="date_constrains"
    )
    full_name = fields.Char(string="Full Name")
    name = fields.Char(string="Name", copy="False")
    lastname = fields.Char(string="Last Name")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")
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

    def date_constrains(self):
        for rec in self:
            if rec.end_date < rec.start_date:
                raise ValidationError(
                    _("Sorry, End Date Must be greater Than Start Date...")
                )

    # perform object button
    def action_test(self):
        print("hello student, welcome to collage campus!!!!")

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
        return result
