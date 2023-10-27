# -*- encoding: utf-8 -*-
"""
"""

from flask import Blueprint

blueprint = Blueprint(
    'receiver_blueprint',
    __name__,
    url_prefix=''
)
