from odoo import models, fields
from io import BytesIO
from odoo.exceptions import UserError
import base64
import xlrd

class SaleOrderWizard(models.TransientModel):
    _name = 'sale.order.wizard'
    _description = "Open Sale Order Import Wizard"

    xml_file = fields.Binary(string='Upload XML File', required=True)
    sale_order_id = fields.Many2one("sale.order", string="Ordered ID")


    def import_xml(self):
        file = base64.b64decode(self.xml_file)
        workbook = xlrd.open_workbook(file_contents=file)
        worksheet = workbook.sheet_by_index(0)

        for row_index in range(1, worksheet.nrows): #skip header
            product_name = worksheet.cell(row_index, 0).value
            qty = worksheet.cell(row_index, 1).value
            unit_price = worksheet.cell(row_index, 2).value

            # Find product by name
            product = self.env['product.product'].search([('name', '=', product_name)], limit=1)
            if product:
                # Create Sales Order line
                self.env['sale.order.line'].create({
                    'order_id': self.sale_order_id.id,
                    'product_id': product.id,
                    'product_uom_qty': qty,
                    'price_unit': unit_price,
                })
            else:
                raise UserError("not found")
        
        return {'type': 'ir.actions.act_window_close'} # Close wizard if action is completed