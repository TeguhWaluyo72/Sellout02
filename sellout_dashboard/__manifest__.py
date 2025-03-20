# -*- coding: utf-8 -*-
{
    'name': "sellout_dashboard",

    'summary': "Sellingout Project - Dashboard",

    'description': """ 
        Replicate modul Sales : 
        Modifikasi : 
           - Customer Industry -> Kategory pelanggan 3 
           - Kategory Pelanggan 1,2 sebagai parent dari Customer Industry 
           - Wilayah Per propinsi , kota/kabupaten 
                
    """,

    'author': "DragoPF",
    'website': "https://sellingout.dragonpferp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '2.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base','contacts' , 'sale' , 'sellout_base' ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'report/sale_report_views.xml',
        'report/outlet_report_views.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

