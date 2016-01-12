#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Evan
# @Date:   2016-01-10 10:53:47
# @Last Modified by:   Evan
# @Last Modified time: 2016-01-11 16:15:27

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SLOW_DB_QUERY_TIME=0.5

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'productionconfig':ProductionConfig,
	'default': DevelopmentConfig
}