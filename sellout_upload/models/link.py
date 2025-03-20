# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LinkWilayah(models.Model):
    _name = 'sellout.link.wilayah'
    _description = 'Link Wilayah'
    code = fields.Char(string="Kode Wilayah" , index = True)
    name = fields.Char(string="Nama Wilayah")
    company_id = fields.Many2one(
        comodel_name='res.company',
        index=True,
        default=lambda self: self.env.company)
#    template_id = fields.Many2one('link.template','Template' , index = True)
    village_id = fields.Many2one('res.district.village', string="Kelurahan/Desa" )
    sub_district_id = fields.Many2one('res.district.sub', string='Kecamatan' )
    district_id = fields.Many2one('res.district', string='Kabupaten/Kota')
    state_id = fields.Many2one('res.country.state', string='Provinsi' )    

class LinkBarang(models.Model):
    _name   = 'sellout.link.barang'
    _description = 'Link Barang'
    code = fields.Char(string="Kode Barang" , index = True )
    name = fields.Char(string="Nama Barang" )
    company_id = fields.Many2one(
        comodel_name='res.company',
        index=True,
        default=lambda self: self.env.company)
#    template_id = fields.Many2one('link.template','Template' , index = True)
    barang_id = fields.Many2one(
        string="Barang",
        comodel_name='product.template')

class LinkSalesman(models.Model):
    _name   = 'sellout.link.salesman'
    _description = 'Link Salesman'    
    code = fields.Char(string="Kode Salesman" , index = True )
    name = fields.Char(string="Nama Salesman" )
    company_id = fields.Many2one(
        comodel_name='res.company',
        index=True,
        default=lambda self: self.env.company)
    user_id = fields.Many2one(
        comodel_name='res.users',
        string="Salesperson",
        )    
    salesman_id = fields.Many2one(
        comodel_name='sellout.salesman',
        string = 'Salesman'
    )
        
    
class LinkKlpcustomer(models.Model):
    _name   = 'sellout.link.customer.kelompok'
    _description = 'Link Kelompok Pelanggan'    
    code    = fields.Char(string="Kode " , index = True )
    name    = fields.Char(string="Nama " )
    company_id = fields.Many2one(
        comodel_name='res.company',
        index=True,
        default=lambda self: self.env.company)
    klp_cust_id  = fields.Many2one('res.partner.industry','Kelompok ')
#    template_id = fields.Many2one('link.template','Template' , index = True)
    
    
class LinkCustomer(models.Model):
    _name   = 'sellout.link.customer'
    _description = 'Link Pelanggan'    
    code = fields.Char(string="Kode " , index = True )
    name = fields.Char(string="Nama " )
    company_id = fields.Many2one(
        comodel_name='res.company',
        index=True,
        default=lambda self: self.env.company)
    alamat     = fields.Char(string="Alamat")
    kelom_cust = fields.Char(string="Kelompok")
    kode_wilay = fields.Char(string="Kode Wilayah")
    nama_wilay = fields.Char(string="Nama Wilayah")
#   template_id = fields.Many2one('link.template','Template' , index = True)

    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer')
