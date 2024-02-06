from datetime import date
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StudentDetails(models.Model):
    _name = "student.details"
    _description = "student information"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    # Char fields

    name = fields.Char(string="Student Name")
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
        [("ielts", "IELTS"), ("upsc", "UPSC"), ("ssc", "SSC"), ("hsc", "HSC")]
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
    subject_count = fields.Integer(string="Subject Count", compute="_compute_subject")
    marks = fields.Float("Marks in pr")

    # Date time fields :-

    exam_date = fields.Datetime("Exam_date_time")
    date_of_birth = fields.Date("Date of Birth")

    # Other fields :-

    image = fields.Binary("Profile photo")
    document = fields.Binary("Upload your document")
    # archive the data field
    active = fields.Boolean(string="Active", defult=True)

    teacher = fields.Many2one(comodel_name="teacher.details", string="Teacher Name")
    subjects = fields.Many2many("student.subject.details", string="Subject")

    _sql_constraints = [
        (
            "unique_student_name_",
            "UNIQUE(name)",
            "Student name must be unique, this name is already exist.",
        ),
        (
            "result_uniq",
            "CHECK (result > 0)",
            "marks and result must be in postive number.",
        ),
    ]

    # Compute filed :-

    # compute age from the date of birth
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

    def _compute_subject(self):
        for rec in self:
            total_student = len(self.subjects)
            self.subject_count = total_student

    # module constrains
    @api.constrains("name", "exam_description")
    def _check_name(self):
        for rec in self:
            if len(rec.name) < 3:
                raise ValidationError("Student name should be at least 3 charcters")

            if rec.name == rec.exam_description:
                raise ValidationError("Student name and Description shoud be different")

    @api.constrains("date_of_birth")
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth >= fields.Date.today():
                raise ValidationError("Enter a date of birth is not correct")

    # perform object button
    def action_test(self):
        print("button clicked!!!!")

    def action_open_subject_details(self):
        return {
            "type": "ir.actions.act_window",
            "name": ("subjects"),
            "res_model": "student.subject.details",
            "view_mode": "tree,form",
            "domain": [("students", "=", self.name)],
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


class StudentSubjectDetails(models.Model):
    _name = "student.subject.details"
    _description = "Information about subject which student give exam"
    _rec_name = "subject_name"

    students = fields.Many2many("student.details", string="Student")
    subject_name = fields.Selection(
        [
            ("maths", "Maths"),
            ("english", "English"),
            ("science", "Science"),
            ("gujrati", "Gujrati"),
        ],
        "Select Subject",
    )
