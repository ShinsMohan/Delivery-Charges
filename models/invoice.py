from odoo import models, fields, api


class InvoiceComments(models.Model):
    _inherit = 'account.move'

    delivery_comments = fields.Text(string='Delivery Comments')
    delivery_terms = fields.Char(string="Delivery Terms", readonly=True)