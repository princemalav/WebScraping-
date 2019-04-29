import requests , json
from lxml import html
import urllib.request


s=requests.session()
url = 'https://parivahan.gov.in/rcdlstatus/?pur_cd=101'
resp = s.get(url,headers = dict(referer=url))
tree = html.fromstring(resp.content)
def get_captcha_image():
        captcha_image_path = tree.get_element_by_id('form_rcdl:j_idt31:j_idt36')
        captcha_img_url_src = captcha_image_pathimage_path.attrib['src']
        captcha_image_url = 'https://parivahan.gov.in'+img_url_src
        captcha_image = urllib.urlretrieve(captcha_image_url, "captcha-image.jpg")


#dummy function for captcha solve
def get_captcha(imagefile):
        return captcha_text


def post_form():
        licence_no = input('Enter your licence no:- ')
        dob = input('Enter your Date of birth (dd-mm-year):- ')
        captcha = input('Enter captcha: ')        #for testing purpose

        #captcha  = get_captcha(captcha_image)  #after replacing it with your get_captcha()
        form_data = {'form_rcdl:tf_dlNO':licence_no,
                'form_rcdl:tf_dob_input':dob,
                'form_rcdl:j_idt39:CaptchaID':captcha}

        response = s.post(url,data=form_data)
        content = response.content
        if 'Verificaion code does not match' in content:
                print('Captcha is does not match.')
                get_captcha_image()
                post_form()
        else:
                tree = html.fromstring(content)
                current_status = tree.xpath('//*[@id="form_rcdl:j_idt125"]/table[1]/tbody/tr[1]/td[2]/span')
                name = tree.xpath('//*[@id="form_rcdl:j_idt125"]/table[1]/tbody/tr[2]/td[2]')
                Date_of_issue = tree.xpath('//*[@id="form_rcdl:j_idt125"]/table[1]/tbody/tr[3]/td[2]')
                Date_of_expiry = tree.xpath('//*[@id="form_rcdl:j_idt125"]/table[2]/tbody/tr[1]/td[3]/text()')
                vehicle_type = tree.xpath('//*[@id="form_rcdl:j_idt170_data"]/tr/td[2]')

                details = {
                        'current status':current_status,
                        'Name':name,
                        'Date of Issue':Date_of_issue,
                        'Date of Expiry':Date_of_expiry,
                        'Vehicle Type':vehicle_type
                }
                json_data = json.dump(details)
                print(json_data)

post_form()

