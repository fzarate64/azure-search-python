import os

def azure_config():
    
    configs={}
    configs["search_facets"]= "authors*,language_code"
    configs["search_index_name"]=os.environ.get("SearchIndexName","good-books")
    configs["search_service_name"]=os.environ.get("SearchServiceName","servicio-busqueda")
    configs["search_api_key"]=os.environ.get("SearchApiKey","40410AD301192C5C71231411E593477D")
        
    return configs
