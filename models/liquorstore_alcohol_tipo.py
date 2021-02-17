from odoo import api, fields, models

class AlcoholTipo(models.Model):
    _name = 'liquorstore.alcohol.tipo'
    _description = 'Alcohol Category'
    _parent_store = True
    name = fields.Char('Nombre', required=True)

    parent_id = fields.Many2one(
        'liquorstore.alcohol',
        'Parent Category',
        ondelete='cascade')
    parent_path = fields.Char(index=True)

