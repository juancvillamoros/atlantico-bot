"""Decode the idtype"""
def encode_idtpe(idtype_code):
    try:
        if idtype_code == "CC":
            persona = "Natural"
            tipo_de_documento = "Cedula de ciudadania"
        
        if idtype_code == "TI":
            persona = "Natural"
            tipo_de_documento = "Tarjeta de identidad"

        if idtype_code == "PA":
            persona = "Natural"
            tipo_de_documento = "Pasaporte"

        if idtype_code == "NIT":
            persona = "Juridica"
            tipo_de_documento = "Nit"

        if idtype_code == "CE":
            persona = "Natural"
            tipo_de_documento = "Cedula de extranjeria"
    except:
        raise

    return persona, tipo_de_documento

def pass_details(persona, document_type, fullname, idtype, document_id, placa_vehiculo, NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal, NoResoluciónSancionatoria, FechaDeComparendo, FechaDeResoluciónSancionatoria, NoComparendoDelCaso):
    try:
        '''ALVARO MARTINEZ DE LA VEGA, quien se identifica con CC No. 98.378.315 propietario del vehículo de placas
        ZIS235 con fundamento en el artículo 23 de la Constitución Política de Colombia y las demás normas concordantes
        que lo regulan y desarrollan, presento ante ustedes el presente derecho de petición.'''    
        if persona == "Natural":
       
            if document_type.startswith("Derecho de petición"):
                description = "Buen día,\n Yo, {0}, identificado con {1} No. {2} propietario del vehículo de placas {3}. Con todo respeto manifiesto a usted que presentó derecho de petición.\n Cordialmente".format(fullname, idtype, document_id, placa_vehiculo)
            if document_type.startswith("Caducidad"):
                description = "Buen día,/n Yo, {0}, identificado con {1} No. {2} propietario del vehículo de placas {3}. Con todo respeto manifiesto a usted que presentó caducidad contra el\n comparendo No. {4} del {5}.\n Cordialmente.".format(fullname, idtype, document_id, placa_vehiculo, NoComparendoDelCaso, FechaDeComparendo)
            if document_type.startswith("Revocatoria"):
                description = "Buen día, \nYo, {0}, identificado con {1} No. {2} propietario del vehículo de placas {3}. Con todo respeto manifiesto a usted que presentó revocatoria directa contra la Resolución {4} del {5}. \nCordialmente.".format(fullname, idtype, document_id, placa_vehiculo, NoResoluciónSancionatoria, FechaDeResoluciónSancionatoria) 
            if document_type == "Prescripción":
                description = "Buenas tardes, \nYo, {0}, identificado con {1} No. {2} propietario del vehículo de placas {3}. Con todo respeto manifiesto a usted que presento prescripción contra de la Resolución {3} del {4}. \nCordialmente.".format(fullname, idtype, document_id, placa_vehiculo, NoResoluciónSancionatoria, FechaDeResoluciónSancionatoria)
        '''PETRODYNAMIC PETROLEUM SERVICES SAS, sociedad debidamente constituida e identificada con Nit.
        900468628-9, representada por Fabian Montoya quien se identifica con CC No. 94.365.982 propietario del vehículo
        de placas DSK229 con fundamento en el artículo 23 de la Constitución Política de Colombia y las demás normas
        concordantes que lo regulan y desarrollan, presento ante ustedes el presente derecho de petición.'''
        if persona == "Juridica":
            if document_type.startswith("Derecho de petición"):
                description = "Buen día, \n {0}, sociedad debidamente constituida e identificada con {1} No. {2}, representada por {3} quien se identifica con {4} {5} propietario del vehículo de placas {6} con todo respeto manifiesto a usted que presentó derecho de petición. \nCordialmente.".format(fullname, document_type, document_id, NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal, placa_vehiculo)
            if document_type.startswith("Caducidad"):
                description = "Buen día, \nYo, {0}, sociedad debidamente constituida e identificada con {1} No. {2}, representada por {3} quien se identifica con {4} {5} propietario del vehículo de placas {6}con todo respeto manifiesto a usted que presentó caducidad contra el comparendo No. {7} del  {8}. \nCordialmente.".format(fullname, document_type, document_id, NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal, placa_vehiculo, NoComparendoDelCaso, FechaDeComparendo)
            if document_type.startswith("Revocatoria"):
                description = "Buen día, \nYo, {0}, sociedad debidamente constituida e identificada con {1} No. {2}, representada por {3} quien se identifica con {4} {5} propietario del vehículo de placas {6} con todo respeto manifiesto a usted que presentó revocatoria directa contra la Resolución {7} del {8} \nCordialmente.".format(fullname, document_type, document_id, NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal, placa_vehiculo, NoResoluciónSancionatoria, FechaDeResoluciónSancionatoria)
            if document_type == "Prescripción":
                description = "Buenas tardes, \nYo, {0}, sociedad debidamente constituida e identificada con {1} No. {2}, representada por {3} quien se identifica con {4} {5} propietario del vehículo de placas {6} con todo respeto manifiesto a usted que presento prescripción contra de la Resolución {7} del {8}. \nCordialmente.".format(fullname, document_type, document_id, NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal, placa_vehiculo, NoResoluciónSancionatoria, FechaDeResoluciónSancionatoria)
        return description
    except:
        raise


def robot_status(api_status):
    try:
        if "data" not in api_status:
            return ""
        data = api_status["data"]
        
        if "status" not in data[0]:
            return ""
        status = data[0]["status"]

        return status
    except:
        raise