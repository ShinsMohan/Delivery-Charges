from odoo import models, fields, api

class SalesOrderSqlView(models.Model):
    _name = 'sales.order.view'
    _description = 'Sales Order View'
    _auto = False

    order_number = fields.Char(string='Order Number')
    date_order = fields.Datetime(string='Order Date')
    customer_name = fields.Char(string='Customer Name')
    amount_total = fields.Float(string='Total Amount')
    product_qty = fields.Float(string='Product Quantity')  # New field
    product_volume = fields.Float(string='Product Volume')  # New field

    @api.model
    def init(self):
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW sales_order_view AS (
                SELECT
                    so.id AS id,
                    so.name AS order_number,
                    so.date_order AS date_order,
                    partner.name AS customer_name,
                    so.amount_total AS amount_total,
                    SUM(sol.product_uom_qty) AS product_qty,
                    SUM(pp.volume * sol.product_uom_qty) AS product_volume
                FROM
                    sale_order AS so
                JOIN    
                    sale_order_line AS sol ON so.id = sol.order_id
                JOIN
                    product_product AS pp ON sol.product_id = pp.id
                JOIN
                    res_partner AS partner ON so.partner_id = partner.id
                GROUP BY
                    so.id, so.name, so.date_order, partner.name, so.amount_total
            )
        """)