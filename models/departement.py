from odoo import models, fields, api


class Departement(models.Model):
    _inherit = "hr.department"
    _description = "Département"

    nombre_habitant = fields.Integer(string="Nombre d'habitant")
    # nombre_commune = fields.Integer(string="Nombre de Commune")
    nombre_partisant = fields.Integer(string="Nombre de partisant")
    coordonnateur_id = fields.Many2one("hr.employee", string="Coordonnateur")
    partisant_ids = fields.One2many("hr.employee", "departement_id", string="Partisant", store=True)
    # commune_ids = fields.One2many("s24.commune", "departement_id", string="Commune", store=True)