# -*- coding: utf-8 -*-
{
    'name': "sellout_upload",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
          Update from version 1.0
           - excel yang di upload ke sale.order kecuali field2 mandari masih kosong / tidak lengkap 
           - field2 yang non mandatory diberi tagar INCOMPLETE 
           - field2 mandatory : 
             - Kode Pelanggan 
             - Tanggal 
             - Kode Barang 
             - Qty 
             - Harga 

    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': [ 'base', 'sale' , 'sellout_base' ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/link_barang_views.xml',
        'views/link_wilayah_views.xml',
        'views/link_salesman_views.xml',
        'views/link_kelompok_customer_views.xml',
        'views/link_customer_views.xml',   
        'views/view_partner_form.xml',     
        'views/views.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

