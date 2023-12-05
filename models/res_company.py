# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class Company(models.Model):
    _inherit = 'res.company'

    employer_num_ids = fields.One2many("res.company.affiliation",'company_id')


class CompanyAffiliation(models.Model):
    _name = 'res.company.affiliation'


    company_id = fields.Many2one("res.company",ondelete='cascade')
    agency_id = fields.Many2one("res.partner",string='Agency',domain=[('is_company','=',True)],required=True)
    employer_num = fields.Char(string='Employer number',required=True)