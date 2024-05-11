import simplejson
import http.client
from hashlib import sha1


class WPSService():

    def __init__(self):

        APPID = "YOUR_APPID"
        APPKEY = b"YOUR_APPKEY"
        Content_Md5 = b"d41d8cd98f00b204e9800998ecf8427e"
        Content_Type = b"application/json"
        Date = b"Wed, 23 Jan 2013 06:43:08 GMT"

        signature = sha1(APPKEY + Content_Md5 + Content_Type + Date).hexdigest()

        self.Authorization = 'WPS-2:%s:%s' % (APPID, signature)

    def convert_pdf_to_docx(self, url, dst_file_type="docx"):

        conn = http.client.HTTPSConnection("solution.wps.cn")

        payload = "{\"url\":\"%s\"}" % url

        headers = {
            'Date': "Wed, 23 Jan 2013 06:43:08 GMT",
            'Content-Md5': "d41d8cd98f00b204e9800998ecf8427e",
            'Content-Type': "application/json",
            'Authorization': self.Authorization
            }

        conn.request("POST", "/api/developer/v1/office/pdf/convert/to/%s" % dst_file_type, payload, headers)

        res = conn.getresponse()
        data = res.read()
        task_data = simplejson.loads(data.decode("utf-8"))

        task_id = task_data.get("data").get("task_id")

        return task_id

    def get_task_status(self, task_id):

        conn = http.client.HTTPSConnection("solution.wps.cn")

        headers = {
            'Date': "Wed, 23 Jan 2013 06:43:08 GMT",
            'Content-Md5': "d41d8cd98f00b204e9800998ecf8427e",
            'Content-Type': "application/json",
            'Authorization': self.Authorization
            }

        conn.request("GET", "/api/developer/v1/tasks/convert/to/pptx/%s" % task_id, headers=headers)

        res = conn.getresponse()
        data = res.read()

        data_res = simplejson.loads(data.decode("utf-8"))

        download_url = data_res["data"].get("download_url")

        return download_url
