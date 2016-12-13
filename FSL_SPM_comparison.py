import os
from rdflib.graph import Graph
from rdflib.term import URIRef
from subprocess import check_call
from nidmresults.graph import Graph
from nidmresults.objects.constants import SCR_FSL, SCR_SPM
import collections
import glob
import zipfile
import json
from urllib2 import urlopen, URLError, HTTPError
from urllib2 import Request
# import matlab.engine

request = Request('http://neurovault.org/api/collections/ZJNRUHIM/nidm_results/?limit=184&format=json')
response = urlopen(request)
elevations = response.read()
data = json.loads(elevations)

pwd = os.path.dirname(os.path.realpath('__file__'))
data_dir = os.path.join(pwd, "Neurovault_data")


if not os.path.isdir(data_dir):
    os.makedirs(data_dir)


for nidm_result in data["results"]:
    url = nidm_result["zip_file"]
    study_name = nidm_result["name"]
    
    localzip = os.path.join(data_dir, study_name + ".zip")
    localzip_rel = localzip.replace(pwd, '.')
    if not os.path.isfile(localzip):
        # Copy .nidm.zip export locally in a the data directory
        try:
            f = urlopen(url)
            print("downloading " + url + " at " + localzip_rel)
            with open(localzip, "wb") as local_file:
                local_file.write(f.read())
        except HTTPError, e:
            raise Exception(["HTTP Error:" + e.code + url])
        except URLError, e:
            raise Exception(["URL Error:" + e.reason + url])
    else:
        print(url + " already downloaded at " + localzip_rel)


request = Request('http://neurovault.org/api/collections/UMMSIQGP/nidm_results/?limit=184&format=json')
response = urlopen(request)
elevations = response.read()
data = json.loads(elevations)

pwd = os.path.dirname(os.path.realpath('__file__'))
data_dir = os.path.join(pwd, "Neurovault_data")


if not os.path.isdir(data_dir):
    os.makedirs(data_dir)


for nidm_result in data["results"]:
    url = nidm_result["zip_file"]
    study_name = nidm_result["name"]
    
    localzip = os.path.join(data_dir, study_name + ".zip")
    localzip_rel = localzip.replace(pwd, '.')
    if not os.path.isfile(localzip):
        # Copy .nidm.zip export locally in a the data directory
        try:
            f = urlopen(url)
            print("downloading " + url + " at " + localzip_rel)
            with open(localzip, "wb") as local_file:
                local_file.write(f.read())
        except HTTPError, e:
            raise Exception(["HTTP Error:" + e.code + url])
        except URLError, e:
            raise Exception(["URL Error:" + e.reason + url])
    else:
        print(url + " already downloaded at " + localzip_rel)


spm_archive = zipfile.ZipFile(os.path.join(data_dir, "spm_0001.nidm.zip"), 'r')
spm_archive.extractall(os.path.join(data_dir, "spm_0001.nidm"))
spm_archive.close()
spm_dir = os.path.join(data_dir, "spm_0001.nidm")

fsl_archive = zipfile.ZipFile(os.path.join(data_dir, "group.gfeat.nidm.zip"), 'r')
fsl_archive.extractall(os.path.join(data_dir, "group.gfeat.nidm"))
fsl_archive.close()
fsl_dir = os.path.join(data_dir, "group.gfeat.nidm")


spm_tstat1 = os.path.join(spm_dir, "TStatistic.nii.gz")
fsl_tstat1 = os.path.join(fsl_dir, "TStatistic_T001.nii.gz")
path_to_spm = "/Users/maullz/Software/spm12"
cmd = "matlab -r 'addpath(\'"+path_to_spm+"\'); spm_reslice(\'"+spm_tstat1+"\', \'"+fsl_tstat1+"\')'"
print(cmd)
check_call(cmd, shell=True)

# eng = matlab.engine.start_matlab()
# eng.spm_reslice({spm_tstat1,fsl_tstat1})