{
    'name': "Smarten Project",
    'version': "18.0.1.0.0",
    'category': 'project',

    'author': 'Devendra Stha',
    'summary': 'Support',
    'description': """
        This module provides support for clients to solve their problems.
    """,
    'depends': ['base', 'project', 'planning', 'crm', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'demo/demo.xml',
        'demo/manufacture.xml',
        'views/templates.xml',
		'demo/accounting.xml',
		'demo/crm.xml',
],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
