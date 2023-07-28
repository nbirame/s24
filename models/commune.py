from odoo import models, fields, api


class Commune(models.Model):
    _name = "s24.commune"
    _description = "Commune"

    name = fields.Char(string="Nom", required=True)
    nombre_habitant = fields.Integer(string="Nombre d'Habitants")
    nombre_partisant = fields.Integer(string="Nombre de partisants")
    coordonnateur_id = fields.Many2one("hr.employee", string="Coordonnateur")
    departement_id = fields.Many2one("hr.department", string="Département")
    # partisant_ids = fields.One2many("hr.employee", "commune_id", string="Partisant", store=True)