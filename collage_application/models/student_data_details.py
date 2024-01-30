from datetime import date
from odoo import models, fields, api
from odoo.exceptions import ValidationError



class StudentDataDetails(models.Model):
    _name = "student.data.details"
    _description = "student information"
    _rec_name="first_name"

    # Char fields
    full_name = fields.Char(string="Full Name")
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
        [
            ("externalexam", "External Exam"),
            ("internalexam", "Internal Exam"),
            ("remedialexam", "Remedial Exam"),
        ]
    )

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

    enrollment_number = fields.Integer(string="Enrollment Number", store=True)
    result = fields.Integer(string="Result")
    color_2 = fields.Integer(string=" Fav Color picker")
    clg_fees = fields.Integer(string="Clg Fees")
    age = fields.Integer(string="Age")
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

    # student_class = fields.Many2one("class.details", string="Class name")
    # student_course = fields.Many2one("course.details", string="Course name")
    # faculty = fields.Many2one(comodel_name="faculty.details", string="Faculty Name")
    # student_ids = fields.one2many(comodel_name="faculty.details", string="Faculty")
    # name_ids = fields.Many2many(comodel_name="faculty.details", string="Faculty")

    # Compute filed :-


    # _sql_constraints = [
    #     (
    #         "unique_full_name_",
    #         "unique (full_name)",
    #         "Student name must be unique, this name is already exist.",
    #     )
    #     (
    #         "contact_no_len",
    #         "check(Length(contact_no)=10)",
    #         "You can't enter less than 10 digits and more than 10 digits",
    #     )
    # ]
    # compute age from the date of birth
    # def _compute_age(self):
    #     for rec in self:
    #         today = date.today()
    #         if rec.date_of_birth:
    #             rec.age = today.year - rec.date_of_birth.year
    #         else:
    #             rec.age = 0

    # def _compute_course(self):
    #     for rec in self:
    #         total_course = len(self.course)
    #         self.course_count = total_course

    # module constrains
    # @api.constrains("full_name", "exam_description")
    # def _check_name(self):
    #     for rec in self:
    #         if len(rec.full_name) < 3:
    #             raise ValidationError("Student name should be at least 3 charcters")

    #         if rec.full_name == rec.exam_description:
    #             raise ValidationError("Student name and Description shoud be different")

    # @api.constrains("date_of_birth")
    # def _check_date_of_birth(self):
    #     for rec in self:
    #         if rec.date_of_birth > fields.Date.today():
    #             raise ValidationError("Enter a date of birth is not correct")

    # @api.depends("result")
    # def _compute_pass(self):
    #     for rec in self:
    #         if rec.result > 45:
    #             rec.update({"state": "pass"})
    #         else:
    #             rec.update({"state": "fail"})

    # @api.onchange("enrollment_number")
    # def onchange_student_full_name(self):
    #     if self.enrollment_number:
    #         full_name_id = self.env["admission.details"].search(
    #             [("enrollment_num", "=", self.enrollment_number)]
    #         )
    #         self.full_name=full_name_id.full_name
    #         self.first_name=full_name_id.name
    #         self.mobile_no=full_name_id.contact_no
    #         self.last_name=full_name_id.lastname
    #         self.gender=full_name_id.gender
    #         self.date_of_birth=full_name_id.date_of_birth


    # def action_open_course_details(self):
    #     return {
    #         "type": "ir.actions.act_window",
    #         "name": ("Course"),
    #         "res_model": "course.details",
    #         "view_mode": "tree,form",
    #         "domain": [("student_id", "=", self.id)],
    #         "target": "current",
    #     }

    # def action_in_progress(self):
    #     for rec in self:
    #         rec.state = "in_progress"

    # def action_in_complete(self):
    #     for rec in self:
    #         rec.state = "complete"

    # def action_in_cancel(self):
    #     for rec in self:
    #         rec.state = "cancel"

    # def action_in_done(self):
    #     for rec in self:
    #         rec.state = "done"

    # def action_in_draft(self):
    #     for rec in self:
    #         rec.state = "draft"
