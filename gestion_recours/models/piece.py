from odoo import models, fields

class Piece(models.Model):
    _name = 'recours.piece'
    _description = 'Pièce'
    _rec_name = "nom"

    nom = fields.Char(string='Nom du fichier')
    fichier = fields.Binary(string='Fichier')

    # Relations
    recours_id = fields.Many2one('recours.recours', string='Recours', required=True)
