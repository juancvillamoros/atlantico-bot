from RPA.Browser.Selenium import Selenium
from utility.handlers_process_utils import handle_error, raise_error, log_message
from services.supabase import insert_filled_ld
from services.captcha import TwoCaptcher
from services.variable_coder import *
from services.zoho_service import *
from services.handlers_process_services import split_fullname
from time import sleep
import os
from SeleniumLibrary.utils.path_formatter import _format_path
EMBED = "EMBED"

browser = Selenium()

def open_webpage(url):
    if url == "":
        raise_error("Please check hardcoded url")
    else:
        for trial in range(3):
            try:
                browser.open_available_browser(url)
                if browser.is_element_visible("//*[@id='form-solicitud']/div[1]/div/h4"):
                    break
            except Exception as e:
                handle_error(e)
        else:
            raise_error(e)


def step_one(persona, fullname, idType, document_id, NombreRepresentateLegal):
    if fullname !="" and document_id != "":
        try:
            # Información del remitente
            if persona == "Natural":
                browser.is_element_visible("/html/body/div[2]/div/div/div/div[1]") 
                if idType !="" and persona == "Persona natural":
                    try:
                        first_name, surname = split_fullname(fullname)
                        browser.select_from_list_by_value("//*[@id='tipo1']") 
                        if idType == "CC":
                            persona = "Natural"
                            #Seleccionar el tipo de documento
                            browser.select_from_list_by_value("//*[@id='bs-select-1-0'] ,Cedula de ciudadania")
                            #Tipear el número de documento
                            browser.input_text("//*[@id='id']", document_id)
                            #Tipear el nombre
                            browser.input_text("//*[@id='nombres']", first_name)
                            #Tipear el apellido
                            browser.input_text("//*[@id='apellidos']", surname)
                            # Seleccionar el país como "Colombia"
                            browser.select_from_list_by_value("*//select[@id='pais']", "Colombia")
                            # Seleccionar el departamento como "ATLANTICO"
                            browser.select_from_list_by_value("*//select[@id='departamento']", "ATLANTICO")
                            # Seleccionar la ciudad / municipio como "BARRANQUILLA"
                            browser.select_from_list_by_value("*//select[@id='ciudad']", "BARRANQUILLA")
                        if idType == "CE":
                            persona = "Natural"
                            #Seleccionar el tipo de documento
                            browser.select_from_list_by_value("//*[@id='bs-select-1-1'] ,Cedula de extranjeria")
                            browser.input_text("//*[@id='id']", document_id)
                            #Tipear el nombre
                            browser.input_text("//*[@id='nombres']", first_name)
                            #Tipear el apellido
                            browser.input_text("//*[@id='apellidos']", surname)
                            # Seleccionar el país como "Colombia"
                            browser.select_from_list_by_value("*//select[@id='pais']", "Colombia")
                            # Seleccionar el departamento como "ATLANTICO"
                            browser.select_from_list_by_value("*//select[@id='departamento']", "ATLANTICO")
                            # Seleccionar la ciudad / municipio como "BARRANQUILLA"
                            browser.select_from_list_by_value("*//select[@id='ciudad']", "BARRANQUILLA")
                        if idType == "PA":
                            persona = "Natural"
                            #Seleccionar el tipo de documento
                            browser.select_from_list_by_value("//*[@id='bs-select-1-2'] ,Pasaporte")
                            #Tipear el número de documento
                            browser.input_text("//input[@id='id']", document_id)
                            #Tipear el nombre
                            browser.input_text("//*[@id='nombres']", first_name)
                            #Tipear el apellido
                            browser.input_text("//*[@id='apellidos']", surname)
                            # Seleccionar el país como "Colombia"
                            browser.select_from_list_by_value("*//select[@id='pais']", "Colombia")
                            # Seleccionar el departamento como "ATLANTICO"
                            browser.select_from_list_by_value("*//select[@id='departamento']", "ATLANTICO")
                            # Seleccionar la ciudad / municipio como "BARRANQUILLA"
                            browser.select_from_list_by_value("*//select[@id='ciudad']", "BARRANQUILLA")
                    except:
                        raise
                elif idType !="" and persona == "Niños, niñas y adolescentes":
                    try:
                        browser.select_from_list_by_value("//*[@id='tipo3']")
                        if idType == "TI":
                            persona = "Natural"
                            browser.select_from_list_by_value("//*[@id='bs-select-1-0'] ,Tarjeta de identidad")
                            #Tipear el número de documento
                            browser.input_text("//input[@id='id']", document_id)
                            #Tipear el nombre
                            browser.input_text("//*[@id='nombres']", first_name)
                            #Tipear el apellido
                            browser.input_text("//*[@id='apellidos']", surname)
                            # Seleccionar el país como "Colombia"
                            browser.select_from_list_by_value("*//select[@id='pais']", "Colombia")
                            # Seleccionar el departamento como "ATLANTICO"
                            browser.select_from_list_by_value("*//select[@id='departamento']", "ATLANTICO")
                            # Seleccionar la ciudad / municipio como "BARRANQUILLA"
                            browser.select_from_list_by_value("*//select[@id='ciudad']", "BARRANQUILLA")
                    except:
                        raise

            if persona == "Juridica":
                #Selecciona el tipo de remitente
                browser.click_element("//*[@id='tipo2']")  
                #Selecciona el tipo de identificación 
                browser.click_element("//*[@id='bs-select-1-0']")
                #Tipea el número de documento
                browser.input_text("//*[@id='id']", document_id)
                #Tipea el nombre de la Razón Social
                browser.input_text("//*[@id='rs']", NombreRepresentateLegal)
                # Seleccionar el país como "Colombia"
                browser.select_from_list_by_value("*//select[@id='pais']", "Colombia")
                # Seleccionar el departamento como "ATLANTICO"
                browser.select_from_list_by_value("*//select[@id='departamento']", "ATLANTICO")
                # Seleccionar la ciudad / municipio como "BARRANQUILLA"
                browser.select_from_list_by_value("*//select[@id='ciudad']", "BARRANQUILLA")
        except Exception as e:
            handle_error(e)
    else:
        ### realease work item as exception since surname is neccessary to fill the form
        raise_error(e)


