from odoo import models, fields, api

class Reunion(models.Model):
    _name = 'recours.reunion'
    _description = 'Réunion'

    arret_ministeriel = fields.Char(string='Arret ministeriel', required=True)
    date = fields.Date(string='Date', required=True)
    heure = fields.Float(string="Heure", help="Heure au format HH:MM")
    state = fields.Selection([
        ('pas_commencer', 'Pas commencer'),
        ('en_cours', 'En cours'),
        ('terminer', 'Terminée'),
    ], string='State', default='pas_commencer')

    # Relations
    recours_ids = fields.Many2many('recours.recours', string="Recours", required=True,
                                   domain=[('state', '=', 'pret')])
    commission_id = fields.Many2one('recours.commission', string='Commission', required=True)
