from odoo import models, fields, api


class Partisant(models.Model):
    _inherit = "hr.employee"
    _description = "Partisant"

    numero_cedeao = fields.Integer(string="N° de la Carte d'identité")
    departement_id = fields.Many2one("hr.department", string="Departement", required=True)
    # commune_id = fields.Many2one("s24.commune", string="Commune", required=True)