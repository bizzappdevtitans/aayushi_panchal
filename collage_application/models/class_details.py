from odoo import models, fields


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
    faculty_count=fields.Integer(
        string="total faculty of class", compute="_compute_faculty"
    )

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

    def _compute_faculty(self):
        for rec in self:
            rec.faculty_count = self.env['faculty.details'].search_count(
                [('faculty_class', '=', self.id)])

    def action_count_faculty_of_class(self):
        if self.faculty_count > 1:
            return{
                "type": "ir.actions.act_window",
                "name": ("faculty_class"),
                "res_model": "faculty.details",
                "view_mode": "tree,form",
                "domain": [("faculty_class", "=", self.id)],
                "target": "current",
            }
        else:
            return{
                "type": "ir.actions.act_window",
                "name": ("faculty_class"),
                "res_model": "faculty.details",
                "view_mode": "form",
                "domain": [("faculty_class", "=", self.id)],
                "target": "current",
            }


