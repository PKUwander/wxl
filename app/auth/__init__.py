#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Evan
# @Date:   2016-01-10 15:19:26
# @Last Modified by:   Evan
# @Last Modified time: 2016-01-11 16:55:44
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views