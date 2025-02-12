from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError

class Assure(models.Model):
    _name = 'recours.assure'
    _description = 'Assuré'
    _rec_name = "nom"

    num_ss = fields.Char(string='Numéro SS', required=True)
    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    date_naissance = fields.Date(string='Date de Naissance', required=True)
    phone = fields.Char(string='Numéro de Téléphone', required=True)
    email = fields.Char(string='Email', required=True, email=True)
    password = fields.Char(string='Mot de Passe', required=True, password=True)
    genre = fields.Selection([('M', 'Masculin'), ('F', 'Féminin')], string='Genre', required=True)
    adresse = fields.Char(string='Adresse', required=True)
    id_fiche = fields.Char(string='ID Fiche')
    num_dossier = fields.Char(string='Numéro Dossier')
    date_dossier = fields.Date(string='Date Dossier')
    date_cessation_activites = fields.Date(string='Date Cessation Activités')
    date_effet = fields.Date(string='Date Effet')
    date_revision = fields.Date(string='Date Révision')
    montant_servies = fields.Float(string='Montant Servies')
    regime_salarie = fields.Integer(string='Régime Salarié')
    non_salarie = fields.Integer(string='Non Salarié')
    regime_etranger = fields.Integer(string='Régime Étranger')
    moudjahid = fields.Boolean(string='Moudjahid')
    fils_chahid = fields.Boolean(string='Fils de Chahid')
    gratuit = fields.Boolean(string='Gratuit')
    autres_ressources = fields.Char(string='Autres Ressources')

    # Contraints
    _sql_constraints = [
        ('unique_email', 'unique(email)', 'Cet email est déjà utilisé !'),
        ('unique_num_ss', 'unique(num_ss)', 'Ce numéro de sécurité sociale est déjà utilisé !'),
        ('unique_num_dossier', 'unique(num_dossier)', 'Ce numéro de dossier est déjà utilisé !')
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

    # Verify dates
    @api.constrains('date_naissance', 'date_dossier')
    def _check_dates(self):
        """ Vérifie que date_naissance est bien antérieure à date_dossier """
        for record in self:
            if record.date_naissance and record.date_dossier and record.date_naissance >= record.date_dossier:
                raise ValidationError("La Date naissance doit être strictement inférieure à la Date dossier.")

    @api.constrains('date_naissance', 'date_cessation_activites')
    def _check_dates(self):
        """ Vérifie que date_naissance est bien antérieure à date_cessation_activites """
        for record in self:
            if record.date_naissance and record.date_cessation_activites and record.date_naissance >= record.date_cessation_activites:
                raise ValidationError("La Date naissance doit être strictement inférieure à la Date essation d'activites.")

    @api.constrains('date_naissance', 'date_effet')
    def _check_dates(self):
        """ Vérifie que date_naissance est bien antérieure à date_effet """
        for record in self:
            if record.date_naissance and record.date_effet and record.date_naissance >= record.date_effet:
                raise ValidationError(
                    "La Date naissance doit être strictement inférieure à la Date d'effet.")

    @api.constrains('date_naissance', 'date_revision')
    def _check_dates(self):
        """ Vérifie que date_naissance est bien antérieure à date_revision """
        for record in self:
            if record.date_naissance and record.date_revision and record.date_naissance >= record.date_revision:
                raise ValidationError(
                    "La Date naissance doit être strictement inférieure à la Date de revision.")

    #Relations
    agence_id = fields.Many2one('recours.agence', string='Agence', required=True)
    #recours_ids = fields.One2many('recours.recours', 'assure_id', string="Recours")
