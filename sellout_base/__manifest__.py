# -*- coding: utf-8 -*-
{
    'name': "sellout_base",

    'summary': "Sellingout Project - Base versi 2.0 ",

    'description': """ 
        Base Project - 
           - Models 
                - Wilayah     ( Propinsi , Kabupaten , Kecamatan , Desa )
                - Pelanggan   ( Kategory Pelanggan 1,2,3)
        Update from version 1
        create default value 
                - INCOMPLETE 
                  di WILAYAH , TIPE PELANGGAN 
                
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
    'depends': ['base','contacts'],

    # always loaded
    'data': [
       'security/security.xml',
       'security/ir.model.access.csv',
       'data/res.district.csv',
       'data/res.partner.categorylevel1.csv',
       'data/res.partner.categorylevel2.csv',
       'data/res.partner.industry.csv',
       'views/views.xml',
       'views/wilayah_views.xml',
       'views/partner_views.xml',
       'views/menu.xml',
    ],
}

