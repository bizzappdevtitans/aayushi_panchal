from odoo import models, fields, _,api


class FacultyDetails(models.Model):
    _name = "faculty.details"
    _description = "faculty information"
    _rec_name = "faculty_name"

    faculty_name = fields.Char(string="Faculty name")
    faculty_short_name = fields.Char(string="Faculty ShortName")
    mobile_no = fields.Char(string="Mobile No")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")
    email = fields.Char(string="Email id")
    image = fields.Binary("Profile photo")
    experience = fields.Char("experience")
    document = fields.Binary("Upload your document")

    sequence = fields.Integer(string = "Sequence")
    course_count = fields.Integer(string="Course Count", compute="_compute_course")
    faculty_class = fields.Many2one("class.details", string="Class facility")
    course = fields.One2many("course.details", "faculty_course", "Course given")
    faculty_no = fields.Char(
        string="Order Reference",
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _("New"),
    )

    """Returns the unique sequence number whenever new form is created"""
    @api.model
    def create(self, vals):
        if vals.get("faculty_no", "New") == "New":
            vals["faculty_no"] = (
                self.env["ir.sequence"].next_by_code("faculty.details")
            )
            vals["email"] = "faculty.123@email.com"
            vals["mobile_no"] = 1234567890
        result = super(FacultyDetails, self).create(vals)
        return result

    # def unlink(self,vals):
    #     for rec in self:
    #         vals = course
    #         if rec.course in vals:
    #             raise UserError('You cannot Delete this record')
    #     return super(FacultyDetails, self).unlink(vals)

    # def unlink(self):
    #     return super(FacultyDetails, self).unlink()

    def write(self, vals):
        if 'faculty_name' in vals and vals['faculty_name']:
            vals['faculty_name'] = vals['faculty_name'].capitalize()
        return super(FacultyDetails, self).write(vals)

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s - %s' % (rec.faculty_short_name,rec.faculty_name)))
        return result


    _sql_constraints = [
        (
            "unique_faculty_name_",
            "unique (faculty_name)",
            "Faculty name must be unique, this name is already exist.",
        )
    ]

    @api.constrains("mobile_no")
    def _validate_mobile_no(self):
        for record in self:
            if len(record.mobile_no) != 10:
                raise ValidationError("Please add 10 digit phone number")


    def _compute_course(self):
        for rec in self:
            total_course = len(self.course)
            self.course_count = total_course

    def action_open_course_details(self):
        if self.course_count > 1:
            return {
                "type": "ir.actions.act_window",
                "name": ("faculty_course"),
                "res_model": "course.details",
                "view_mode": "tree,form",
                "domain": [("faculty_course", "=", self.id)],
                "target": "current",
            }
        else:
            return {
                "type": "ir.actions.act_window",
                "name": ("faculty_course"),
                "res_model": "course.details",
                "view_mode": "form",
                "domain": [("faculty_course", "=", self.id)],
                "target": "current",
            }

