# -*- coding: utf-8 -*-

from odoo import models, fields, api

therapist_specialty = [
    ('1', 'Grief'),
    ('2', 'Anxiety'),
    ('3', 'Burnout'),
    ('4', 'Cognitive'),
    ('5', 'Addictions'),
    ('6', 'OCD'),
    ('7', 'Other'),
]


class Region(models.Model):
    _name = 'therapy.region'
    _description = 'Info about the region where there are therapy centers'

    area_name = fields.Char(string='Area name', size=50, required=True)
    postcode = fields.Integer(string='Postcode')
    area_code = fields.Integer(string='Area code')
    therapy_center = fields.One2many('therapy.therapy', 'area', String='Therapy Center')


class TherapyCenter(models.Model):
    _name = 'therapy.therapy_center'
    _description = 'Therapy centers available to employees'

    therapy_id = fields.Integer(string='Therapy Center ID', required=True)
    therapy_center_name = fields.Char(string='Therapy Center Name', size=30, required=True)
    monthly_users = fields.Integer(string='Max number of users monthly', required=True)
    price_session = fields.Float(string='Price per session', required=True)
    credit_card = fields.Boolean(string='Accept credit card?')
    area = fields.Many2one('therapy.area', string='Ciudad', required=True, ondelete="cascade")
    employees = fields.Many2many('hr.employee', string='Employee', index=True)


class Therapist(models.Model):
    _name = 'therapy.therapist'
    _description = 'Therapist available in each Therapy Center'

    therapist_id = fields.Integer(string='Therapist ID', required=True)
    therapist_name = fields.Char(string='Therapist name', size=80, required=True)
    therapist_specialty = fields.Selection(therapist_specialty, string="Therapist Specialty")
    therapist_center = fields.Many2one('therapy.therapy', string='Therapy Center', required=True, ondelete='cascade')
