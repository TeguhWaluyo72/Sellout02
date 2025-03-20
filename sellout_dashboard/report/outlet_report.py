# -*- coding: utf-8 -*-

from odoo import models, fields, api




class OutletReport(models.Model):
    _name = 'outlet.report'
    _description = ' Outlet Report'
    _auto = False
    _rec_name = 'date'
    _order = 'date desc'


    count_partner   = fields.Float(string="Count Customer", readonly=True)
    company_id      = fields.Many2one(comodel_name='res.company', readonly=True)
    date            = fields.Datetime(string="Order Date", readonly=True)
    partner_id = fields.Many2one(comodel_name='res.partner', string="Customer", readonly=True)
    product_id      = fields.Many2one(
        comodel_name='product.product', string="Product Variant", readonly=True , domain="[('categ_id','=',categ_id)]" )
    product_tmpl_id = fields.Many2one(
        comodel_name='product.template', string="Product", readonly=True, domain="[('product_id','=',product_id))]" )
    categ_id        = fields.Many2one(
        comodel_name='product.category', string="Product Category", readonly=True, domain="[('categ_id','=',categ_id)]")    

    def _select_sale(self):
        return """
            MIN(l.id) AS id,
            s.date_order as date,
            s.company_id as company_id,
            COUNT( DISTINCT s.partner_id ) as count_partner 

            """


    def _with_sale(self):
        return ""


    def _from_sale(self):
        return """
            sale_order_line l
            LEFT OUTER JOIN sale_order s ON s.id=l.order_id 
            """
            
    def _where_sale(self):
        return """
            l.display_type IS NULL"""

    def _group_by_sale(self):
        return """
            s.date_order,
            s.company_id

            """

    def _query(self):
        with_ = self._with_sale()
        return f"""
            SELECT {self._select_sale()}
            FROM {self._from_sale()}
            WHERE {self._where_sale()}
            GROUP BY {self._group_by_sale()}
        """

    @property
    def _table_query(self):
        return self._query()




