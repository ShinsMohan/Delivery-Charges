from odoo import models, fields, api

class DeliveryComments(models.Model):
    _inherit = 'sale.order'

    delivery_comments = fields.Text(string='Delivery Comments')
    delivery_terms = fields.Char(string="Delivery Terms", default=lambda self: self._get_default_delivery_terms(), readonly=True)

    def _create_invoices(self, grouped=False, final=False, date=None):
        moves = super(DeliveryComments, self)._create_invoices(grouped=grouped, final=final, date=date)
        for move in moves:
            move.delivery_comments = self.delivery_comments
            move.delivery_terms = self.delivery_terms
        return moves
    
    @api.model
    def _get_default_delivery_terms(self):
        delivery_terms = self.env['ir.config_parameter'].sudo().get_param('delivery_charge.delivery_terms', default="")
        return delivery_terms
    
    # FUNCTION OPEN WIZARD
    def action_open_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Import Sale Order Document',
            'view_mode': 'form',
            'res_model': 'sale.order.wizard',
            'target': 'new',
            'context': {
                'default_sale_order_id': self.id,
            },
        }