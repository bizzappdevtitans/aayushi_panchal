from odoo import models, fields


class EventDetails(models.Model):
    _name = "event.details"
    _description = "event Information"
    _rec_name = "event_name"

    event_name = fields.Char(string="event name")
    event_faculty = fields.Many2many("faculty.details", string="event facility")
    event_time = fields.Selection(
        [
            ("morning", "Morning"),
            ("afternoon", "Afternoon"),
            ("evening", "Evening"),
        ],
        "Select event time",
    )
    event_type = fields.Selection(
        [
            ("education", "Education"),
            ("entertainment", "Entertainment"),
            ("seminar", "Seminar"),
        ],
        "Select event type",
    )
    event_date = fields.Datetime(string="Event Date")
