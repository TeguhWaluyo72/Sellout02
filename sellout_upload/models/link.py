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
    village_id = fields.Many2one('res.district.village', string="Kelurahan/Desa" )
    sub_district_id = fields.Many2one('res.district.sub', string='Kecamatan' )
    district_id = fields.Many2one('res.district', string='Kabupaten/Kota')
    state_id = fields.Many2one('res.country.state', string='Provinsi' ) 

    @api.model
    def write(self, values):
        super(LinkWilayah, self).write(values)

        if 'wilayah_id' in values and values.get('wilayah_id'):
            wilayah_id = values.get('wilayah_id')
            linkcusts = self.env["sellout.link.customer"].search([
                ('company_id','=',self.company_id.id),
                ('code' , '=', self.code )
            ])
            linkcusts.write({
                'wilayah_id' :  wilayah_id
            })
            for linkcust in linkcusts:
                cust = self.env["res.partner"].search([('id','=', linkcust.customer_id.id )])
                cust.write({
                    'district_id' : wilayah_id
                })


class LinkBarang(models.Model):
    _name   = 'sellout.link.barang'
    _description = 'Link Barang'
    code = fields.Char(string="Kode Barang" , index = True )
    name = fields.Char(string="Nama Barang" )
    company_id = fields.Many2one(
        comodel_name='res.company',
        index=True,
        default=lambda self: self.env.company)
    barang_id = fields.Many2one(
        string="Barang",
        comodel_name='product.template')
    
    @api.model
    def write(self, values):
        super(LinkBarang, self).write(values)
        if 'barang_id' in values and values.get('barang_id'):
            barang_id   = values.get('barang_id')
            linkdetails = self.env["sellout.upload.detail"].search([
                ('company_id','=',self.company_id.id),
                ('kode_brg' , '=', self.code )
            ])
            linkdetails.write({
                'barang_id' : barang_id
            })
            for linkdetail in linkdetails:
                ada  = self.env["sale.order.line"].search_count([('upload_detail_id','=', linkdetail.id )])
                if ada>0:
                    detail = self.env["sale.order.line"].search([('upload_detail_id','=', linkdetail.id )])
                    detail.write({
                        'barang_id' : barang_id
                    })    


class LinkSalesman(models.Model):
    _name   = 'sellout.link.salesman'
    _description = 'Link Salesman'    
    code = fields.Char(string="Kode Salesman" , index = True )
    name = fields.Char(string="Nama Salesman" )
    company_id = fields.Many2one(
        comodel_name='res.company',
        index=True,
        default=lambda self: self.env.company)
    salesman_id = fields.Many2one(
        comodel_name='sellout.salesman',
        string = 'Salesman'
    )

    @api.model
    def write(self, values):
        super(LinkSalesman, self).write(values)
        if 'salesman_id' in values and values.get('salesman_id'):
            salesman_id = values.get('salesman_id')
            linkcusts = self.env["sellout.link.salesman"].search([
                ('company_id','=',self.company_id.id),
                ('kode_sls' , '=', self.code )
            ])
            linkcusts.write({
                'salesman_id' : salesman_id
            })
            for linkcust in linkcusts:
                count = self.env["sale.order"].search_count([('upload_id','=',linkcust.upload_id)]) 
                if count>0:
                    cust = self.env["sale.order"].search([('upload_id','=',linkcust.upload_id)])
                    cust.write({
                        'salesman_id' : values('salesman_id')                    
                    })

        
    
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

    @api.model
    def write(self, values):
        super(LinkKlpcustomer, self).write(values)
        if 'klp_cust_id' in values and values.get('klp_cust_id'):
            klp_cust_id = values.get('klp_cust_id')
            linkcusts = self.env["sellout.link.customer"].search([
                ('company_id','=',self.company_id.id),
                ('kelompok' , '=', self.code )
            ])
            linkcusts.write({
                'klp_cust_id' : klp_cust_id
            })
            for linkcust in linkcusts:
                count = self.env["res.partner"].search_count([('id','=', linkcust.customer_id.id )])
                if count>0:
                    cust = self.env["res.partner"].search([('id','=', linkcust.customer_id.id )])
                    cust.write({
                        'industry_id' : klp_cust_id
                    })

    
    
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
    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer')

    @api.model
    def write(self, values):
        super(LinkCustomer, self).write(values)
        if 'customer_id' in values and values.get('customer_id'):
            customer_id = values.get('customer_id')
            linkcusts = self.env["sellout.link.customer"].search([
                ('company_id','=',self.company_id.id),
                ('kode_ctm' , '=', self.code )
            ])
            linkcusts.write({
                'customer_id' : customer_id
            })
            for linkcust in linkcusts:
                count =  self.env["sale.order"].search_count([('upload_id','=',linkcust.upload_id)])
                if count>0:
                    cust = self.env["sale.order"].search([('upload_id','=',linkcust.upload_id)])
                    cust.write({
                        'customer_id' : customer_id                    
                    })

