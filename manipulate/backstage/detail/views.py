# -*- coding: utf-8 -*-

from flask import Blueprint,render_template,request
import json
from backstage import backstage

mod = Blueprint('topic_geo_analyze',__name__,url_prefix='/topic_geo_analyze')


@rumor.route('/test/')
def test():
    result = 'Hello World!'
    return json.dumps(result,ensure_ascii=False)