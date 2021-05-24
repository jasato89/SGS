# -*- coding: utf-8 -*-
# from odoo import http


# class Therapy(http.Controller):
#     @http.route('/therapy/therapy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/therapy/therapy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('therapy.listing', {
#             'root': '/therapy/therapy',
#             'objects': http.request.env['therapy.therapy'].search([]),
#         })

#     @http.route('/therapy/therapy/objects/<model("therapy.therapy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('therapy.object', {
#             'object': obj
#         })
