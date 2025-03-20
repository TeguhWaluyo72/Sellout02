# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Salesman(models.Model):
    _name = 'sellout.salesman'
    _description = 'Sellout Salesman'
    _rec_name = "nama_sls"

    kode_sls    = fields.Char(string="Kode Salesman")
    nama_sls    = fields.Char(string="Nama Salesman")
    company_id = fields.Many2one(
        comodel_name='res.company',
        index=True,
        default=lambda self: self.env.company)

class SelloutHNAPricelist(models.Model):
    _name = 'sellout.hnapricelist'
    _description = 'Sellout HNA Pricelist'

    barang_id = fields.Many2one(
        string="Barang",
        comodel_name='product.template')
    date_start  = fields.Date("Start")
    date_end    = fields.Date("End")
    price       = fields.Float("Price")

