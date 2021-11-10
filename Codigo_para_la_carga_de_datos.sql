SET datestyle = GERMAN, DMY;

copy caso(id, fecha_reporte_web, fecha_notificacion, tipo_contagio, ubicacion_caso, estado, recuperacion, fecha_inicio_sintomas, fecha_muerte, Fecha_diagnostico, fecha_recuperacion, tipo_recuperacion, id_paciente, id_divapola_municipio_Municipio)
from 'E:\AAAROSARIO\3 semestre\Ingenieria de datos\Proyecto\Segunda entrega/Casos_1.csv'
delimiter ','
csv header;

copy paciente(id, edad, unidad_edad, sexo, codigo_iso_pais_nacionalidad)
from 'E:\AAAROSARIO\3 semestre\Ingenieria de datos\Proyecto\Segunda entrega/Casos_2.csv'
delimiter ','
csv header;


INSERT INTO nacionalidad
VALUES (32,'argentina');

INSERT INTO nacionalidad
VALUES (36, 'australia');

INSERT INTO nacionalidad
VALUES (51, 'armenia');

INSERT INTO nacionalidad
VALUES (56, 'belgica');

INSERT INTO nacionalidad
VALUES (68, 'bolivia');

INSERT INTO nacionalidad
VALUES (76, 'brasil');

INSERT INTO nacionalidad
VALUES (120, 'camerun');

INSERT INTO nacionalidad
VALUES (124, 'canada');

INSERT INTO nacionalidad
VALUES (140, 'republica centro_africana');

INSERT INTO nacionalidad
VALUES (152, 'chile');

INSERT INTO nacionalidad
VALUES (156, 'china');

INSERT INTO nacionalidad
VALUES (188, 'costa rica');

INSERT INTO nacionalidad
VALUES (191, 'croacia');

INSERT INTO nacionalidad
VALUES (192, 'cuba');

INSERT INTO nacionalidad
VALUES (212, 'dominicana');

INSERT INTO nacionalidad
VALUES (214, 'republica dominicana');

INSERT INTO nacionalidad
VALUES (218, 'ecuador');

INSERT INTO nacionalidad
VALUES (222, 'el salvador');

INSERT INTO nacionalidad
VALUES (250, 'francia');

INSERT INTO nacionalidad
VALUES (276, 'alemania');

INSERT INTO nacionalidad
VALUES (308, 'granada');

INSERT INTO nacionalidad
VALUES (312, 'guadalupe');

INSERT INTO nacionalidad
VALUES (320, 'guatemala');

INSERT INTO nacionalidad
VALUES (340, 'honduras');

INSERT INTO nacionalidad
VALUES (360, 'indonesia');

INSERT INTO nacionalidad
VALUES (380, 'italia');

INSERT INTO nacionalidad
VALUES (388, 'jamaica');

INSERT INTO nacionalidad
VALUES (410, 'corea del sur');

INSERT INTO nacionalidad
VALUES (484, 'mexico');

INSERT INTO nacionalidad
VALUES (504, 'marruecos');

INSERT INTO nacionalidad
VALUES (528, 'paises bajos');

INSERT INTO nacionalidad
VALUES (530, 'antillas neerlandesas');

INSERT INTO nacionalidad
VALUES (533, 'aruba');

INSERT INTO nacionalidad
VALUES (558, 'nicaragua');

INSERT INTO nacionalidad
VALUES (566, 'nigeria');

INSERT INTO nacionalidad
VALUES (591, 'panama');

INSERT INTO nacionalidad
VALUES (600, 'paraguay');

INSERT INTO nacionalidad
VALUES (604, 'peru');

INSERT INTO nacionalidad
VALUES (620, 'portugal');

INSERT INTO nacionalidad
VALUES (630, 'puerto rico');

INSERT INTO nacionalidad
VALUES (634, 'qatar');

INSERT INTO nacionalidad
VALUES (654, 'santa helena');

INSERT INTO nacionalidad
VALUES (670, 'san vicente y las granadinas');

INSERT INTO nacionalidad
VALUES (682, 'arabia saudita');

INSERT INTO nacionalidad
VALUES (724, 'espana');

INSERT INTO nacionalidad
VALUES (752, 'suecia');

INSERT INTO nacionalidad
VALUES (792, 'turquia');

INSERT INTO nacionalidad
VALUES (826, 'reino unido de gran bretana e irlanda del norte');

INSERT INTO nacionalidad
VALUES (840, 'estados unidos de america');

INSERT INTO nacionalidad
VALUES (858, 'uruguay');

INSERT INTO nacionalidad
VALUES (862, 'venezuela');


copy municipio(id_divapola_municipio, nombre)
from 'E:\AAAROSARIO\3 semestre\Ingenieria de datos\Proyecto\Segunda entrega/Casos_4.csv'
delimiter ','
csv header;
