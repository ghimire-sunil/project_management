# -*- coding: utf-8 -*-
# from odoo import http


# class SmartenProject(http.Controller):
#     @http.route('/smarten_project/smarten_project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/smarten_project/smarten_project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('smarten_project.listing', {
#             'root': '/smarten_project/smarten_project',
#             'objects': http.request.env['smarten_project.smarten_project'].search([]),
#         })

#     @http.route('/smarten_project/smarten_project/objects/<model("smarten_project.smarten_project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smarten_project.object', {
#             'object': obj
#         })

