from flask import Flask, render_template, request
import boto3
app = Flask(__name__)
from werkzeug.utils import secure_filename


s3 = boto3.client('s3',
                    aws_access_key_id='AKIA2GMDKXUQZR7OKFSW',
                    aws_secret_access_key= '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',

                     )

BUCKET_NAME='arqui'

@app.route('/')  
def home():
    return render_template("form.html")

@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                msg = "Upload Done ! "

    return render_template("form.html",msg =msg)


app.run(host='0.0.0.0', port=8080, debug=True)