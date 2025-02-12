from odoo import models, fields

class Loi(models.Model):
    _name = 'recours.loi'
    _description = 'Loi'

    date = fields.Date(string='Date de de la loi', required=True)
    contenu = fields.Char(string='Contenu de la loi', required=True)