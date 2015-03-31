# -*- encoding: utf-8 -*-
from openerp import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _display_address(self, cr, uid, address, without_company=False, context=None):
        address_format = address.country_id.address_format or \
              "%(street)s\n%(street2)s\n%(city)s\n%(state_name)s\n%(zip)s\n%(country_name)s"
        args = {
            'state_code': address.state_id.code or '',
            'state_name': address.state_id.name or '',
            'country_code': address.country_id.code or '',
            'country_name': address.country_id.name or '',
            'company_name': address.parent_name or '',
        }
        for field in self._address_fields(cr, uid, context=context):
            args[field] = getattr(address, field) or ''
        if without_company:
            args['company_name'] = ''
        elif address.parent_id:
            address_format = '%(company_name)s\n' + address_format
        return address_format % args