from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    print_selected = fields.Boolean(string='Print Selected')