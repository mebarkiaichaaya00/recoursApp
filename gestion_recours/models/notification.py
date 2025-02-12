from odoo import models, fields

class Notification(models.Model):
    _name = 'recours.notification'
    _description = 'Notification'

    num_notif = fields.Char(string='N° notification', required=True)
    date = fields.Date(string='Date', required=True)
    state = fields.Selection([('consulter', 'Consultée'),('non_cons', 'Non consultée')],
                            string='Etat', required=True)

    # Contraints
    _sql_constraints = [
        ('unique_num_notif', 'unique(num_notif)', 'Ce numéro est déjà utilisé !')
    ]

