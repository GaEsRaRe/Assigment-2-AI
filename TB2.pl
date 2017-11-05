enfermedad(depresion). %F33
enfermedad(esquizofrenia). %F20
enfermedad(toc). %F42
enfermedad(fobia_social). %F40.1
enfermedad(agorafobia). %F40.0
enfermedad(anorexia). %F50.0
enfermedad(bulimia). %F50.2
enfermedad(cleptomania). %F63.2
enfermedad(ludopatia). %F63.0
enfermedad(postraumatico). %F43.1


%PARA AGREGAR PERSONAS, USAR ASSERT()


%DPRESION ----------

%Tipos
episodio(e_depresivo_leve).
episodio(e_depresivo_moderado).
episodio(e_depresivo_grave).

%Depresion A
humor_depresivo_anormal(depresion).
perdida_de_interes(depresion).
disminucion_de_energia(depresion).

%Depresion B
perdida_de_confianza(depresion).
culpa_excesiva(depresion).
pensamientos_suicidas(depresion).
indecision(depresion).
agitacion_o_enlentecimiento(depresion).
alteracion_de_sueno(depresion).
cambio_apetito(depresion).

tipo_depresion_tipo(Variable):-
% 2 de A(por lo menos) y uno B(almenos) e_depresivo_leve
% 2 de A(por lo menos) y uno B(almenos) e_depresivo_moderado Todo suma mas de 6
% 3 de A y almenos 5 B(todo suma 8) e_depresivo_grave
  enfermedad(depresion)
  .

tiene_depresion(Variable):-
  %And
  (
  (humor_depresivo_anormal(Variable),perdida_de_interes(Variable));
  (humor_depresivo_anormal(Variable),disminucion_de_energia(Variable));
  (perdida_de_interes(Variable),disminucion_de_energia(Variable))
  ),
  (
  perdida_de_confianza(Variable);
  culpa_excesiva(Variable);
  pensamientos_suicidas(Variable);
  indecision(Variable);
  agitacion_o_enlentecimiento(Variable);
  alteracion_de_sueno(Variable);
  cambio_apetito(Variable)
  )
  .

% 2 de A(por lo menos) y uno B(almenos) e_depresivo_leve


%Esquizofrenia ----------

%Esquizofrenia1 (Por lo menos 1)
alteracion_del_pensamiento(esquizofrenia).
ideas_delirantes(esquizofrenia).
voces_alucinatorias(esquizofrenia).
ideas_de_control(esquizofrenia).
ideas_de_poder(esquizofrenia).

%Esquizofrenia2 (Almenos2)

alucinaciones_persistenes(esquizofrenia).
discurso_incoherente(esquizofrenia).
conductas_catatonicas(esquizofrenia). %Exitacion, mutismo, estupor
sintomas_negativos(esquizofrenia). %apatia, pobre discurso, incongruencia emocional

%Esquizofrenia No(Si es esto, no es ezquizofrenia)

intoxicacion(not(esquizofrenia)).
dependencia_de_sustancias(not(esquizofrenia)).


%TOc ----------

obsesiones(toc). %por al menos 2 semanas
%0
compulsiones(toc). %por al menos 2 semanas
% Y
%TODAS las siguentes caracteristicas
o_c_reiteradas_y_desagradables(toc).
intencion_de_resistencia(toc).
disgusto(toc).

%Ninguna de las siguientes
regla(enfermedad,sintoma)
%No puedes tener toc si tienes esquizofrenia

tiene_toc(Persona):-
  (obsesiones(Persona);
  compulsiones(Persona)),
  o_c_reiteradas_y_desagradables(Persona),
  intencion_de_resistencia(Persona),
  disgusto(Persona).

%Fobia Social ----------

%Cualquiera de las siguientes
miedo_atencion(fobia_social). %miedo a ser el centro de atencion
miedo_humillacion(fobia_social). %blah blah a la humillacion
miedosocial(fobia_social). %Miedo a situaciones sociales

%Al menos 1
palpitaciones(fobia_social).
sudoracion(fobia_social).
temblores(fobia_social).
sequedad_boca(fobia_social).
dificultad_respiracion(fobia_social).
sensacion_ahogo(fobia_social).
dolor_pecho(fobia_social).
nauseas(fobia_social).
mareos(fobia_social).
miedo_muerte(fobia_social).
escalofrios(fobia_social).
hormigueo(fobia_social).
%y
% 1 de los siguientes
ruborizacion(fobia_social).
miedo_vomitar(fobia_social).
necesidad_orinar_o_defecar(fobia_social).

tiene_fobia_social(Persona):-
  miedo_atencion(Persona);
  miedo_humillacion(Persona); %blah blah a la humillacion
  miedosocial(Persona). %Mm


%agorafobia


%Al menos 2
palpitaciones(agorafobia).
sudoracion(agorafobia).
temblores(agorafobia).
sequedad_boca(agorafobia).
dificultad_respiracion(agorafobia).
sensacion_ahogo(agorafobia).
dolor_pecho(agorafobia).
nauseas(agorafobia).
mareos(agorafobia).
miedo_muerte(agorafobia).
escalofrios(agorafobia).
hormigueo(agorafobia).
%Y
%OTRO Almenos2
miedo_multitudes(agorafobia).
miedo_lugares_publicos(agorafobia).
miedo_viajar_solo(agorafobia).
miedo_viajar_lejos(agorafobia).

%Y ninguno de los siguientes
alucinaciones_persistentes(not(agorafobia)).
ideas_delirantes(not(agorafobia)).
tiene_esquizofrenia(not(agorafobia)).
tiene_toc(not(agorafobia)).


%Anorexia
%Mas de la mitad
bajo_peso(anorexia). % 15% menos del
autoinduccion_perdida_peso(anorexia).
distorcion_imagen_corporal(anorexia).
transtorno_endocrino(anorexia).

preocupacion_por_peso(anorexia).
preocupacion_por_imagen(anorexia).

%Negativo
tiene_bulimia(not(anorexia)).

%bulimia
ingesta_excesiva_alimentos(bulimia).
preocupacion_por_peso(bulimia).
preocupacion_por_imagen(bulimia).
uso_de_purgantes(bulimia).
ansias_de_comer(bulimia).


%Negativo
tiene_anorexia(not(bulimia)).

%Cleptopmania

robos_sin_ganancia(cleptomania).
impulso_robar(cleptomania).
alivio_de_tension_al_robar(cleptomania).

%ludopatia
juego_en_un_ano(ludopatia).
jugar_sin_provecho_economico(ludopatia).
repitencia_perjudicial(ludopatia).
impulso_de_jugar(ludopatia).
incapacidad_dejar_jugar(ludopatia).
preocupacion_por_juego(ludopatia).


%PosTraumatico
%2 de Tres
situacion_extrema_estres(postraumatico).
recuerdos_recurrentes_acontecimiento(postraumatico).
evitacion_similar_recuerdo(postraumatico). %evita circunstacionas parecidas

%Alguno de los siguientes
incapacidad_recordar_acontecimiento(postraumatico).
hipersensibilidad_psicologica(postraumatico).
