from api import WPSService


if __name__ == '__main__':

    wps_service = WPSService()

    file_url = "http://www.caict.ac.cn/english/research/whitepapers/202303/P020230316608528378472.pdf"
    task_id = wps_service.convert_pdf_to_docx(file_url)

    while True:
        download_url = wps_service.get_task_status(task_id)

        if len(download_url) > 0:
            break

    print('download_url:', download_url)