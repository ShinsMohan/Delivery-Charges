from odoo import models, fields

class DeliveryTerms(models.TransientModel):
    _inherit = 'res.config.settings'

    delivery_terms = fields.Char(string="Delivery Terms", config_parameter='delivery_charge.delivery_terms')