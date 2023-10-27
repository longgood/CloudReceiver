# -*- encoding: utf-8 -*-
"""
"""
from apps.authentication.models import TEvent
from apps.report import blueprint
from flask import render_template, request, send_from_directory
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/report')
@login_required
def index():
    data_list=TEvent.query.all()
    
    for data in data_list:
        print("資料:",data.score, ",",data.raw_file)
    return render_template('report/index.html', segment='index',data_list=data_list)
    
@blueprint.route('/download/<filename>')
def download_file(filename):
    file_folder="D:\\projects\\CloudReceiver\\download_files"
    return send_from_directory(file_folder, filename, as_attachment=True)

