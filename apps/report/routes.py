# -*- encoding: utf-8 -*-
"""
"""
from apps.authentication.models import TEvent
from apps.report import blueprint
from flask import render_template, request, send_from_directory,session
from flask_login import login_required
from jinja2 import TemplateNotFound

from apps.report.datas import TData

data=TData()
@blueprint.route('/report')
@login_required
def report_view():
	result=data.get_report_view()
	return render_template('report/report_view.html',data_list=result)

@blueprint.route('/api', methods=['POST'])
def api_json():

	print("===============")
	json_content = request.get_json()
	goodToken=False

	if "Token" in json_content:

		if json_content["Token"]=="3e2jiAc69b674cCDCAc69b674cCDCc62":
			goodToken=True
    
	if not goodToken:
		return "error"
	result=data.get_report_json()
	
	return result

"""
@blueprint.route('/report')
@login_required
def index():
    data_list=TEvent.query.all()
    
    for data in data_list:
        print("資料:",data.score, ",",data.raw_file)
    return render_template('report/index.html', segment='index',data_list=data_list)


import sys
if sys.platform.startswith('win32'):
    file_folder="..\\download_files"

elif sys.platform.startswith('linux'):
    file_folder="/home/ray/CloudReceiver/download_files"
@blueprint.route('/download/<filename>')
def download_file(filename):
    global file_folder
    return send_from_directory(file_folder, filename, as_attachment=True)

"""