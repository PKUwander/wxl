#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Evan
# @Date:   2016-01-10 15:54:14
# @Last Modified by:   Evan
# @Last Modified time: 2016-01-11 21:59:21
from . import main
from flask import render_template, redirect, url_for, abort, flash, request, current_app, make_response
from flask.ext.login import login_required, current_user
from flask.ext.sqlalchemy import get_debug_queries
from .. import db
from ..models import User

@main.after_app_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= current_app.config['SLOW_DB_QUERY_TIME']:
            current_app.logger.warning(
                'Slow query: %s\nParameters: %s\nDuration: %fs\nContext: %s\n'
                % (query.statement, query.parameters, query.duration,
                   query.context))
    return response

@main.route('/')
def index():
	return render_template('index.html',current_user=current_user)

@main.route('/admin')
def admin():
	return render_template('admin.html',current_user=current_user)

@main.route('/manager')
def manager():
	return render_template('manager.html',current_user=current_user)

@main.route('/trader')
def trader():
	return render_template('trader.html',current_user=current_user)

@main.route('/other')
def other():
	return render_template('other.html',current_user=current_user)
