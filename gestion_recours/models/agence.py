from odoo import models, fields

class Agence(models.Model):
    _name = 'recours.agence'
    _description = 'Agence'
    _rec_name = "nom"

    # Odoo gère automatiquement le champ 'id'
    nom = fields.Char(string='Nom de l\'Agence', required=True)

    # Contraints verified by postgres
    _sql_constraints = [
        ('unique_nom', 'unique(nom)', 'Le nom de l\'agence doit être unique.')
    ]

    # Relations
    personnel_ids = fields.One2many('recours.personnel', 'agence_id', string='Personnels')
    assure_ids = fields.One2many('recours.assure', 'agence_id', string='Assurés')
    commission_ids = fields.One2many('recours.commission', 'agence_id', string='Commissions')