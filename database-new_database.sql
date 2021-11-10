-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.2
-- PostgreSQL version: 12.0
-- Project Site: pgmodeler.io
-- Model Author: ---


-- Database creation must be done outside a multicommand file.
-- These commands were put in this file only as a convenience.
-- -- object: new_database | type: DATABASE --
-- -- DROP DATABASE IF EXISTS new_database;
-- CREATE DATABASE new_database;
-- -- ddl-end --
-- 

-- object: public.caso | type: TABLE --
-- DROP TABLE IF EXISTS public.caso CASCADE;
CREATE TABLE public.caso (
	id integer NOT NULL,
	fecha_notificacion date NOT NULL,
	tipo_contagio varchar NOT NULL,
	estado varchar NOT NULL,
	recuperacion varchar,
	fecha_inicio_sintomas date NOT NULL,
	"Fecha_muerte" date,
	fecha_diagnostico date NOT NULL,
	fecha_recuperacion date,
	tipo_recuperacion varchar,
	fecha_reporte_web date NOT NULL,
	ubicacion_caso varchar NOT NULL,
	"Id_Paciente" integer,
	"ID_DIVAPOLA_municipio_Municipio" smallint,
	CONSTRAINT "Caso_pk" PRIMARY KEY (id)

);
-- ddl-end --
-- ALTER TABLE public.caso OWNER TO postgres;
-- ddl-end --

-- object: public."Paciente" | type: TABLE --
-- DROP TABLE IF EXISTS public."Paciente" CASCADE;
CREATE TABLE public."Paciente" (
	"Id" integer NOT NULL,
	"Edad" smallint NOT NULL,
	"Unidad_edad" smallint NOT NULL,
	"Sexo" char NOT NULL,
	"Codigo_ISO_pais_Nacionalidad" smallint,
	"Pertenencia_etnica_ID_Etnia" smallint,
	CONSTRAINT "Paciente_pk" PRIMARY KEY ("Id")

);
-- ddl-end --
-- ALTER TABLE public."Paciente" OWNER TO postgres;
-- ddl-end --

-- object: public."Nacionalidad" | type: TABLE --
-- DROP TABLE IF EXISTS public."Nacionalidad" CASCADE;
CREATE TABLE public."Nacionalidad" (
	"Codigo_ISO_pais" smallint NOT NULL,
	"Nombre" varchar,
	CONSTRAINT "Nacionalidad_pk" PRIMARY KEY ("Codigo_ISO_pais")

);
-- ddl-end --
-- ALTER TABLE public."Nacionalidad" OWNER TO postgres;
-- ddl-end --

-- object: public."Etnia" | type: TABLE --
-- DROP TABLE IF EXISTS public."Etnia" CASCADE;
CREATE TABLE public."Etnia" (
	"Pertenencia_etnica_ID" smallint NOT NULL,
	"Pertenencia_etnica" varchar,
	CONSTRAINT "Etnia_pk" PRIMARY KEY ("Pertenencia_etnica_ID")

);
-- ddl-end --
-- ALTER TABLE public."Etnia" OWNER TO postgres;
-- ddl-end --

-- object: public."Municipio" | type: TABLE --
-- DROP TABLE IF EXISTS public."Municipio" CASCADE;
CREATE TABLE public."Municipio" (
	"ID_DIVAPOLA_municipio" smallint NOT NULL,
	"Nombre" varchar NOT NULL,
	CONSTRAINT "Municipio_pk" PRIMARY KEY ("ID_DIVAPOLA_municipio")

);
-- ddl-end --
-- ALTER TABLE public."Municipio" OWNER TO postgres;
-- ddl-end --

-- object: "Paciente_fk" | type: CONSTRAINT --
-- ALTER TABLE public.caso DROP CONSTRAINT IF EXISTS "Paciente_fk" CASCADE;
ALTER TABLE public.caso ADD CONSTRAINT "Paciente_fk" FOREIGN KEY ("Id_Paciente")
REFERENCES public."Paciente" ("Id") MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "Nacionalidad_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Paciente" DROP CONSTRAINT IF EXISTS "Nacionalidad_fk" CASCADE;
ALTER TABLE public."Paciente" ADD CONSTRAINT "Nacionalidad_fk" FOREIGN KEY ("Codigo_ISO_pais_Nacionalidad")
REFERENCES public."Nacionalidad" ("Codigo_ISO_pais") MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "Etnia_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Paciente" DROP CONSTRAINT IF EXISTS "Etnia_fk" CASCADE;
ALTER TABLE public."Paciente" ADD CONSTRAINT "Etnia_fk" FOREIGN KEY ("Pertenencia_etnica_ID_Etnia")
REFERENCES public."Etnia" ("Pertenencia_etnica_ID") MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "Municipio_fk" | type: CONSTRAINT --
-- ALTER TABLE public.caso DROP CONSTRAINT IF EXISTS "Municipio_fk" CASCADE;
ALTER TABLE public.caso ADD CONSTRAINT "Municipio_fk" FOREIGN KEY ("ID_DIVAPOLA_municipio_Municipio")
REFERENCES public."Municipio" ("ID_DIVAPOLA_municipio") MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --


