# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartners(models.Model):
    _inherit = ['res.partner']

    
    dgExType    = fields.Char(string="Dist. Type Pelanggan ")
    dgExNama    = fields.Char(string="Dist. Nama Pelanggan ")
    dgExAlamat  = fields.Char(string="Dist. Alamat Pelanggan")
    dgExWilayah = fields.Char(string="Dist. Kode Wilayah")

    dgCompanyId = fields.Integer(string="Company DG Id")
    dgExreff    = fields.Char(string="Dist. Kode Pelanggan ")
    district_id = fields.Many2one('res.district', string="Kota/Kabupaten")
    subdistrict_id = fields.Many2one('res.district.sub', string="Kecamatan")
    village_id  = fields.Many2one('res.district.village', string="Kelurahan")
