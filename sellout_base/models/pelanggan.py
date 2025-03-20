# -*- coding: utf-8 -*-

from odoo import models, fields, api



class ResCompany(models.Model):
    _inherit = ['res.company']

    dgExCompId  = fields.Integer(string="External")    

class ResSalesman(models.Model):
    _name   = 'res.partner.salesman'

    code = fields.Char(string="Kode Salesman")
    name = fields.Char(string="Nama Salesman", index=True)
    team_id  = fields.Many2one('res.partner.salesteam', string="Sales Team")

class ResSalesTeam(models.Model):
    _name   = 'res.partner.salesteam'

    code = fields.Char(string="Code Team Salesman")
    name = fields.Char(string="Nama Team Salesman", index=True)

class CustomerCategoryLevel1(models.Model):
    _name = 'res.partner.categorylevel1'
    _description = 'Category Pelanggan Level1'
    name = fields.Char(string="Name")
    
class CustomerCategoryLevel2(models.Model):
    _name = 'res.partner.categorylevel2'
    _description = 'Category Pelanggan Level2'
    code = fields.Char(string="Code")
    name = fields.Char(string="Name", index=True)
    parent_id = fields.Many2one('res.partner.categorylevel1','Parent Category', index=True, ondelete='cascade')
   

class CustomerCategory(models.Model):
    _inherit = ['res.partner.industry']
    parent_id = fields.Many2one('res.partner.categorylevel2','Parent Category', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)


