from odoo import models, fields, api

class Commission(models.Model):
    _name = 'recours.commission'
    _description = 'Commission'
    _rec_name = "ref"

    ref = fields.Char(string='Ref', required=True)
    date_debut = fields.Date(string='Date Début', required=True)
    date_fin = fields.Date(string='Date Fin')
    type = fields.Selection([('l', 'Locale'), ('n', 'Nationale')], string='Type', required=True)

    # Verify dates
    @api.constrains('date_debut', 'date_fin')
    def _check_dates(self):
        for record in self:
            if record.date_debut and record.date_fin and record.date_debut >= record.date_fin:
                raise ValidationError("La Date début doit être strictement inférieure à la Date fin.")

    # Relations
    agence_id = fields.Many2one('recours.agence', string='Agence', required=True)
    membre_ids = fields.Many2many('recours.membre', string="Membres", required=True)
    reunion_ids = fields.One2many('recours.reunion', 'commission_id', string='Réunions')