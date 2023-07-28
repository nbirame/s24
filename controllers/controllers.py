# -*- coding: utf-8 -*-
# from odoo import http


# class S24(http.Controller):
#     @http.route('/s24/s24', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/s24/s24/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('s24.listing', {
#             'root': '/s24/s24',
#             'objects': http.request.env['s24.s24'].search([]),
#         })

#     @http.route('/s24/s24/objects/<model("s24.s24"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('s24.object', {
#             'object': obj
#         })
