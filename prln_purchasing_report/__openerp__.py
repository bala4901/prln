# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Michael Viriyananda
#    Copyright 2015 OpenSynergy Indonesia
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Pralon Purchasing Report Module',
    'version': '1.0.0',
    'author': "Michael Viriyananda,OpenSynergy Indonesia",
    'license': 'AGPL-3',
    'category': 'Reporting',
    'depends': [
        'purchase',
        'purchase_requisition',
        'pralon_purchase_enhancements',
        'report_aeroo_ooo',
        'pralon_accounting_reports'
    ],
    'description': """
Purchasing Report Based On Purchase Order.
============================

Creates a purchasing report for accountants based using aeroo
--------------------------------------------------
* Wizard with parameter:
    - Companies
    - Departments
    - PO Date From
    - PO Date To
    - Output Format(PDF/XLS/CSV)

    """,
    'website': 'http://opensynergy-indonesia.com',
    'data': [
        'security/ir.model.access.csv',
        'wizards/purchasing.xml',
        'view/view_ResCompany.xml',
        'report/report.xml',
        'menu_Accounting.xml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True
}
