from odoo import models, fields, _,api
from odoo.exceptions import UserError

class ClassDetails(models.Model):
    _name = "class.details"
    _description = "Class Information"
    _rec_name = "room_number"

    class_name = fields.Char(string="Class name")
    class_faculty = fields.Many2one("faculty.details", string="Class facility")
    room_number = fields.Integer("Room number")
    students = fields.One2many("student.details", "student_class", "Students")
    course = fields.One2many("course.details", "course_class", "Course")
    strenth_of_class = fields.Integer(string="strenth of a class")
    student_count = fields.Integer(
        string="total student of class", compute="_compute_student"
    )
    course_count=fields.Integer(
        string="total course of class", compute="_compute_course"
    )
    class_no = fields.Char(
        string="Class Reference",
        required=True,
        readonly=True,
        copy=False,
        index=True,
        default=lambda self: _("New"),
    )

    @api.model
    def create(self, vals):
        if vals.get("class_no", "New") == "New":
            vals["class_no"] = (
                self.env["ir.sequence"].next_by_code("class.details") or "New"
            )

        result = super(ClassDetails, self).create(vals)
        return result

    def _compute_student(self):
        for rec in self:
            total_student = len(self.students)
            self.student_count = total_student

    def action_count_student_of_class(self):
        return{
            "type": "ir.actions.act_window",
            "name": ("students_class"),
            "res_model": "student.details",
            "view_mode": "tree,form",
            "domain": [("student_class", "=", self.id)],
            "target": "current",
        }

    def unlink(self):
        if (self.class_faculty or self.course):
            raise UserError("You cannot Delete this class")
        return super(ClassDetails, self).unlink()

    def _compute_course(self):
        for rec in self:
            rec.course_count = self.env['course.details'].search_count(
                [('course_class', '=', self.id)])

    def action_count_faculty_of_class(self):
        if self.course_count > 1:
            return{
                "type": "ir.actions.act_window",
                "name": ("course_class"),
                "res_model": "course.details",
                "view_mode": "tree,form",
                "domain": [("course_class", "=", self.id)],
                "target": "current",
            }
        else:
            return{
                "type": "ir.actions.act_window",
                "name": ("course_class"),
                "res_model": "course.details",
                "view_mode": "form",
                "domain": [("course_class", "=", self.id)],
                "target": "current",
            }

    def name_get(self):
        result = []
        for rec in self:
            result.append(
                (rec.id, "%s - %s" % (rec.room_number, rec.class_name))
            )
        return result

