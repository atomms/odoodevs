# -*- coding: utf-8 -*-
{
    'name': "lista_de_tareas",

    'summary': "Sencilla lista de tareas organizadas",

    'description': "Sencilla lista de tareas utilizadas para crear un nuevo módulo con un nuevo modelo de datos",

    'author': "atomms",
    'website': "https://github.com/atomms",
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
