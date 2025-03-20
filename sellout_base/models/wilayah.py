# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CountryState(models.Model):
    _inherit = 'res.country.state'
    district_ids = fields.One2many('res.district','state_id',string="Provinsi")

class District(models.Model):
    _name = 'res.district'
    _description = 'Kota/Kabupaten'
    state_id = fields.Many2one('res.country.state', string='Provinsi', required=True)
    code = fields.Char(string="Kode Kota/Kabupaten")
    name = fields.Char(string="Nama Kota/Kabupaten", index=True)
    typ = fields.Selection([
        ('kab','Kabupaten'),
        ('kabtif','Kabupaten Administratof'),
        ('kota','Kota'),
        ('kotif','Kota Administratif')      
    ],string="jenis" , required=True)
    display_code = fields.Char(index=True)
    area = fields.Char(string="area")
    # display_code = fields.Char(compute='_compute_display_code', store=True, index=True)
    # sub_district_ids = fields.One2many('res.district.sub', 'district_id', string='Kecamatan')
    # address_view_id = fields.Many2one(
    #     comodel_name='ir.ui.view', string="Input View",
    #     domain=[('model', '=', 'res.partner'), ('type', '=', 'form')],
    #     help="Use this field if you want to replace the usual way to encode a complete address. "
    #          "Note that the address_format field is used to modify the way to display addresses "
    #          "(in reports for example), while this field is used to modify the input form for "
    #          "addresses.")
    #
    # image_url = fields.Char(
    #     compute="_compute_image_url", string="Flag",
    #     help="Url of static flag image",
    # )

    # @api.model
    # def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #     args = args or []
    #     if self.env.context.get('state_id'):
    #         args = expression.AND([args, [('state_id', '=', self.env.context.get('state_id'))]])
    #
    #     if operator == 'ilike' and not (name or '').strip():
    #         first_domain = []
    #         domain = []
    #     else:
    #         first_domain = [('code', '=ilike', name)]
    #         domain = [('name', operator, name)]
    #
    #     first_district_ids = self._search(expression.AND([first_domain, args]), limit=limit,
    #                                       access_rights_uid=name_get_uid) if first_domain else []
    #     return list(first_district_ids) + [
    #         state_id
    #         for state_id in self._search(expression.AND([domain, args]),
    #                                      limit=limit, access_rights_uid=name_get_uid)
    #         if state_id not in first_district_ids
    #     ]
    #
    # def name_get(self):
    #     result = []
    #     for record in self:
    #         result.append((record.id, "{} ({})".format(record.name, record.state_id.code)))
    #     return result
    #
    # def code_get(self):
    #     result = []
    #     for record in self:
    #         result.append((record.id, "{} ({})".format(record.state_id.code, record.code)))
    #     return result
    #
    # @api.depends('code')
    # def _compute_display_code(self):
    #     return self.code_get()
    #     # result = []
    #     # for record in self:
    #     #     result.append((record.id, "{} ({})".format(record.state_id.code, record.code)))
    #     # return result
    #
    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         if vals.get('code'):
    #             vals['code'] = vals['code'].upper()
    #     return super(District, self).create(vals_list)
    #
    # def write(self, vals):
    #     if vals.get('code'):
    #         vals['code'] = vals['code'].upper()
    #     return super(District, self).write(vals)
    #
    # def get_address_fields(self):
    #     self.ensure_one()
    #     return re.findall(r'\((.+?)\)', self.address_format)
    #
    # @api.depends('code')
    # def _compute_image_url(self):
    #     for district in self:
    #         if not district.code:
    #             district.image_url = False
    #         else:
    #             code = self.display_code
    #             district.image_url = "/base/static/img/district_flags/%s.png" % code


class SubDistrict(models.Model):
    _name = 'res.district.sub'
    _description = 'Kecamatan'
    district_id = fields.Many2one('res.district', string='Kabupaten/Kota', required=True)
    code = fields.Char(string="Kode Kecamatan")
    name = fields.Char(string="Nama Kecamatan", index=True)
    display_code = fields.Char(index=True)  # compute='_compute_display_code', store=True,
    # display_name = fields.Char(index=True)  # compute='_compute_display_name', store=True,
    _sql_constraints = [
        ('code_uniq', 'unique (district_id,code)', 'Kode Kecamatan Harus Unik !'),
        ('name_uniq', 'unique (district_id,name)', 'Nama Kecamatan Harus Unik !'),
    ]

class Village(models.Model):
    _name = 'res.district.village'
    _description = "Desa/Keurahan"
    sub_district_id = fields.Many2one('res.district.sub', string='Kecamatan', required=True)
    code = fields.Char(string="Kode Desa/Kelurahan")
    name = fields.Char(string="Nama Desa/Kelurahan", index=True)
    display_code = fields.Char(index=True)  # compute='_compute_display_code', store=True,
    display_name = fields.Char(index=True)  # compute='_compute_display_name', store=True,
    _sql_constraints = [
        ('village_code_uniq', 'unique (sub_district_id,code)', 'Kode Kelurahan/Desa Harus Unik !'),
        ('village_name_uniq', 'unique (sub_district_id,name)', 'Nama Kelurahan/Desa  Harus Unik !'),
    ]

class Postal(models.Model):
    _name = 'res.district.postal'
    _description = 'Kode Pos'
    code = fields.Char(string="Kode Pos")
    village_id = fields.Many2one('res.district.village', string="Kelurahan/Desa" )
    sub_district_id = fields.Many2one('res.district.sub', string='Kecamatan' , required=True)
    district_id = fields.Many2one('res.district', string='Kabupaten/Kota', required=True)
    state_id = fields.Many2one('res.country.state', string='Provinsi', required=True)
    