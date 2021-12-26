from flask import Flask, render_template, request
import boto3
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)


app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'app',
    'SECRET_TOKEN': 'VmWj7v2Er8WoiiDPN3',
    'SERVER_URL': 'https://9a9fa401c090449ab47ec8a07f8dc47b.apm.eu-west-1.aws.cloud.es.io:443',
    'DEBUG': True
    }
apm = ElasticAPM(app)

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