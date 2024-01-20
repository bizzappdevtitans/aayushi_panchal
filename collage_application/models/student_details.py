from datetime import date
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StudentDetails(models.Model):
    _name = "student.details"
    _description = "student information"

    # Char fields
    full_name =fields.Char(string="Full Name")
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    color = fields.Char(string="Color")
    isbn = fields.Char("ISBN")
    mobile_no = fields.Char(string="Mobile no")
    email = fields.Char(string="Email id")
    linkdin_id = fields.Char(string="Linkdin Id")
    ref = fields.Char(string="Reference")

    exam_description = fields.Html(string="Exam Description", sanitize_attributes=False)
    address = fields.Text("Address")

    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")
    examtype = fields.Selection(
        [("externalexam", "External Exam"), ("internalexam", "Internal Exam"), ("remedialexam", "Remedial Exam"), ("hsc", "HSC")]
    )
    # compute age base on the date of birth
    marital = fields.Selection(
        [("single", "Single"), ("married", "Married"), ("divorced", "Divorced")],
        string="Marital status",
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
        string="Status",
        required=True,
        default="draft",
    )
    # priority widgets
    priority = fields.Selection(
        [("0", "Normal"), ("1", "Low"), ("2", "Hight"), ("3", "Very High")],
        string="priority",
    )

    # numerical fields :-

    result = fields.Integer("Result")
    color_2 = fields.Integer(string=" Fav Color picker")
    clg_fees = fields.Integer(string="Clg Fees")
    # age=fields.Integer(string="Age") normal filed
    age = fields.Integer(string="Age", compute="_compute_age")
    course_name = fields.Selection(
        [
            ("mca", "MCA"),
            ("mscit", "MSCIT"),
            ("mba", "MBA"),
            ("llb", "LLB"),
        ],
        "Select course",
    )
    course_count = fields.Integer(string="Course Count", compute="_compute_course")
    marks = fields.Float("Marks in pr")

    # Date time fields :-

    exam_date = fields.Datetime("Exam_date_time")
    date_of_birth = fields.Date("Date of Birth")

    # Other fields :-

    image = fields.Binary("Profile photo")
    document = fields.Binary("Upload your document")
    # archive the data field
    active = fields.Boolean(string="Active")

    faculty = fields.Many2one(comodel_name="faculty.details", string="Faculty Name")
    course= fields.Many2many("student.subject.details", string="course")
    # student_ids = fields.one2many(comodel_name="faculty.details", string="Faculty")
    name_ids = fields.Many2many(comodel_name="faculty.details", string="Faculty")

    # Compute filed :-

    # compute age from the date of birth
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

    def _compute_course(self):
        for rec in self:
            total_course = len(self.course)
            self.course_count = total_course

    # module constrains
    @api.constrains("full_name", "exam_description")
    def _check_name(self):
        for rec in self:
            if len(rec.full_name) < 3:
                raise ValidationError("Student name should be at least 3 charcters")

            if rec.full_name == rec.exam_description:
                raise ValidationError("Student name and Description shoud be different")

    @api.constrains("date_of_birth")
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth >= fields.Date.today():
                raise ValidationError("Enter a date of birth is not correct")

    # def action_open_course_details(self):
    #     return {
    #         "type": "ir.actions.act_window",
    #         "name": ("Course"),
    #         "res_model": "course.details",
    #         "view_mode": "tree,form",
    #         "domain": [("student_id", "=", self.id)],
    #         "target": "current",
    #     }

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
