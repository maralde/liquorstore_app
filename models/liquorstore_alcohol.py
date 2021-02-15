from odoo import fields, models, api
from odoo.exceptions import Warning


class Alcohol(models.Model):
    _name = 'liquorstore.alcohol'
    _description = 'Alcohol'
    name = fields.Char('Name', required=True)
    marca = fields.Char('Marca')
    active = fields.Boolean('Active?', default=True)
    # date_published = fields.Date()
    image = fields.Binary('Image')
    # publisher_id = fields.Many2one('res.partner', string='Publisher')
    # author_ids = fields.Many2many('res.partner', string='Authors')
