#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Evan
# @Date:   2016-01-10 15:11:07
# @Last Modified by:   Evan
# @Last Modified time: 2016-01-11 10:25:07
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views,errors