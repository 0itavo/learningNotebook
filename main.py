
def verificar_qtplacas_string_baseVoc(Voc_max,Voc_placas,Tmin,Tstc,STC):
    Voc_placas_real = Voc_placas + Voc_placas*(Tmin-Tstc)*STC
    n_max_placas = Voc_max/Voc_placas_real
    n_max_placas = round(n_max_placas)
    return n_max_placas

