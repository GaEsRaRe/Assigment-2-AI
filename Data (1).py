A.add_rule("enfermedad", "depresion") #F33
A.add_rule("enfermedad", "esquizofrenia") #F20
A.add_rule("enfermedad", "toc") #F42
A.add_rule("enfermedad", "fobia_social") #F40.1
A.add_rule("enfermedad", "agorafobia") #F40.0
A.add_rule("enfermedad", "anorexia") #F50.0
A.add_rule("enfermedad", "cleptomania") #F63.2
A.add_rule("enfermedad", "ludopatia") #F63.0
A.add_rule("enfermedad", "postraumatico") #F43.1

#PARA AGREGAR PERSONAS, USAR ASSERT()


#DPRESION ----------

#Tipos
A.add_rule("episodio", "e_depresivo_leve")
A.add_rule("episodio", "e_depresivo_moderado")
A.add_rule("episodio", "e_depresivo_grave")

#Depresion A
A.add_rule("humor_depresivo_anormal", "depresion")
A.add_rule("perdida_de_interes", "depresion")
A.add_rule("disminucion_de_energia", "depresion")

#Depresion B
A.add_rule("perdida_de_confianza", "depresion")
A.add_rule("culpa_excesiva", "depresion")
A.add_rule("pensamientos_suicidas", "depresion")
A.add_rule("indecision", "depresion")
A.add_rule("agitacion_o_enlentecimiento", "depresion")
A.add_rule("alteracion_de_sueno", "depresion")
A.add_rule("cambio_apetito", "depresion")



#Esquizofrenia ----------
#Esquizofrenia1 (Por lo menos 1)
A.add_rule("alteracion_del_pensamiento", "esquizofrenia")
A.add_rule("ideas_delirantes", "esquizofrenia")
A.add_rule("voces_alucinatorias", "esquizofrenia")
A.add_rule("ideas_de_control", "esquizofrenia")
A.add_rule("ideas_de_poder", "esquizofrenia")

#Esquizofrenia2 (Almenos2)
A.add_rule("alucinaciones_persistenes", "esquizofrenia")
A.add_rule("discurso_incoherente", "esquizofrenia")
A.add_rule("conductas_catatonicas", "esquizofrenia") #Exitacion, mutismo, estupor
A.add_rule("sintomas_negativos", "esquizofrenia") #apatia, pobre discurso, incongruencia emocional

#Esquizofrenia No(Si es esto, no es ezquizofrenia)
#A.add_rule("intoxicacion", "!esquizofrenia")
#A.add_rule("dependencia_de_sustancias", "!esquizofrenia")

#TOc ----------
A.add_rule("obsesiones", "toc") #por al menos 2 semanas
# 0
A.add_rule("compulsiones", "toc") #por al menos 2 semanas
# Y
#TODAS las siguentes caracteristicas
A.add_rule("o_c_reiteradas_y_desagradables", "toc")
A.add_rule("intencion_de_resistencia", "toc")
A.add_rule("disgusto", "toc")

#Ninguna de las siguientes
#No puedes tener toc si tienes esquizofrenia


#Fobia Social ----------

#Cualquiera de las siguientes
A.add_rule("miedo_atencion", "fobia_social") #miedo a ser el centro de atencion
A.add_rule("miedo_humillacion", "fobia_social") #blah blah a la humillacion
A.add_rule("miedosocial", "fobia_social") #Miedo a situaciones sociales

#Al menos 2
A.add_rule("palpitaciones", "fobia_social")
A.add_rule("sudoracion", "fobia_social")
A.add_rule("temblores", "fobia_social")
A.add_rule("sequedad_boca", "fobia_social")
A.add_rule("dificultad_respiracion", "fobia_social")
A.add_rule("sensacion_ahogo", "fobia_social")
A.add_rule("dolor_pecho", "fobia_social")
A.add_rule("nauseas", "fobia_social")
A.add_rule("mareos", "fobia_social")
A.add_rule("miedo_muerte", "fobia_social")
A.add_rule("escalofrios", "fobia_social")
A.add_rule("hormigueo", "fobia_social")

# y
# 1 de los siguientes
A.add_rule("ruborizacion", "fobia_social")
A.add_rule("miedo_vomitar", "fobia_social")
A.add_rule("necesidad_orinar_o_defecar", "fobia_social")

#agorafobia
#Al menos 1
A.add_rule("palpitaciones", "agorafobia")
A.add_rule("sudoracion", "agorafobia")
A.add_rule("temblores", "agorafobia")
A.add_rule("sequedad_boca", "agorafobia")
A.add_rule("dificultad_respiracion", "agorafobia")
A.add_rule("sensacion_ahogo", "agorafobia")
A.add_rule("dolor_pecho", "agorafobia")
A.add_rule("nauseas", "agorafobia")
A.add_rule("mareos", "agorafobia")
A.add_rule("miedo_muerte", "agorafobia")
A.add_rule("escalofrios", "agorafobia")
A.add_rule("hormigueo", "agorafobia")

#Y
#OTRO Almenos2
A.add_rule("miedo_multitudes", "agorafobia")
A.add_rule("miedo_lugares_publicos", "agorafobia")
A.add_rule("miedo_viajar_solo", "agorafobia")
A.add_rule("miedo_viajar_lejos", "agorafobia")

#Y ninguno de los siguientes
    #A.add_rule("alucinaciones_persistentes", "!agorafobia")
    #A.add_rule("ideas_delirantes", "!agorafobia")
    #A.add_rule("tiene_esquizofrenia", "!agorafobia")
    #A.add_rule("tiene_toc", "!agorafobia")

#Anorexia
#Mas de la mitad
A.add_rule("bajo_peso", "anorexia") # 15% menos del
A.add_rule("autoinduccion_perdida_peso", "anorexia")
A.add_rule("distorcion_imagen_corporal", "anorexia")
A.add_rule("transtorno_endocrino", "anorexia")
A.add_rule("preocupacion_por_peso", "anorexia")
A.add_rule("preocupacion_por_imagen", "anorexia")

#Negativo
#A.add_rule("tiene_bulimia", "!anorexia")



#Cleptopmania 2 DE 3
A.add_rule("robos_sin_ganancia", "cleptomania")
A.add_rule("impulso_robar", "cleptomania")
A.add_rule("alivio_de_tension_al_robar", "cleptomania")

#ludopatia
A.add_rule("jugar_sin_provecho_economico", "ludopatia")
A.add_rule("repitencia_perjudicial", "ludopatia")
A.add_rule("impulso_de_jugar", "ludopatia")
A.add_rule("incapacidad_dejar_jugar", "ludopatia")
A.add_rule("preocupacion_por_juego", "ludopatia")

#PosTraumatico
#2 de Tres
A.add_rule("situacion_extrema_estres", "postraumatico")
A.add_rule("recuerdos_recurrentes_acontecimiento", "postraumatico")
A.add_rule("evitacion_similar_recuerdo", "postraumatico") #evita circunstacionas parecidas

#Alguno de los siguientes
A.add_rule("incapacidad_recordar_acontecimiento", "postraumatico")
A.add_rule("hipersensibilidad_psicologica", "postraumatico")
