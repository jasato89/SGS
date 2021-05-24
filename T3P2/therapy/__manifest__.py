# -*- coding: utf-8 -*-
{
    'name': "Therapy Centers",

    'summary': """
        Information about therapy centers subsidized by the company""",

    'description': """
        This module allows to control which therapy centers we subsidize and how our employees use them
    """,

    'author': "Jaume Sánchez",
    'website': "http://github.com/jasato89/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
