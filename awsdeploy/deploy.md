### Layer Deployment
pip install --upgrade --no-deps --target awsdeploy\python .
7z a envirodataqc_vX.zip python
aws lambda publish-layer-version \
    --layer-name EnviroDataQC \
    --description "Version number" \
    --compatible-runtimes python3.6 python 3.7 python 3.8 \
    --zip-file fileb://<filename>