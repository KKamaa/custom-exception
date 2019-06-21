# -*- coding: utf-8 -*-
#   © 2019 Kevin Kamau
#   License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl)


class UserError(Exception):
    """ custom odoo Error exception """


class UserInfo(Exception):
    """custom odoo User info message after action """


class UserSuccess(Exception):
    """ custom odoo successfull exection """
