from odoo import fields, models, api
from odoo.exceptions import Warning,ValidationError


class Alcohol(models.Model):
    _name = 'liquorstore.alcohol'
    _description = 'Alcohol'
    name = fields.Char('Nombre', required=True)
    marca = fields.Char('Marca')
    descripcion = fields.Char('Descripcion')
    image = fields.Binary('Image', help="../static/description/imgliquorstore.png")
    active = fields.Boolean('Active?', default=True)
    precio = fields.Integer('Precio',required=True)
    # date_published = fields.Date()
    # publisher_id = fields.Many2one('res.partner', string='Publisher')
    # author_ids = fields.Many2many('res.partner', string='Authors')
    # name = fields.Char(translate=True, required=True)

    # Hierarchy fields

    parent_path = fields.Char(index=True)

    @api.constrains('precio')
    def check_precioCorrecto(self):
        for Alcohol in self:
            if Alcohol.precio <= 0:
                raise Warning('El precio tiene que ser mayor que cero')
