import os
import flask
from flask import template_rendered

upload_folder = r"C:\Users\Administrator\Desktop\日志\day46\Web后端\flask_file_share\uploaded_files"
#文件接收存放的文件夹


app = flask.Flask(__name__)

@app.route("/")
def home():
    file_list = os.listdir(upload_folder)
    return flask.render_template("file_upload.html",file_list=file_list)


@app.route("/file_upload",methods=["POST"])
def file_upload():
    uploaded_file = flask.request.files["file_choose"]
    file_name = uploaded_file.filename
    file_path = os.path.join(upload_folder,file_name)
    uploaded_file.save(file_path)
    
    return "文件上传成功"


@app.route("/file_upload/<file_name>")
def download_file(file_name):
    return flask.send_from_directory(upload_folder,file_name)


if __name__ == "__main__":
    app.run(port=80,debug=True)
