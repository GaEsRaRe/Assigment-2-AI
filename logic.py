# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:54:20 2017

@author: Gabriel PC
"""

##Core of logic
class Logic:
    rules = {}
    negations = {}

    def add_rule(self,rule,value):
        if rule in self.rules:
            self.rules[rule].append(value)
        else:
            self.rules[rule] = [value]
    def exist(self,rule,value):
        if rule in self.rules:
            return value in self.rules[rule]
        else:
            return False
    def get_rule(self,val):
        solutions = []
        for key, value in self.rules.items():
            if val in value:
                solutions.append(key)
        return solutions

    def add_negation(self,rule,value):
        if rule in self.negations:
            self.negations[rule].append(value)
        else:
            self.negations[rule] = [value]
    pass
    

#prolog to python

#Iniciamos un motor de inferencias
A = Logic()

#Enfermedades
A.add_rule("enfermedad","depresion") #Done
A.add_rule("enfermedad","esquizofrenia") #Done
A.add_rule("enfermedad","toc") #Done
A.add_rule("enfermedad","fobia_social") #Done
A.add_rule("enfermedad","agorafobia") #Done
A.add_rule("enfermedad","anorexia") #Done
A.add_rule("enfermedad","cleptomania") #Done
A.add_rule("enfermedad","ludopatia") #Done
A.add_rule("enfermedad","postraumatico") #Done

#2 de tres
A.add_rule("humor_depresivo_anormal","depresion")
A.add_rule("perdida_de_interes","depresion")
A.add_rule("disminucion_de_energia","depresion")

A.add_rule("perdida_de_confianza","depresion")
A.add_rule("culpa_excesiva","depresion")
A.add_rule("pensamientos_suicidas","depresion")
A.add_rule("indecision","depresion")
A.add_rule("agitacion_o_enlentecimiento","depresion")
A.add_rule("alteracion_de_sueno","depresion")
A.add_rule("cambio_apetito","depresion")

#Funcion para depresion
def tiene_depresion(value):        
    answer = (
            ((A.exist("humor_depresivo_anormal",value) and A.exist("perdida_de_interes",value)) or
            (A.exist("humor_depresivo_anormal",value) and A.exist("disminucion_de_energia",value)) or
            (A.exist("perdida_de_interes",value) and A.exist("disminucion_de_energia",value))) and
             (A.exist("perdida_de_confianza",value) or 
             A.exist("culpa_excesiva",value) or 
             A.exist("pensamientos_suicidas",value) or
             A.exist("indecision",value) or 
             A.exist("agitacion_o_enlentecimiento",value) or 
             A.exist("cambio_apetito",value)
                     )
    )
    return answer

#Reglas para Esquizofrenia

#Esquizofrenia1 (Por lo menos 1)
A.add_rule("alteracion_del_pensamiento","esquizofrenia")
A.add_rule("ideas_delirantes","esquizofrenia")
A.add_rule("ideas_de_control","esquizofrenia")
A.add_rule("ideas_de_poder","esquizofrenia")

# Esquizofrenia2 (Almenos2)
A.add_rule("alucinaciones_persistenes","esquizofrenia")
A.add_rule("discurso_incoherente","esquizofrenia")
A.add_rule("conductas_catatonicas","esquizofrenia") #Exitacion, mutismo, estupor
A.add_rule("sintomas_negativos","esquizofrenia") #apatia, pobre discurso, incongruencia emocional

#dependencia
A.add_negation("intoxicacion","esquizofrenia")
A.add_negation("dependencia_de_sustancias","esquizofrenia")

#Regla para esquizofrenia

def tiene_esquizofrenia(value):
    answer = ( # 
            (A.exist("alteracion_del_pensamiento",value) or A.exist("ideas_delirantes",value) or
             A.exist("voces_alucinatorias",value) or A.exist("ideas_de_control",value) or
             A.exist("ideas_de_poder",value) )
            and (
             (A.exist("alucinaciones_persistenes",value) and 
              (A.exist("discurso_incoherente",value) or A.exist("conductas_catatonicas",value) or A.exist("sintomas_negativos",value))) or
              (A.exist("discurso_incoherente",value) and 
              (A.exist("conductas_catatonicas",value) or A.exist("sintomas_negativos",value))) or
              (A.exist("conductas_catatonicas",value) and A.exist("sintomas_negativos",value))
                    )
              and
              not(A.exist("intoxicacion",value) or A.exist("dependencia_de_sustancias",value))
            )
    return answer


#Uno de los dos
A.add_rule("obsesiones","toc")
A.add_rule("compulsiones","toc")

#Todas
A.add_rule("o_c_reiteradas_y_desagradables","toc")
A.add_rule("intencion_de_resistencia","toc")
A.add_rule("disgusto","toc")

#ninguna

A.add_negation("esquizofrenia","toc")

def tiene_toc(value):
    answer = (
            (A.exist("obsesiones",value) or A.exist("obsesiones")) and
            A.exist("o_c_reiteradas_y_desagradables") and
            A.exist("intencion_de_resistencia") and
            A.exist("disgusto") 
            )
    return answer

#Cualquiera de las siguientes
A.add_rule("miedo_atencion", "fobia_social")
A.add_rule("miedo_humillacion", "fobia_social")
A.add_rule("miedo_social", "fobia_social")

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

A.add_rule("ruborizacion", "fobia_social")
A.add_rule("miedo_vomitar", "fobia_social")
A.add_rule("necesidad_orinar_o_defecar", "fobia_social")


def tiene_fobia_social(value):
    answer = (
            (A.exist("miedo_atencion",value)or A.exist("miedo_humillacion",value) or A.exist("miedo_social",value)) and
            (A.exist("palpitaciones",value)or A.exist("sudoracion",value) or A.exist("temblores",value) or
             A.exist("sequedad_boca",value)or A.exist("dificultad_respiracion",value) or A.exist("sensacion_ahogo",value) or
             A.exist("dolor_pecho",value)or A.exist("nauseas",value) or A.exist("mareos",value) or
             A.exist("miedo_muerte",value)or A.exist("escalofrios",value) or A.exist("hormigueo",value)) and
             (A.exist("ruborizacion",value)or A.exist("miedo_vomitar",value) or A.exist("necesidad_orinar_o_defecar",value))
            )
    return answer
    

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

#Al menos 2
A.add_rule("miedo_multitudes", "agorafobia")
A.add_rule("miedo_lugares_publicos", "agorafobia")
A.add_rule("miedo_viajar_solo", "agorafobia")
A.add_rule("miedo_viajar_lejos", "agorafobia")

A.add_negation("alucinaciones_persistentes", "agorafobia")
A.add_negation("ideas_delirantes", "agorafobia")
A.add_negation("tiene_esquizofrenia", "agorafobia")
A.add_negation("tiene_toc", "agorafobia")

def tiene_agorafobia(value):
    answer = (
             (A.exist("palpitaciones",value)or A.exist("sudoracion",value) or A.exist("temblores",value) or
             A.exist("sequedad_boca",value)or A.exist("dificultad_respiracion",value) or A.exist("sensacion_ahogo",value) or
             A.exist("dolor_pecho",value)or A.exist("nauseas",value) or A.exist("mareos",value) or
             A.exist("miedo_muerte",value)or A.exist("escalofrios",value) or A.exist("hormigueo",value)) and
              (
             (A.exist("miedo_multitudes",value) and 
              (A.exist("miedo_lugares_publicos",value) or A.exist("miedo_viajar_solo",value) or A.exist("miedo_viajar_lejos",value))) or
              (A.exist("miedo_lugares_publicos",value) and 
              (A.exist("miedo_viajar_solo",value) or A.exist("miedo_viajar_lejos",value))) or
              (A.exist("miedo_viajar_solo",value) and A.exist("miedo_viajar_lejos",value))
                    ) and 
              not(A.exist("alucinaciones_persistentes",value) or 
                  A.exist("ideas_delirantes",value) or 
                  A.exist("tiene_esquizofrenia",value) or 
                  A.exist("tiene_toc",value)
                      )
            )
    
    return answer

#Anorexia
#Mitad o mas
A.add_rule("bajo_peso", "anorexia") 
A.add_rule("autoinduccion_perdida_peso", "anorexia")
A.add_rule("distorcion_imagen_corporal", "anorexia")
A.add_rule("transtorno_endocrino", "anorexia")
A.add_rule("preocupacion_por_peso", "anorexia")
A.add_rule("preocupacion_por_imagen", "anorexia")

#A(C(B+D) + E(D+F)+ B(D(C+D)+EF)) + CE(D+F) + DEF
def tiene_anorexia(value):
    answer = (
            (A.exist("bajo_peso",value) and 
             ((A.exist("distorcion_imagen_corporal",value) and(A.exist("autoinduccion_perdida_peso",value) or A.exist("transtorno_endocrino",value))) or 
              (A.exist("preocupacion_por_peso",value) and(A.exist("transtorno_endocrino",value) or A.exist("preocupacion_por_imagen",value))))) or
              (A.exist("autoinduccion_perdida_peso",value) and 
             ((A.exist("transtorno_endocrino",value) and(A.exist("distorcion_imagen_corporal",value) or A.exist("preocupacion_por_peso",value)))) or 
              (A.exist("preocupacion_por_peso",value) and(A.exist("preocupacion_por_imagen",value)))) or
              (A.exist("transtorno_endocrino",value) or A.exist("preocupacion_por_peso",value) or A.exist("preocupacion_por_imagen",value))
             
            )
    return answer

#Cleptopmania
#2 de 3
A.add_rule("robos_sin_ganancia", "cleptomania")
A.add_rule("impulso_robar", "cleptomania")
A.add_rule("alivio_de_tension_al_robar", "cleptomania")

def tiene_cleptomania(value):
    answer = ((A.exist("robos_sin_ganancia",value) and A.exist("impulso_robar",value)) or
            (A.exist("robos_sin_ganancia",value) and A.exist("alivio_de_tension_al_robar",value)) or
            (A.exist("impulso_robar",value) and A.exist("alivio_de_tension_al_robar",value)))
    return answer


#ludopatia
A.add_rule("jugar_sin_provecho_economico", "ludopatia")
A.add_rule("repitencia_perjudicial", "ludopatia")
A.add_rule("impulso_de_jugar", "ludopatia")
A.add_rule("incapacidad_dejar_jugar", "ludopatia")
A.add_rule("preocupacion_por_juego", "ludopatia")

#A(C(B+D)+DE) + BD(C+E) + CDE
def tiene_ludopatia(value):
    answer = (
            (A.exist("jugar_sin_provecho_economico",value) and 
             ((A.exist("impulso_de_jugar",value) and(A.exist("repitencia_perjudicial",value) or A.exist("incapacidad_dejar_jugar",value))) or 
              (A.exist("incapacidad_dejar_jugar",value) and A.exist("preocupacion_por_juego",value)))) or
             ((A.exist("repitencia_perjudicial",value) and A.exist("incapacidad_dejar_jugar",value)) and (A.exist("impulso_de_jugar",value) and A.exist("preocupacion_por_juego",value))
             ) or
             (A.exist("impulso_de_jugar",value) and A.exist("incapacidad_dejar_jugar",value) and A.exist("preocupacion_por_juego",value))
            )
    
    return answer

#PosTraumatico
#2 de Tres
A.add_rule("situacion_extrema_estres", "postraumatico")
A.add_rule("recuerdos_recurrentes_acontecimiento", "postraumatico")
A.add_rule("evitacion_similar_recuerdo", "postraumatico") #evita circunstacionas parecidas

#Alguno de los siguientes
A.add_rule("incapacidad_recordar_acontecimiento", "postraumatico")
A.add_rule("hipersensibilidad_psicologica", "postraumatico")

def tiene_pos_traumatico(value):
    answer = (
            ((A.exist("situacion_extrema_estres",value) and A.exist("recuerdos_recurrentes_acontecimiento",value)) or
            (A.exist("situacion_extrema_estres",value) and A.exist("evitacion_similar_recuerdo",value)) or
            (A.exist("recuerdos_recurrentes_acontecimiento",value) and A.exist("evitacion_similar_recuerdo",value))) and
             (A.exist("hipersensibilidad_psicologica",value) or A.exist("incapacidad_recordar_acontecimiento",value))           
                )
    return answer


