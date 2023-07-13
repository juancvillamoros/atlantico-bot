"""main bot"""
from handlers.process import open_webpage, step_one, step_two, step_three, update_records_on_zoho
from services.supabase import check_DB_for_LD
from services.variable_coder import *
from utility.handlers_process_utils import handle_error, log_message
from RPA.Robocorp.WorkItems import WorkItems
from zcrmsdk import ZCRMRestClient

# Configurar el cliente de Zoho CRM
ZCRMRestClient.initialize()
oAuthClient = ZCRMRestClient.get_instance().generate_oauth_client()

workitem = WorkItems()
workitem.get_input_work_item()
url = "https://orfeo.transitodelatlantico.gov.co/formularioWeb/"

# Obtener las variables de Zoho CRM

FechaDeResoluciónSancionatoria = workitem.get_work_item_variable("FechaDeResolucionSancionatoria").replace("-", "/")
NoResoluciónSancionatoria = workitem.get_work_item_variable("NoResolucionSancionatoria")
FechaDeComparendo = workitem.get_work_item_variable("FechaDeComparendo").replace("-", "/")
NombreRepresentateLegal = workitem.get_work_item_variable("NombreRepresentateLegal")
TipodeDocumentoRepresentateLegal = workitem.get_work_item_variable("TipodeDocumentoRepresentateLegal") 
DocumentoRepresentateLegal = workitem.get_work_item_variable("DocumentoRepresentateLegal")
document_id = workitem.get_work_item_variable("idnumber") 
fullname = workitem.get_work_item_variable("fullname") 
idtype= workitem.get_work_item_variable("idtype")
NoComparendoDelCaso= workitem.get_work_item_variable("NoComparendoDelCaso")
persona, tipo_de_documento = encode_idtpe(idtype) 
idld= workitem.get_work_item_variable("idld")
document_type = workitem.get_work_item_variable("document_type")
ldname = workitem.get_work_item_variable("ldname")
placa_vehiculo = workitem.delete_work_item_variable("Placa_vehiculo")

# Resto del código
def robot_atlantico():
    for trial in range(2):
        try:
            log_message("Robot starts")
            if check_DB_for_LD(idld):
                open_webpage(url)
                step_one(persona, ldname, document_id, fullname)
                step_two(ldname)
                step_three(ldname, idld, persona, document_type, fullname, idtype, document_id, placa_vehiculo, FechaDeResoluciónSancionatoria, NoComparendoDelCaso, NoResoluciónSancionatoria, FechaDeComparendo, NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal)
                api_status = update_records_on_zoho(idld, ldname)
                robot_status = robot_status(api_status)
                if robot_status == "success":    
                    log_message("Robot finishes successfully")
                    break
            else:
                raise ValueError("This LD has been filed before")
        except Exception as e:
            handle_error(f"ROBOT FAILED because: {e}")
    else:
        workitem.release_input_work_item(state="FAILED", exception_type="BUSINESS")


if __name__ == "__main__":
    robot_atlantico()