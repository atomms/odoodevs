# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lista_tareas(models.Model):
     _name = 'lista_tareas.lista_tareas'
     _description = 'lista_tareas.lista_tareas'

     avatar = fields.Image()
     tarea = fields.Char()
     fecha = fields.Date()
     prioridad = fields.Integer()
     urgente = fields.Boolean(compute="_value_urgente", store=True)
     realizada = fields.Boolean()
     descripcion = fields.Text()
#
     @api.depends('prioridad')
     def _value_urgente(self):

          for record in self:
            #Si la prioridad es mayor que 8, se considera urgente, en otro caso no lo es
            if record.prioridad>8:
                record.urgente = True
            else:
                record.urgente = False

#             record.value2 = float(record.value) / 100