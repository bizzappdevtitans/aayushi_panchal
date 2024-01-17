from odoo import models, fields, api


class TeacherDetails(models.Model):
    _name = "teacher.details"
    _description = "teacher information"

    # many2one filed
    # student_id = fields.Many2one(comodel_name="student.details", string="student")

    # defult value store in field
    exam_time = fields.Datetime(string="Exam time", defult=fields.Datetime.now)
    booking_date = fields.Date(
        string="Booking Exam Date", defult=fields.Date.context_today
    )
    # gender = fields.Selection([("male", "Male"), ("female", "Female")],readonly=False)
    ref = fields.Char(string="Reference")

    # @api.onchange("student_id")  # add decorater
    # def onchange_teacher_id(
    #     self,
    # ):  # on change function when id selected automaticly ref change
    #     self.ref = self.student_id
