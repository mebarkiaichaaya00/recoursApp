from odoo import models, fields

class Decision(models.Model):
    _name = 'recours.decision'
    _description = 'Décision'

    decision = fields.Selection([
        ('accepter', 'Accepté'),
        ('refuser', 'Refusé')
    ], string='Décision', required=True)
    texte = fields.Text(string='Texte', required=True)

    # Relations
    recours_id = fields.Many2one('recours.recours', string='Recours')
    loi_ids = fields.Many2many('recours.loi', string='Lois Concernées')
    notification_id = fields.Many2one('recours.notification', string='Notification')
