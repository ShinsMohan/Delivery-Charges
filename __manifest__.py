{
    "name": "Delivery Charges",
    "author": "Shins",
    'license': 'LGPL-3',
    'depends': ['sale','account'],
    'data': [
        'security/ir.model.access.csv',
        'views/charges.xml',
        'views/invoice.xml',
        'views/delivery.xml',
        'report/boolean_view.xml',
        'wizard/import_wizard.xml',
        'views/sales_order_view.xml',
        'views/boolean.xml',
    ]
}