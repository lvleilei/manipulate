# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, jsonify, Blueprint, send_from_directory, url_for, session
import json

mod = Blueprint("index",__name__,url_prefix='/index')


@mod.route('/backstage/test')
def test():
	return render_template('backstage/1.html')



@mod.route('/dashboard/test')
def test2():
	return render_template('dashboard/2.html')

# 业务系统 -态势分析
@mod.route('/newSituationtem')
def test2():
    return render_template('dashboard/2.html')