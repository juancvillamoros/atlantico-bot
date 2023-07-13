import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

def captcha_cracker():
    api_key = os.getenv('APIKEY_2CAPTCHA', '66a780879e183c8fc52eadd47e786180') 

    solver = TwoCaptcha(api_key)

    try:
        result = solver.solve_captcha(
            site_key='6LeK8NUZAAAAAMBHUd8ZsGM1zJb-RXROmLXylmGl',
            page_url='https://orfeo.transitodelatlantico.gov.co/formularioWeb/')

    except Exception as e:
        sys.exit(e)

    else:
        return str(result)

class TwoCaptcher:
        def solve_recaptcha_v2(self):
            api_key = os.getenv('APIKEY_2CAPTCHA', '66a780879e183c8fc52eadd47e786180') 
            solver = TwoCaptcha(api_key)
            for i in range(0,10):
                try:
                    result = solver.solve_captcha(
                        sitekey='6LeK8NUZAAAAAMBHUd8ZsGM1zJb-RXROmLXylmGl',
                        url='https://orfeo.transitodelatlantico.gov.co/formularioWeb/')
                    return [True,result]
                except:
                    pass
            return [False,"failed 10 times"]
