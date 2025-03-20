# -*- coding: utf-8 -*-
# from odoo import http


# class SelloutUpload(http.Controller):
#     @http.route('/sellout_upload/sellout_upload', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sellout_upload/sellout_upload/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sellout_upload.listing', {
#             'root': '/sellout_upload/sellout_upload',
#             'objects': http.request.env['sellout_upload.sellout_upload'].search([]),
#         })

#     @http.route('/sellout_upload/sellout_upload/objects/<model("sellout_upload.sellout_upload"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sellout_upload.object', {
#             'object': obj
#         })

