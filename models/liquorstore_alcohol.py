from odoo import fields, models, api
from odoo.exceptions import Warning


class Alcohol(models.Model):
    _name = 'liquorstore.alcohol'
    _description = 'Alcohol'
    name = fields.Char('Nombre', required=True)
    marca = fields.Char('Marca')
    descripcion = fields.Char('Descripcion')
    image = fields.Binary('Image', help="../static/description/imgliquorstore.png")
    active = fields.Boolean('Active?', default=True)
    precio = fields.Integer()
    # date_published = fields.Date()
    # publisher_id = fields.Many2one('res.partner', string='Publisher')
    # author_ids = fields.Many2many('res.partner', string='Authors')
    # name = fields.Char(translate=True, required=True)

    # Hierarchy fields
    parent_id = fields.Many2one(
        'liquorstore.alcohol.tipo',
        'Parent Category',
        ondelete='restrict')
    parent_path = fields.Char(index=True)