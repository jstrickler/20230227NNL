import requests
import subprocess

NNL_URL = "https://navalnuclearlab.energy.gov/"

response = requests.get(NNL_URL, timeout=5)
if response.status_code == requests.codes.OK:
    page_source = response.text
    print(f"page_source: {page_source}")
print('-' * 60)

PDF_URL = "https://navalnuclearlab-energy-gov.cloudfront.msts.network/docs/April%202021%20Update%20to%20the%20Kesselring%20Site%20Refueling%20and%20Overhaul%20of%20the%20S8G%20Prototype.pdf"

PDF_NAME = "nnl.pdf"

response = requests.get(PDF_URL, headers={'key': 'my_api_key'})
if response.status_code == requests.codes.OK:
    # response.content is contents of PDF
    with open(PDF_NAME, "wb") as nnl_out:
        nnl_out.write(response.content)

subprocess.run(PDF_NAME)