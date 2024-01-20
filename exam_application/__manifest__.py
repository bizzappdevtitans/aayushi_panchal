{
    "name": "exam application",
    "sequence": 0,
    "summary": "This is for examination application",
    "author": "bizzappdev",
    "website": "https://bizzappdev.com",
    "category": "uncategorized",
    "version": "15.0.1.0.0",
    "description": """
This module contains all the common features of exam Management and all.""",
    "depends": ["base","mail"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/cancel_student_views.xml",
        "view/student_details_views.xml",
        "view/teacher_details_views.xml",
        "view/subject_details_views.xml",
        "view/exam_menu.xml",

    ],
    "demo": [],
    "installable": True,
    "license": "LGPL-3",
}
