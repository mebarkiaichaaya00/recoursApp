from pkg_resources import require

from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError

class Personnel(models.Model):
    _name = 'recours.personnel'
    _description = 'Personnel'
    _rec_name = "nom"

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    date_naissance = fields.Date(string='Date de Naissance', required=True)
    phone = fields.Char(string='Numéro de Téléphone', required=True)
    email = fields.Char(string='Email', required=True, email=True)
    password = fields.Char(string='Mot de Passe', required=True, password=True)
    state = fields.Selection([('act', 'Activé'), ('desact', 'Désactivé')], string='Statut Compte',
                                     required=True)
    profile = fields.Selection([('secrtL', 'Secrétaire CRLPQ'), ('secrtN', 'Secrétaire CRNPQ'),
                                ('presidL', 'Président CRLPQ'), ('presidN', 'Président CRNPQ'),
                                ('direct', 'Directeur'), ('sdPension', 'Sous-Directeur des Pensions'),
                                ('membreL', 'Membre CRLPQ'), ('membreN', 'Membre CRNPQ')], string='Profile',
                                required=True)

    # Contraints
    _sql_constraints = [
        ('unique_email', 'unique(email)', 'Cet email est déjà utilisé !')
    ]

    # Verify phone number
    @api.constrains('phone')
    def _check_phone_number(self):
        """ Vérifie que le numéro de téléphone commence par 06, 05 ou 07 et contient 10 chiffres """
        phone_pattern = re.compile(r'^(06|05|07)[0-9]{8}$')  # Regex pour 06, 05, 07 + 8 chiffres
        for record in self:
            if record.phone and not phone_pattern.match(record.phone):
                raise ValidationError(
                    "Le numéro de téléphone doit commencer par 06, 05 ou 07 et contenir 10 chiffres (ex: 0654123456).")

    # Verify password length
    @api.constrains('password')
    def _check_password_length(self):
        """ Vérifie que le mot de passe contient au moins 8 caractères """
        for record in self:
            if len(record.password) < 8:
                raise ValidationError("Le mot de passe doit contenir au moins 8 caractères.")

    # Relations
    agence_id = fields.Many2one('recours.agence', string='Agence', required=True)
    recours_ids = fields.One2many('recours.recours', 'personnel_id', string="Décisions contestées par le Directeur")