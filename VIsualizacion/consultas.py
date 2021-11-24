
def casosPorMunicipio():
    return """select count(c.id) as num_casos, m.nombre as nombre_municipio
              from caso c join municipio m on (c.id_divapola_municipio_municipio = m.id_divapola_municipio)
              group by nombre_municipio
              order by num_casos desc"""

def EdadPromedioDeMuertos():
    return """select m.nombre as nombre_municipio, round(avg(p.edad),1) as promedio_edad
              from paciente p  join caso c on (p.id = id_paciente) 
			                   join municipio m on (m.id_divapola_municipio = c.id_divapola_municipio_municipio)
              where c.fecha_muerte is not null 
              group by m.nombre
              order by promedio_edad desc"""
              
def CasosTTotalesYMuertesPorMunicipio():
    return """with muertes as(
            	select m.nombre as nombre_municipio, count(c.id) as num_muertes
	            from paciente p  join caso c on (p.id = id_paciente) 
			     	             join municipio m on (m.id_divapola_municipio = c.id_divapola_municipio_municipio)
	           where c.fecha_muerte is not null 
	           group by m.nombre
	           order by num_muertes desc),
	
	           casos as(
	           select m.nombre as nom_mun, count(c.id) as num_casos
	           from paciente p  join caso c on (p.id = id_paciente) 
			                    join municipio m on (m.id_divapola_municipio = c.id_divapola_municipio_municipio)
	           group by m.nombre)
	
	           select nombre_municipio, num_muertes, num_casos
	           from muertes join casos on (nombre_municipio = nom_mun)
	           order by num_muertes desc"""
              
              
def origenCaso():
    return """with Importado as (
            select count(cs.id) as num_imports, mun.nombre as nom_mun
            from caso cs right join municipio mun on (cs.id_divapola_municipio_municipio = mun.id_divapola_municipio)
            where cs.tipo_contagio = 'Importado'
            group by mun.nombre ), 
        Relacionado as (
                select count(cs.id) as num_rela, mun.nombre as nom_municipio
                 from caso cs right join municipio mun on (cs.id_divapola_municipio_municipio = mun.id_divapola_municipio)
                where cs.tipo_contagio = 'Relacionado'
                group by mun.nombre),
        Comunitaria as (
                select count(cs.id) as num_com, mun.nombre as nom_munic
                from caso cs right join municipio mun on (cs.id_divapola_municipio_municipio = mun.id_divapola_municipio)
                where cs.tipo_contagio = 'Comunitaria'
                group by mun.nombre),
        Estudio as (
                select count(cs.id) as num_std, mun.nombre as nom_muni
                from caso cs right join municipio mun on (cs.id_divapola_municipio_municipio = mun.id_divapola_municipio)
                where cs.tipo_contagio = 'En estudio'
                group by mun.nombre)

        select imp.num_imports as numero_imports, rela.num_rela as numero_rela, comu.num_com as numero_com, std.num_std as nuemro_std, nom_municipio 
        from Importado imp right join Relacionado rela on (imp.nom_mun = rela.nom_municipio)
                                 join comunitaria comu on (rela.nom_municipio = comu.nom_munic)
                                 join Estudio std on (comu.nom_munic = std.nom_muni)"""
                                 
def casosPorDia2020():
    return """select count(cs.id) as num_casos, cs.fecha_inicio_sintomas as fecha
                  from caso cs 
                  where fecha_inicio_sintomas <= '2020-12-31' and fecha_inicio_sintomas > '2020-01-01'
                  group by fecha 
                  order by fecha asc"""          

def casosPorDia2021():
        return """select count(cs.id) as num_casos, cs.fecha_inicio_sintomas as fecha
                  from caso cs 
                  where fecha_inicio_sintomas <= '2021-12-31' and fecha_inicio_sintomas > '2020-12-31'
                  group by fecha 
                  order by fecha asc"""   

def tasaRecuperadosPorGenero():
    return """select count(cs.id) as tasa, pt.sexo as genero
            from caso cs join paciente pt on (cs.id_paciente = pt.id)
            where cs.recuperacion = 'Recuperado'
            group by pt.sexo """                   