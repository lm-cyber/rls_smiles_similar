




def parser_data(data)->dict:

    __mapping__ ={
        "name_ru": "Русское название",
        "name_en": "Английское название",
        "name_lat": "Латинское название",
        "name_chem": "Химическое название",
        "brutto_formula": "Брутто формула",
        "name_farm_group": "Фармакологическая группа",
        "cas": "Код CAS",
        "farm_action": {"name":"Фармакологическое действие","action":"start_with"},
        "description": "Характеристика",
        "farmacy":"Фармакология",
        "use": {"name":"Применение вещества","action":"start_with"},
        "contraindication": "Противопоказания",
        "restrictions":"Ограничения к применению",
        "side_effects": {"name":"Побочные действия вещества","action":"start_with"},
        "method_of_administration_and_dosage": "Способ применения и дозы",

    }
    def get_row_element(text,id,key):
        key_value = __mapping__[key]
        if isinstance(key_value,dict):
            if text[id].startswith(key_value["name"]):
                return {key:text[id+1]}
        else:
            if text[id] == key_value:
                return {key:text[id+1]}
        return None

    text = data.text.split("\n")
    index = text.index("Русское название", text.index("Русское название") + 1)
    values = {}
    for i in range(index, len(text)-1):
        for key in __mapping__.keys():
            value = get_row_element(text,i,key)
            if value:
                values.update(value)
        if len(values) == len(__mapping__):
            break
    return values