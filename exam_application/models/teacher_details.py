from odoo import models, fields, api


class TeacherDetails(models.Model):
    _name = "teacher.details"
    _description = "teacher information"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    # many2one filed
    teacher_id = fields.Many2one(comodel_name="student.details", string="Student name")
    student_id = fields.One2many("student.details", "teacher", "StudentName")
    teacher_name = fields.Char(string="Teacher name")
    # defult value store in field
    exam_time = fields.Datetime(string="Exam time", defult=fields.Datetime.now)
    booking_date = fields.Date(
        string="Booking Exam Date", defult=fields.Date.context_today
    )
    mobile_no = fields.Char(string="Mobile No")
    gender = fields.Selection(related="teacher_id.gender", readonly=False)
    ref = fields.Char(string="Reference")
    student_count= fields.Integer(string="student Count",compute="_compute_student_count")

    _sql_constraints = [
        (
            "unique_teacher_name_",
            "unique (teacher_name)",
            "Teacher name must be unique, this name is already exist."
        )
    ]

    @api.onchange("teacher_id")  # add decorater
    def onchange_teacher_id(
        self,
    ):  # on change function when id selected automaticly ref change
        self.ref = self.teacher_id

    def action_share_whatsapp(self):
        if not self.teacher_id.mobile_no:
            raise ValidationError(("missing mobile num in Teacher record"))
        msg = "Hello %s" % self.teacher_id.mobile_no
        whatsapp_api_url = "https://api.whatsapp.com/send?phone=%s&text=%s" % (
            self.teacher_id.mobile_no,
            msg,
        )
        return {
            "type": "ir.actions.act_window",
            "url": "whatsapp_api_url",
            "target": "new",
        }

    def _compute_student_count(self):
        for rec in self:
            student_count = self.env["student.details"].search_count(
                [("teacher", "=", rec.id)]
            )
            rec.student_count = student_count

    def action_open_student_details(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Students",
            "res_model": "student.details",
            "domain": [("teacher", "=", self.id)],
            "view_mode": "tree,form",
            "target": "current",
            }