def step_two(ldname):
    if ldname != "":
        try:
            browser.input_text("//*[@id='direccion']", "CALLE 86 A BIS # 15.12")
            browser.input_text("//*[@id='telefono']", "5140369")
            browser.input_text("//*[@id='celular']", "3226149157")     
            browser.input_text("//*[@id='correo']", "entidades+{0}@juzto.co".format(ldname))       
        except Exception as e:
            handle_error(e)
    else:
        ### realease work item as exception since surname is neccessary to fill the form
        raise_error(e)
    pass

def step_three(ldname, idld, persona, document_type, fullname, idtype, document_id, placa_vehiculo, NombreTitular, TipodeDocumentoTitular, NoDocumentoTitular, FechaDeResoluciónSancionatoria, NoComparendoDelCaso, NoResoluciónSancionatoria, FechaDeComparendo, NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal):
    if ldname != "":
        try:
            # Detalle de la petición
            browser.select_from_list_by_value("*//select[@id='tipoSolicitud']", "Petición")
            # Seleccionar la clasificación previa
            browser.select_from_list_by_value("*//select[@id='temaPQRS']", "Comparendo físico")
            # Seleccionar el medio de respuesta
            browser.select_from_list_by_value("*//select[@id='medioRespuesta']", "Correo electrónico")
            # Esperar a que aparezca la alerta
            browser.wait_until_alert_is_present()
            # Cambiar el control a la alerta
            browser.switch_browser_alert()
            # Aceptar la alerta
            browser.accept_browser_alert()
            browser.input_text("//*[@id='placa']", placa_vehiculo)

            if persona == "Natural":
                # Textarea
                description = pass_details(fullname, idtype, document_id, placa_vehiculo, NombreTitular, TipodeDocumentoTitular, NoDocumentoTitular, FechaDeResoluciónSancionatoria, NoComparendoDelCaso, NoResoluciónSancionatoria, FechaDeComparendo, NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal)
                browser.input_text("*//textarea[@name='comentarios']", description)
                # Documentos adjuntos
                attachment_list = get_attachments(idld)
                attachment_id = get_attachment_id(attachment_list)
                filename = download_attachment(idld, attachment_id, ldname)
                current_dir = os.getcwd()
                filepath = os.path.join(current_dir, filename)
                browser.choose_file("//*[@id='filelimit-fine-uploader']/div/div[2]/input", filepath)
                # Política de Privacidad
                browser.click_element("//*[@id='politica_priv']")
            
            else:
                # Textarea
                description = pass_details(fullname, idtype, document_id, placa_vehiculo, NombreTitular, TipodeDocumentoTitular, NoDocumentoTitular, FechaDeResoluciónSancionatoria, NoComparendoDelCaso, NoResoluciónSancionatoria, FechaDeComparendo, NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal)
                browser.input_text("*//textarea[@name='comentarios']", description)
                # Documentos adjuntos
                attachment_list = get_attachments(idld)
                attachment_id = get_attachment_id(attachment_list)
                filename = download_attachment(idld, attachment_id, ldname)
                current_dir = os.getcwd()
                filepath = os.path.join(current_dir, filename)
                browser.choose_file("//*[@id='filelimit-fine-uploader']/div/div[2]/input", filepath)
                # Política de Privacidad
                browser.click_element("//*[@id='politica_priv']")

            description = pass_details(persona, document_type, fullname, idtype, document_id, placa_vehiculo, NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal, NoResoluciónSancionatoria, FechaDeComparendo, FechaDeResoluciónSancionatoria, NoComparendoDelCaso)
            #captcha
            two_captcher = TwoCaptcher()
            captcha_solution = two_captcher.solve_recaptcha_v2()
            browser.execute_javascript('document.getElementById("g-recaptcha-response").innerHTML="{0}";'.format(captcha_solution))
            #botón
            browser.click_element("//*[@id='btn-submit']")
        except Exception as e:
            raise_error(e)


def _get_screenshot_path(self, filename):
    if self._screenshot_root_directory != EMBED:
        directory = self._screenshot_root_directory or self.log_dir
    else:
        directory = self.log_dir
    filename = filename.replace("/", os.sep)
    index = 0
    while True:
        index += 1
        formatted = _format_path(filename, index)
        path = os.path.join(directory, formatted)
        # filename didn't contain {index} or unique path was found
        if formatted == filename or not os.path.exists(path):
            return path
        
def update_records_on_zoho(idld, ld_name):
    if idld != "":
        browser.wait_until_element_is_visible("/html/body/div/div']", timeout=200)
        try: 
            radicado_number = browser.get_text("/html/body/div/div/div/div/div[2]/div/div[1]/div/strong[1]']")
            log_message(f"El número de radicado para la {idld} es {radicado_number}")
            browser.wait_until_element_is_visible("/html/body/div/div/div/div/div[2]/div/div[1]/div']", timeout=20)  
            sleep(1)
            browser.screenshot("/html/body/div/div/div/div/div[2]/div/div[1]/div", "EVIDENCIA_" + radicado_number + ".png")
            update_records(idld, radicado_number)
            sleep(5)
            api_result = upload_an_attachment(idld, radicado_number)
            browser.close_browser()
            insert_filled_ld(idld, radicado_number, ld_name)
            return api_result
        except Exception as e:
            raise_error(e)