from datetime import date

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class StudentDetails(models.Model):
    _name = "student.details"
    _description = "student information"
    _rec_name = "first_name"

    # Char fields
    full_name = fields.Char(string="Full Name :")
    first_name = fields.Char(string="First Name :")
    last_name = fields.Char(string="Last Name :")
    color = fields.Char(string="Color :")
    isbn = fields.Char("ISBN :")
    mobile_no = fields.Char(string="Mobile no :")
    email = fields.Char(string="Email id :")
    linkdin_id = fields.Char(string="Linkdin Id :")
    ref = fields.Char(string="Reference :")

    exam_description = fields.Html(
        string="Exam Description :", sanitize_attributes=False
    )
    address = fields.Text("Address :")

    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")], string="Gender :"
    )
    examtype = fields.Selection(
        [
            ("externalexam", "External Exam"),
            ("internalexam", "Internal Exam"),
            ("remedialexam", "Remedial Exam"),
        ]
    )

    marital = fields.Selection(
        [("single", "Single"), ("married", "Married"), ("divorced", "Divorced")],
        string="Marital status :",
    )
    # status bar in from view
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("in_progress", "In Progress"),
            ("complete", "Complete"),
            ("cancel", "Cancelled"),
            ("done", "Done"),
        ],
        string="Status ",
        required=True,
        default="draft",
    )
    # priority widgets
    priority = fields.Selection(
        [("0", "Normal"), ("1", "Low"), ("2", "Hight"), ("3", "Very High")],
        string="priority",
    )

    # numerical fields :-

    enrollment_number = fields.Integer(string="Enrollment Number :", store=True)
    result = fields.Integer(string="Result :")
    color_2 = fields.Integer(string=" Fav Color picker :")
    clg_fees = fields.Integer(string="Clg Fees :")
    age = fields.Integer(string="Age :", compute="_compute_age")
    course_count = fields.Integer(string="Course Count :", compute="_compute_course")
    marks = fields.Float("Marks in pr :")

    # Date time fields :-

    exam_date = fields.Datetime("Exam_date_time")
    date_of_birth = fields.Date("Date of Birth")

    # Other fields :-

    # image = fields.Binary("Profile photo",default='_get_default_image')
    image = fields.Binary("Profile photo")
    document = fields.Binary("Upload your document")

    # archive the data field
    active = fields.Boolean(string="Active :")

    student_class = fields.Many2one("class.details", string="Class name")
    student_course = fields.Many2one("course.details", string="Course name")

    student_no = fields.Char(
        string="Order Reference",
        required=True,
        readonly=True,
        copy=False,
        index=True,
        default=lambda self: _("New"),
    )

    # Compute filed :-

    # compute age from the date of birth
    @api.depends("date_of_birth")
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

    def _compute_course(self):
        total_course = len(self.student_course)
        self.course_count = total_course

    @api.model
    def create(self, vals):
        if vals.get("student_no", "New") == "New":
            vals["student_no"] = (
                self.env["ir.sequence"].next_by_code("student.details") or "New"
            )

        result = super(StudentDetails, self).create(vals)
        return result

    # module constrains

    @api.constrains("full_name", "exam_description")
    def _check_name(self):
        for rec in self:
            if len(rec.full_name) < 3:
                raise ValidationError(_("Student name should be at least 3 charcters"))

            if rec.full_name == rec.exam_description:
                raise ValidationError(
                    _("Student name and Description shoud be different")
                )

    @api.constrains("date_of_birth")
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth >= fields.Date.today():
                raise ValidationError(_("Enter a date of birth is not correct"))

    @api.onchange("enrollment_number")
    def onchange_student_full_name(self):
        if self.enrollment_number:
            full_name_id = self.env["admission.details"].search(
                [("enrollment_num", "=", self.enrollment_number)]
            )
            self.full_name = full_name_id.full_name
            self.first_name = full_name_id.name
            self.mobile_no = full_name_id.contact_no
            self.last_name = full_name_id.lastname
            self.gender = full_name_id.gender
            self.date_of_birth = full_name_id.date_of_birth

    def action_open_course_details(self):
        if self.course_count > 1:
            return {
                "type": "ir.actions.act_window",
                "name": ("students"),
                "res_model": "course.details",
                "view_mode": "tree,form",
                "domain": [("students", "=", self.id)],
                "target": "current",
            }
        else:
            return {
                "type": "ir.actions.act_window",
                "name": ("students"),
                "res_model": "course.details",
                "view_mode": "form",
                "domain": [("students", "=", self.id)],
                "target": "current",
            }

    def action_in_progress(self):
        for rec in self:
            rec.state = "in_progress"

    def action_in_complete(self):
        for rec in self:
            rec.state = "complete"

    def action_in_cancel(self):
        for rec in self:
            rec.state = "cancel"

    def action_in_done(self):
        for rec in self:
            rec.state = "done"

    def action_in_draft(self):
        for rec in self:
            rec.state = "draft"

    # @api.model
    # def write(self, vals, contect=None):
    #     if (self.image == False):
    #         get_imae = "/college_application/static/description/noimage.jpg"
    #         vals['image'] = get_image
    #     return super(StudentDetails, self).write(vals)

    # def _get_default_image(self):
    #     image_path = modules.get_module_resource('student.details',
    # '/college_application/static/description/noimage.jpg', 'noimage.jpg')
    #     return tools.image_resize_image_big(base64.b64encode(open('
    # /college_application/static/description/noimage.jpg', 'rb').read()))

    # def _set_image(self):
    #     for record in self:
    #         path = (
    #             record.get_image_path()
    #         )  #: image path in odoo folder structure, example: /odoo/images/<file>
    #         if not record.image:
    #             with open(
    #                 "/college_application/static/description/noimage.jpg", "rb"
    #             ) as img:
    #                 record.image = base64.b64encode(img.read())

    # @api.model
    # def search_read(
    #     self, model, fields=False, offset=0, limit=False, domain=None, order=None
    # ):
    #     domain = [
    #         "|",
    #         ("gender","ilike","male"),
    #         ("gender","ilike", "female"),
    #     ]
    #     res = super(StudentDetails, self).search_read(
    #         domain,fields,offset,limit,order
    #     )
    #     return res
