from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Recours(models.Model):
    _name = 'recours.recours'
    _description = 'Recours'
    _rec_name = "num_recours"

    num_recours = fields.Char(string='Numéro Recours', required=True)
    objet = fields.Text(string='Objet', required=True)
    date = fields.Date(string='Date', required=True)
    state = fields.Selection([
        ('init', 'Etat initiale'),
        ('pret', 'Prét pour traité'),
        ('en_cours', 'En cours'),
        ('traite', 'Traité'),
        ('national', 'Au niveau national'),
    ], string='State')

    # Contraints
    _sql_constraints = [
        ('unique_num_recours', 'unique(num_recours)', 'Ce numméro de recours est déjà utilisé !'),
    ]

    # Relations
    assure_id = fields.Many2one('recours.assure', string='Assuré', required=True)
    piece_ids = fields.One2many('recours.piece', 'recours_id', string='Pièces')
    decision_ids = fields.One2many('recours.decision', 'recours_id', string='Décisions')

    # Cas recours au  niveau national fait par l'assuré
    # @api.depends('decision_ids')
    # def _compute_state_nationale(self):
    #    for record in self:
    #        if len(record.decision_ids) == 1 and record.decision_ids[0].state == 'refuser':
    #            record.state = 'nationale'

    @api.constrains('decision_ids')
    def _check_state_nationale(self):
        for record in self:
            if len(record.decision_ids) != 1 or record.decision_ids[0].state != 'refuser':
                if record.state == 'nationale':
                    raise ValidationError(
                        "Le recours au niveau national est fait lorsqu'une décision existe et qu'elle est refusée.")

    # Cas décision contestée par le directeur
    personnel_id = fields.Many2one('recours.personnel', string='Directeur conteste décision', required=True)
    decision_id = fields.Many2one('recours.decision', string='Décision contestée', required=True)

    @api.constrains('personnel_id')
    def _check_personnel_profile(self):
        for record in self:
            if record.personnel_id.profil != 'directeur':
                raise ValidationError("Seul un personnel de profile 'Directeur' peut contester une décision.")

    @api.constrains('decision_id')
    def _check_decision_accepted(self):
        for record in self:
            if record.decision_id.decision != 'accepter':
                raise ValidationError("Seules les décisions acceptées peuvent être contestées par le directeur.")

    # Contraite XOR, Soit l'assuré dépose le recours, soit le directeur avec une decision
    @api.constrains('assure_id', 'personnel_id', 'decision_id')
    def _check_xor_constraint(self):
        for record in self:
            has_assure = bool(record.assure_id)
            has_personnel_decision = bool(record.personnel_id and record.decision_id)

            # XOR : l'un doit être vrai, pas les deux
            if not (has_assure ^ has_personnel_decision):
                raise ValidationError(
                    "Un recours doit être lié soit à un Assuré, soit à un Personnel et une Décision, mais pas les deux en même temps.")