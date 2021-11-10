def casosPorMunicipio():
    return """select count(c.id) as num_casos, m.nombre as nombre_municipio
              from caso c join municipio m on (c.id_divapola_municipio_municipio = m.id_divapola_municipio)
              group by nombre_municipio
              order by num_casos asc"""

def CasosDeMuejeresMayoresDe80anos():
    return """select c.id as caso_id, p.id as paciente_id, c.fecha_inicio_sintomas as inicio_sintomas, c.tipo_contagio as tipo_contagio, c.estado as estado, p.edad as edad, p.sexo as sexo
              from caso c join paciente p on (c.id_paciente = p.id)
              where sexo = 'F' and edad > 80"""
              
def ExtranjerosFallecidos():
    return """select na.nombre as pais_nomrbe, pa.id as paciente_id, ca.fecha_notificacion as fecha_notificacion, ca.fecha_muerte as fecha_muerte, mu.nombre as municipio
              from Nacionalidad na join Paciente pa on (na.codigo_iso_pais = pa.codigo_iso_pais_nacionalidad)
		                           join caso ca on (pa.Id = ca.id_paciente)
		                           join Municipio mu on (ca.id_divapola_municipio_municipio = mu.id_divapola_municipio)
             where ca.Fecha_muerte is not null and na.Nombre is not null
             order by ca.Fecha_muerte asc"""
             
def ExtrangerosPorMunicipio():
    return """select count(c.id) as num_casos, n.nombre as nacionalidad, m.nombre as nombre_municipio
              from municipio m join caso c on (c.id_divapola_municipio_municipio = m.id_divapola_municipio)
			                   join paciente p on (c.id_paciente = p.id) 
                               join nacionalidad n on (n.codigo_iso_pais = p.codigo_iso_pais_nacionalidad)			
             where n.nombre is not null 
             group by cube(nacionalidad, nombre_municipio)
             order by nacionalidad asc"""
