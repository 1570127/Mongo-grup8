Client <collection>{
    "dni": <string>
    "nom": <string>
    "cognom": <string>
    "edat": <int>
    "genere": <string>
    "correu": <string>
    "poblacio": <string>
    "codi postal": <int>
    "adreça": <string>
}

Targeta <collection>{
    "numero": <int>
    "tipus": <string>
}

Cotxe <collection>{
    "matricula": <string>
    "marca": <string>
    "model": <string>
    "tipus": <string>
    "color": <string>
    "distintiu_ambiental": <string>
    "dni_client": <string>
}

Estada <collection>{
    "id_estada": <int>
    "porta_entrada": <int>
    "porta_sortida": <int>
    "data_hora_entrada": <DATE>
    "data_hora_sortida": <DATE>
    "matricula_cotxe": <string>
    "id_plaça": <int>
}

Parquing <collection>{
    "id_plaça": <int>
    "planta": <int>
    "zona": <int>
    "número": <int>
    "carregador": <boolean>
}

Tiquet <collection>{
    "id_tiquet": <int>
    "data": <DATE>
    "preu total": <float>
    "tipus pagament": <string>
    "dni_client": <string>
    "unitats": <int>
    "codi_producte": <int>
}

Producte <collection>{
    "codi": <int>
    "nom": <string>
    "fabricant": <string>
    "pes": <float>
    "categoria": <string>
    "preu": <float>
    "pack": [<int>] 
}
