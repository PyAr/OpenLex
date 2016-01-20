--
-- PostgreSQL database dump
--

-- Dumped from database version 9.4.4
-- Dumped by pg_dump version 9.4.4
-- Started on 2015-07-19 20:59:22 GFT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 193 (class 3079 OID 11895)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2175 (class 0 OID 0)
-- Dependencies: 193
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 177 (class 1259 OID 16669)
-- Name: Abogado; Type: TABLE; Schema: public; Owner: mavignau; Tablespace: 
--

CREATE TABLE "Abogado" (
    "CUILCUIT" bigint NOT NULL,
    "Matricula" character varying(64) NOT NULL,
    "DomicilioLegal" character varying(512)
);


ALTER TABLE "Abogado" OWNER TO mavignau;

--
-- TOC entry 191 (class 1259 OID 16796)
-- Name: Agenda; Type: TABLE; Schema: public; Owner: mavignau; Tablespace: 
--

CREATE TABLE "Agenda" (
    "idCarpeta" integer NOT NULL,
    "idExpediente" integer NOT NULL,
    "fCreado" timestamp without time zone NOT NULL,
    "Titulo" character varying(1024),
    "Creador" integer,
    "fPrevisto" timestamp without time zone,
    "fCumplido" timestamp without time zone,
    "Prioridad" smallint,
    "Estado" character varying(64),
    "Archivo" bytea,
    "idTipoArchivo" integer
);


ALTER TABLE "Agenda" OWNER TO mavignau;

--
-- TOC entry 185 (class 1259 OID 16719)
-- Name: Carpeta; Type: TABLE; Schema: public; Owner: mavignau; Tablespace: 
--

CREATE TABLE "Carpeta" (
    "idCarpeta" integer NOT NULL,
    "Titulo" character varying(1024),
    "fInicio" timestamp without time zone,
    "fFin" timestamp without time zone,
    "Responsable" integer,
    "idCarpetaPadre" integer
);


ALTER TABLE "Carpeta" OWNER TO mavignau;

--
-- TOC entry 184 (class 1259 OID 16717)
-- Name: Carpeta_idCarpeta_seq; Type: SEQUENCE; Schema: public; Owner: mavignau
--

CREATE SEQUENCE "Carpeta_idCarpeta_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Carpeta_idCarpeta_seq" OWNER TO mavignau;

--
-- TOC entry 2176 (class 0 OID 0)
-- Dependencies: 184
-- Name: Carpeta_idCarpeta_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mavignau
--

ALTER SEQUENCE "Carpeta_idCarpeta_seq" OWNED BY "Carpeta"."idCarpeta";


--
-- TOC entry 187 (class 1259 OID 16741)
-- Name: Expediente; Type: TABLE; Schema: public; Owner: mavignau; Tablespace: 
--

CREATE TABLE "Expediente" (
    "idExpediente" integer NOT NULL,
    "idCarpeta" integer NOT NULL,
    "Caratula" character varying(1024),
    "NroExpediente" character varying(64),
    "idTipoProceso" integer,
    "idJuzgado" integer,
    "fInicio" timestamp without time zone,
    "fFin" timestamp without time zone
);


ALTER TABLE "Expediente" OWNER TO mavignau;

--
-- TOC entry 186 (class 1259 OID 16739)
-- Name: Expediente_idExpediente_seq; Type: SEQUENCE; Schema: public; Owner: mavignau
--

CREATE SEQUENCE "Expediente_idExpediente_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Expediente_idExpediente_seq" OWNER TO mavignau;

--
-- TOC entry 2177 (class 0 OID 0)
-- Dependencies: 186
-- Name: Expediente_idExpediente_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mavignau
--

ALTER SEQUENCE "Expediente_idExpediente_seq" OWNED BY "Expediente"."idExpediente";


--
-- TOC entry 179 (class 1259 OID 16684)
-- Name: Fuero; Type: TABLE; Schema: public; Owner: mavignau; Tablespace: 
--

CREATE TABLE "Fuero" (
    "idFuero" integer NOT NULL,
    "Descripcion" character varying(256)
);


ALTER TABLE "Fuero" OWNER TO mavignau;

--
-- TOC entry 178 (class 1259 OID 16682)
-- Name: Fuero_idFuero_seq; Type: SEQUENCE; Schema: public; Owner: mavignau
--

CREATE SEQUENCE "Fuero_idFuero_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Fuero_idFuero_seq" OWNER TO mavignau;

--
-- TOC entry 2178 (class 0 OID 0)
-- Dependencies: 178
-- Name: Fuero_idFuero_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mavignau
--

ALTER SEQUENCE "Fuero_idFuero_seq" OWNED BY "Fuero"."idFuero";


--
-- TOC entry 173 (class 1259 OID 16642)
-- Name: GrupoOperador; Type: TABLE; Schema: public; Owner: mavignau; Tablespace: 
--

CREATE TABLE "GrupoOperador" (
    "idGrupo" integer NOT NULL,
    "Descripcion" character varying(256)
);


ALTER TABLE "GrupoOperador" OWNER TO mavignau;

--
-- TOC entry 172 (class 1259 OID 16640)
-- Name: GrupoOperador_idGrupo_seq; Type: SEQUENCE; Schema: public; Owner: mavignau
--

CREATE SEQUENCE "GrupoOperador_idGrupo_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "GrupoOperador_idGrupo_seq" OWNER TO mavignau;

--
-- TOC entry 2179 (class 0 OID 0)
-- Dependencies: 172
-- Name: GrupoOperador_idGrupo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mavignau
--

ALTER SEQUENCE "GrupoOperador_idGrupo_seq" OWNED BY "GrupoOperador"."idGrupo";


--
-- TOC entry 181 (class 1259 OID 16692)
-- Name: Juzgado; Type: TABLE; Schema: public; Owner: mavignau; Tablespace: 
--

CREATE TABLE "Juzgado" (
    "idJuzgado" integer NOT NULL,
    "Nombre" character varying(512),
    "Instancia" character varying(64),
    "Domicilio" character varying(512),
    "idFuero" integer
);


ALTER TABLE "Juzgado" OWNER TO mavignau;

--
-- TOC entry 180 (class 1259 OID 16690)
-- Name: Juzgado_idJuzgado_seq; Type: SEQUENCE; Schema: public; Owner: mavignau
--

CREATE SEQUENCE "Juzgado_idJuzgado_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Juzgado_idJuzgado_seq" OWNER TO mavignau;

--
-- TOC entry 2180 (class 0 OID 0)
-- Dependencies: 180
-- Name: Juzgado_idJuzgado_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mavignau
--

ALTER SEQUENCE "Juzgado_idJuzgado_seq" OWNED BY "Juzgado"."idJuzgado";


--
-- TOC entry 188 (class 1259 OID 16765)
-- Name: Movimiento; Type: TABLE; Schema: public; Owner: mavignau; Tablespace: 
--

CREATE TABLE "Movimiento" (
    "idCarpeta" integer NOT NULL,
    "idExpediente" integer NOT NULL,
    "fCreado" timestamp without time zone NOT NULL,
    "Creador" integer,
    "Titulo" character varying(1024),
    "Estado" character varying(32),
    "Orden" integer,
    "Archivo" bytea,
    "idTipoArchivo" integer
);


ALTER TABLE "Movimiento" OWNER TO mavignau;

--
-- TOC entry 175 (class 1259 OID 16650)
-- Name: Operador; Type: TABLE; Schema: public; Owner: mavignau; Tablespace: 
--

CREATE TABLE "Operador" (
    "idOperador" integer NOT NULL,
    "CUITCUIL" bigint,
    "idGrupo" integer,
    "fCreacion" timestamp without time zone,
    "fFin" timestamp without time zone,
    "Clave" character varying(64)
);


ALTER TABLE "Operador" OWNER TO mavignau;

--
-- TOC entry 174 (class 1259 OID 16648)
-- Name: Operador_idOperador_seq; Type: SEQUENCE; Schema: public; Owner: mavignau
--

CREATE SEQUENCE "Operador_idOperador_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Operador_idOperador_seq" OWNER TO mavignau;

--
-- TOC entry 2181 (class 0 OID 0)
-- Dependencies: 174
-- Name: Operador_idOperador_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mavignau
--

ALTER SEQUENCE "Operador_idOperador_seq" OWNED BY "Operador"."idOperador";


--
-- TOC entry 192 (class 1259 OID 16814)
-- Name: Parte; Type: TABLE; Schema: public; Owner: mavignau; Tablespace: 
--

CREATE TABLE "Parte" (
    "CUILCUIT" bigint NOT NULL,
    "idCarpeta" integer NOT NULL,
    "idExpediente" integer NOT NULL,
    "Caracter" character varying(64),
    "Representado" bigint
);


ALTER TABLE "Parte" OWNER TO mavignau;

--
-- TOC entry 176 (class 1259 OID 16661)
-- Name: Persona; Type: TABLE; Schema: public; Owner: mavignau; Tablespace: 
--

CREATE TABLE "Persona" (
    "CUILCUIT" bigint NOT NULL,
    "Apellido" character varying(512),
    "Nombre" character varying(256),
    "Sexo" character(1),
    "Domicilio" character varying(512),
    "EMail" character varying(512),
    "Observaciones" text,
    "Telefono" character varying(256),
    "Celular" character varying(256)
);


ALTER TABLE "Persona" OWNER TO mavignau;

--
-- TOC entry 190 (class 1259 OID 16780)
-- Name: TipoArchivo; Type: TABLE; Schema: public; Owner: mavignau; Tablespace: 
--

CREATE TABLE "TipoArchivo" (
    "idTipoArchivo" integer NOT NULL,
    "Descripcion" character varying(512)
);


ALTER TABLE "TipoArchivo" OWNER TO mavignau;

--
-- TOC entry 189 (class 1259 OID 16778)
-- Name: TipoArchivo_idTipoArchivo_seq; Type: SEQUENCE; Schema: public; Owner: mavignau
--

CREATE SEQUENCE "TipoArchivo_idTipoArchivo_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "TipoArchivo_idTipoArchivo_seq" OWNER TO mavignau;

--
-- TOC entry 2182 (class 0 OID 0)
-- Dependencies: 189
-- Name: TipoArchivo_idTipoArchivo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mavignau
--

ALTER SEQUENCE "TipoArchivo_idTipoArchivo_seq" OWNED BY "TipoArchivo"."idTipoArchivo";


--
-- TOC entry 183 (class 1259 OID 16708)
-- Name: TipoProceso; Type: TABLE; Schema: public; Owner: mavignau; Tablespace: 
--

CREATE TABLE "TipoProceso" (
    "idTipoProceso" integer NOT NULL,
    "Descripcion" character varying(1024)
);


ALTER TABLE "TipoProceso" OWNER TO mavignau;

--
-- TOC entry 182 (class 1259 OID 16706)
-- Name: TipoProceso_idTipoProceso_seq; Type: SEQUENCE; Schema: public; Owner: mavignau
--

CREATE SEQUENCE "TipoProceso_idTipoProceso_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "TipoProceso_idTipoProceso_seq" OWNER TO mavignau;

--
-- TOC entry 2183 (class 0 OID 0)
-- Dependencies: 182
-- Name: TipoProceso_idTipoProceso_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mavignau
--

ALTER SEQUENCE "TipoProceso_idTipoProceso_seq" OWNED BY "TipoProceso"."idTipoProceso";


--
-- TOC entry 1995 (class 2604 OID 16722)
-- Name: idCarpeta; Type: DEFAULT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Carpeta" ALTER COLUMN "idCarpeta" SET DEFAULT nextval('"Carpeta_idCarpeta_seq"'::regclass);


--
-- TOC entry 1996 (class 2604 OID 16744)
-- Name: idExpediente; Type: DEFAULT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Expediente" ALTER COLUMN "idExpediente" SET DEFAULT nextval('"Expediente_idExpediente_seq"'::regclass);


--
-- TOC entry 1992 (class 2604 OID 16687)
-- Name: idFuero; Type: DEFAULT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Fuero" ALTER COLUMN "idFuero" SET DEFAULT nextval('"Fuero_idFuero_seq"'::regclass);


--
-- TOC entry 1990 (class 2604 OID 16645)
-- Name: idGrupo; Type: DEFAULT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "GrupoOperador" ALTER COLUMN "idGrupo" SET DEFAULT nextval('"GrupoOperador_idGrupo_seq"'::regclass);


--
-- TOC entry 1993 (class 2604 OID 16695)
-- Name: idJuzgado; Type: DEFAULT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Juzgado" ALTER COLUMN "idJuzgado" SET DEFAULT nextval('"Juzgado_idJuzgado_seq"'::regclass);


--
-- TOC entry 1991 (class 2604 OID 16653)
-- Name: idOperador; Type: DEFAULT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Operador" ALTER COLUMN "idOperador" SET DEFAULT nextval('"Operador_idOperador_seq"'::regclass);


--
-- TOC entry 1997 (class 2604 OID 16783)
-- Name: idTipoArchivo; Type: DEFAULT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "TipoArchivo" ALTER COLUMN "idTipoArchivo" SET DEFAULT nextval('"TipoArchivo_idTipoArchivo_seq"'::regclass);


--
-- TOC entry 1994 (class 2604 OID 16711)
-- Name: idTipoProceso; Type: DEFAULT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "TipoProceso" ALTER COLUMN "idTipoProceso" SET DEFAULT nextval('"TipoProceso_idTipoProceso_seq"'::regclass);


--
-- TOC entry 2152 (class 0 OID 16669)
-- Dependencies: 177
-- Data for Name: Abogado; Type: TABLE DATA; Schema: public; Owner: mavignau
--

COPY "Abogado" ("CUILCUIT", "Matricula", "DomicilioLegal") FROM stdin;
\.


--
-- TOC entry 2166 (class 0 OID 16796)
-- Dependencies: 191
-- Data for Name: Agenda; Type: TABLE DATA; Schema: public; Owner: mavignau
--

COPY "Agenda" ("idCarpeta", "idExpediente", "fCreado", "Titulo", "Creador", "fPrevisto", "fCumplido", "Prioridad", "Estado", "Archivo", "idTipoArchivo") FROM stdin;
1	1	2015-06-10 10:15:00	PPreparar avocamiento	1	\N	\N	1	pendiente	\N	\N
1	2	2015-06-20 08:45:00	Tomar Testimonial	1	2015-08-20 10:11:00	\N	1	pendiente	\N	\N
1	1	2015-05-10 09:00:00	Tomar testimonial de Gomez Teresa	1	2015-05-20 10:00:00	2015-05-02 10:15:00	1	cumplido	\N	\N
1	2	2015-06-21 09:00:00	Solicitar testimonio a comisaría	1	\N	\N	1	pendiente	\N	\N
1	2	2015-06-27 10:00:00	Realizar notificaciones	1	2015-07-18 09:00:00	\N	2	pendiente	\N	\N
1	2	2015-06-30 10:05:00	Ordenar documental	1	\N	\N	3	pendiente	\N	\N
\.


--
-- TOC entry 2160 (class 0 OID 16719)
-- Dependencies: 185
-- Data for Name: Carpeta; Type: TABLE DATA; Schema: public; Owner: mavignau
--

COPY "Carpeta" ("idCarpeta", "Titulo", "fInicio", "fFin", "Responsable", "idCarpetaPadre") FROM stdin;
1	Gomez Teresa s/Denuncias	\N	\N	1	\N
3	Juarez Inés 	\N	\N	2	\N
2	Fernandez Manuel 	\N	\N	2	\N
\.


--
-- TOC entry 2184 (class 0 OID 0)
-- Dependencies: 184
-- Name: Carpeta_idCarpeta_seq; Type: SEQUENCE SET; Schema: public; Owner: mavignau
--

SELECT pg_catalog.setval('"Carpeta_idCarpeta_seq"', 3, true);


--
-- TOC entry 2162 (class 0 OID 16741)
-- Dependencies: 187
-- Data for Name: Expediente; Type: TABLE DATA; Schema: public; Owner: mavignau
--

COPY "Expediente" ("idExpediente", "idCarpeta", "Caratula", "NroExpediente", "idTipoProceso", "idJuzgado", "fInicio", "fFin") FROM stdin;
1	1	Gomez Teresa s/Lesiones	78/2015	6	4	\N	\N
2	1	Gomez Teresa s/Desobediencia Judicial	45000/2015	6	4	\N	\N
4	2	Fernandez Manuel s/ Juicio Ejecutivo	8999/2015	1	1	\N	\N
5	3	Juarez Inés s/ Sucesorio	654/2013	2	2	\N	\N
\.


--
-- TOC entry 2185 (class 0 OID 0)
-- Dependencies: 186
-- Name: Expediente_idExpediente_seq; Type: SEQUENCE SET; Schema: public; Owner: mavignau
--

SELECT pg_catalog.setval('"Expediente_idExpediente_seq"', 5, true);


--
-- TOC entry 2154 (class 0 OID 16684)
-- Dependencies: 179
-- Data for Name: Fuero; Type: TABLE DATA; Schema: public; Owner: mavignau
--

COPY "Fuero" ("idFuero", "Descripcion") FROM stdin;
2	Civil y Comercial
4	Menor y Familia
3	Laboral
1	Penal
\.


--
-- TOC entry 2186 (class 0 OID 0)
-- Dependencies: 178
-- Name: Fuero_idFuero_seq; Type: SEQUENCE SET; Schema: public; Owner: mavignau
--

SELECT pg_catalog.setval('"Fuero_idFuero_seq"', 13, true);


--
-- TOC entry 2148 (class 0 OID 16642)
-- Dependencies: 173
-- Data for Name: GrupoOperador; Type: TABLE DATA; Schema: public; Owner: mavignau
--

COPY "GrupoOperador" ("idGrupo", "Descripcion") FROM stdin;
1	Jefe de Mesa de Entradas
2	Proveyente
3	Prosecretario
4	Juez
\.


--
-- TOC entry 2187 (class 0 OID 0)
-- Dependencies: 172
-- Name: GrupoOperador_idGrupo_seq; Type: SEQUENCE SET; Schema: public; Owner: mavignau
--

SELECT pg_catalog.setval('"GrupoOperador_idGrupo_seq"', 5, true);


--
-- TOC entry 2156 (class 0 OID 16692)
-- Dependencies: 181
-- Data for Name: Juzgado; Type: TABLE DATA; Schema: public; Owner: mavignau
--

COPY "Juzgado" ("idJuzgado", "Nombre", "Instancia", "Domicilio", "idFuero") FROM stdin;
1	Juzgado Civil y Comercial Nº 1	1º instancia	calle Imaginaria 34	2
2	Juzgado Civil y Comercial Nº 2	1º instancia	calle Imaginaria 34 1º piso	2
3	Juzgado Civil y Comercial Nº 3	1º instancia	calle Imaginaria 34 2º piso	2
4	Juzgado de Instrucción Nº1	1º instancia	calle Otra 3289	1
5	Juzgado de Instrucción Nº 2	1º instancia	calle del Recuerdo 5456	1
6	Cámara Civil y Comercial 	2º instancia	calle Principal 327	2
10	Cámara Penal - Sala 1	2º instancia	calle Principal 337	1
\.


--
-- TOC entry 2188 (class 0 OID 0)
-- Dependencies: 180
-- Name: Juzgado_idJuzgado_seq; Type: SEQUENCE SET; Schema: public; Owner: mavignau
--

SELECT pg_catalog.setval('"Juzgado_idJuzgado_seq"', 10, true);


--
-- TOC entry 2163 (class 0 OID 16765)
-- Dependencies: 188
-- Data for Name: Movimiento; Type: TABLE DATA; Schema: public; Owner: mavignau
--

COPY "Movimiento" ("idCarpeta", "idExpediente", "fCreado", "Creador", "Titulo", "Estado", "Orden", "Archivo", "idTipoArchivo") FROM stdin;
1	1	2015-07-18 16:37:00	1	Caratula expediente	procesal	\N	\N	\N
1	2	2015-07-18 16:37:01	1	Denuncia 	procesal	2	\N	\N
1	1	2015-07-18 16:37:01	1	Denuncia	procesal	2	\N	\N
1	2	2015-07-18 16:37:00	1	Caratula expediente	procesal	1	\N	\N
1	2	2015-07-18 16:37:02	1	Archivo 322	procesal	3	\N	\N
2	4	2015-07-18 16:00:00	2	Caratula expediente	procesal	1	\N	\N
2	4	2015-07-18 17:00:00	2	Demanda	procesal	2	\N	\N
2	4	2015-07-18 17:02:00	2	Detalle documental	extraprocesal	3	\N	\N
3	5	2015-05-10 09:00:00	2	Caratula expediente	procesal	1	\N	\N
3	5	2015-05-11 08:45:00	2	Demanda	procesal	2	\N	\N
3	5	2015-05-11 08:49:00	2	Detalle documental archivada	extraprocesal	3	\N	\N
\.


--
-- TOC entry 2150 (class 0 OID 16650)
-- Dependencies: 175
-- Data for Name: Operador; Type: TABLE DATA; Schema: public; Owner: mavignau
--

COPY "Operador" ("idOperador", "CUITCUIL", "idGrupo", "fCreacion", "fFin", "Clave") FROM stdin;
1	7654	1	\N	\N	666
2	23232323	2	\N	\N	555
3	55555	4	\N	\N	444
\.


--
-- TOC entry 2189 (class 0 OID 0)
-- Dependencies: 174
-- Name: Operador_idOperador_seq; Type: SEQUENCE SET; Schema: public; Owner: mavignau
--

SELECT pg_catalog.setval('"Operador_idOperador_seq"', 3, true);


--
-- TOC entry 2167 (class 0 OID 16814)
-- Dependencies: 192
-- Data for Name: Parte; Type: TABLE DATA; Schema: public; Owner: mavignau
--

COPY "Parte" ("CUILCUIT", "idCarpeta", "idExpediente", "Caracter", "Representado") FROM stdin;
55555	1	1	Denunciante	\N
3337744	1	1	Imputado	\N
55555	1	2	Denunciante	\N
3337744	1	2	Imputado	\N
88888	2	4	Actora	\N
23232323	2	4	Demandada	\N
34499	3	5	Actora	\N
\.


--
-- TOC entry 2151 (class 0 OID 16661)
-- Dependencies: 176
-- Data for Name: Persona; Type: TABLE DATA; Schema: public; Owner: mavignau
--

COPY "Persona" ("CUILCUIT", "Apellido", "Nombre", "Sexo", "Domicilio", "EMail", "Observaciones", "Telefono", "Celular") FROM stdin;
23232323	Perez	Juan	M	calle invento 22	\N	\N	\N	\N
55555	Gomez	Teresa	F	calle Imaginaria 3322	\N	\N	\N	\N
88888	Fernandez	Manuel	M	calle Imaginaria 342	\N	\N	\N	\N
7654	Lopez	Osvaldo	M	calle invento 65	\N	\N	\N	\N
3337744	Fernandez	Ana	F	calle Otra 4949	\N	\N	\N	\N
34499	Juarez	Inés	F	calle Imaginaria 2198	\N	\N	\N	\N
\.


--
-- TOC entry 2165 (class 0 OID 16780)
-- Dependencies: 190
-- Data for Name: TipoArchivo; Type: TABLE DATA; Schema: public; Owner: mavignau
--

COPY "TipoArchivo" ("idTipoArchivo", "Descripcion") FROM stdin;
1	Texto
2	Planilla
3	Grafico
4	Presentacion
\.


--
-- TOC entry 2190 (class 0 OID 0)
-- Dependencies: 189
-- Name: TipoArchivo_idTipoArchivo_seq; Type: SEQUENCE SET; Schema: public; Owner: mavignau
--

SELECT pg_catalog.setval('"TipoArchivo_idTipoArchivo_seq"', 4, true);


--
-- TOC entry 2158 (class 0 OID 16708)
-- Dependencies: 183
-- Data for Name: TipoProceso; Type: TABLE DATA; Schema: public; Owner: mavignau
--

COPY "TipoProceso" ("idTipoProceso", "Descripcion") FROM stdin;
1	Ejecutivo
2	Sucesorio
3	Robo
4	Hurto
5	Homicidio
6	Lesiones
\.


--
-- TOC entry 2191 (class 0 OID 0)
-- Dependencies: 182
-- Name: TipoProceso_idTipoProceso_seq; Type: SEQUENCE SET; Schema: public; Owner: mavignau
--

SELECT pg_catalog.setval('"TipoProceso_idTipoProceso_seq"', 6, true);


--
-- TOC entry 2005 (class 2606 OID 16676)
-- Name: Abogado_pk; Type: CONSTRAINT; Schema: public; Owner: mavignau; Tablespace: 
--

ALTER TABLE ONLY "Abogado"
    ADD CONSTRAINT "Abogado_pk" PRIMARY KEY ("CUILCUIT", "Matricula");


--
-- TOC entry 2013 (class 2606 OID 16727)
-- Name: Carpeta_pk; Type: CONSTRAINT; Schema: public; Owner: mavignau; Tablespace: 
--

ALTER TABLE ONLY "Carpeta"
    ADD CONSTRAINT "Carpeta_pk" PRIMARY KEY ("idCarpeta");


--
-- TOC entry 2015 (class 2606 OID 16749)
-- Name: Expediente_pk; Type: CONSTRAINT; Schema: public; Owner: mavignau; Tablespace: 
--

ALTER TABLE ONLY "Expediente"
    ADD CONSTRAINT "Expediente_pk" PRIMARY KEY ("idCarpeta", "idExpediente");


--
-- TOC entry 2007 (class 2606 OID 16689)
-- Name: Fuero_pk; Type: CONSTRAINT; Schema: public; Owner: mavignau; Tablespace: 
--

ALTER TABLE ONLY "Fuero"
    ADD CONSTRAINT "Fuero_pk" PRIMARY KEY ("idFuero");


--
-- TOC entry 1999 (class 2606 OID 16647)
-- Name: GrupoOperador_pk; Type: CONSTRAINT; Schema: public; Owner: mavignau; Tablespace: 
--

ALTER TABLE ONLY "GrupoOperador"
    ADD CONSTRAINT "GrupoOperador_pk" PRIMARY KEY ("idGrupo");


--
-- TOC entry 2009 (class 2606 OID 16700)
-- Name: Juzgado_pk; Type: CONSTRAINT; Schema: public; Owner: mavignau; Tablespace: 
--

ALTER TABLE ONLY "Juzgado"
    ADD CONSTRAINT "Juzgado_pk" PRIMARY KEY ("idJuzgado");


--
-- TOC entry 2017 (class 2606 OID 16772)
-- Name: Movimiento_pk; Type: CONSTRAINT; Schema: public; Owner: mavignau; Tablespace: 
--

ALTER TABLE ONLY "Movimiento"
    ADD CONSTRAINT "Movimiento_pk" PRIMARY KEY ("idCarpeta", "idExpediente", "fCreado");


--
-- TOC entry 2001 (class 2606 OID 16655)
-- Name: Operador_pk; Type: CONSTRAINT; Schema: public; Owner: mavignau; Tablespace: 
--

ALTER TABLE ONLY "Operador"
    ADD CONSTRAINT "Operador_pk" PRIMARY KEY ("idOperador");


--
-- TOC entry 2023 (class 2606 OID 16818)
-- Name: Parte_pk; Type: CONSTRAINT; Schema: public; Owner: mavignau; Tablespace: 
--

ALTER TABLE ONLY "Parte"
    ADD CONSTRAINT "Parte_pk" PRIMARY KEY ("CUILCUIT", "idCarpeta", "idExpediente");


--
-- TOC entry 2003 (class 2606 OID 16668)
-- Name: Persona_pk; Type: CONSTRAINT; Schema: public; Owner: mavignau; Tablespace: 
--

ALTER TABLE ONLY "Persona"
    ADD CONSTRAINT "Persona_pk" PRIMARY KEY ("CUILCUIT");


--
-- TOC entry 2019 (class 2606 OID 16790)
-- Name: TipoArchivo_pk; Type: CONSTRAINT; Schema: public; Owner: mavignau; Tablespace: 
--

ALTER TABLE ONLY "TipoArchivo"
    ADD CONSTRAINT "TipoArchivo_pk" PRIMARY KEY ("idTipoArchivo");


--
-- TOC entry 2011 (class 2606 OID 16716)
-- Name: TipoProceso_pk; Type: CONSTRAINT; Schema: public; Owner: mavignau; Tablespace: 
--

ALTER TABLE ONLY "TipoProceso"
    ADD CONSTRAINT "TipoProceso_pk" PRIMARY KEY ("idTipoProceso");


--
-- TOC entry 2021 (class 2606 OID 16803)
-- Name: agenda_pk; Type: CONSTRAINT; Schema: public; Owner: mavignau; Tablespace: 
--

ALTER TABLE ONLY "Agenda"
    ADD CONSTRAINT agenda_pk PRIMARY KEY ("idCarpeta", "idExpediente", "fCreado");


--
-- TOC entry 2035 (class 2606 OID 16804)
-- Name: Agenda_fk_Creador; Type: FK CONSTRAINT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Agenda"
    ADD CONSTRAINT "Agenda_fk_Creador" FOREIGN KEY ("Creador") REFERENCES "Operador"("idOperador");


--
-- TOC entry 2036 (class 2606 OID 16809)
-- Name: Agenda_fk_TipoArchivo; Type: FK CONSTRAINT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Agenda"
    ADD CONSTRAINT "Agenda_fk_TipoArchivo" FOREIGN KEY ("idTipoArchivo") REFERENCES "TipoArchivo"("idTipoArchivo");


--
-- TOC entry 2029 (class 2606 OID 16734)
-- Name: Carpeta_fk_CarpetaPadre; Type: FK CONSTRAINT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Carpeta"
    ADD CONSTRAINT "Carpeta_fk_CarpetaPadre" FOREIGN KEY ("idCarpetaPadre") REFERENCES "Carpeta"("idCarpeta") ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- TOC entry 2032 (class 2606 OID 16760)
-- Name: Carpeta_fk_Expediente; Type: FK CONSTRAINT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Expediente"
    ADD CONSTRAINT "Carpeta_fk_Expediente" FOREIGN KEY ("idCarpeta") REFERENCES "Carpeta"("idCarpeta") ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- TOC entry 2028 (class 2606 OID 16728)
-- Name: Carpeta_fk_Responsable; Type: FK CONSTRAINT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Carpeta"
    ADD CONSTRAINT "Carpeta_fk_Responsable" FOREIGN KEY ("Responsable") REFERENCES "Operador"("idOperador") ON DELETE RESTRICT;


--
-- TOC entry 2031 (class 2606 OID 16755)
-- Name: Expediente_fk_Juzgado; Type: FK CONSTRAINT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Expediente"
    ADD CONSTRAINT "Expediente_fk_Juzgado" FOREIGN KEY ("idJuzgado") REFERENCES "Juzgado"("idJuzgado");


--
-- TOC entry 2030 (class 2606 OID 16750)
-- Name: Expediente_fk_TipoProceso; Type: FK CONSTRAINT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Expediente"
    ADD CONSTRAINT "Expediente_fk_TipoProceso" FOREIGN KEY ("idTipoProceso") REFERENCES "TipoProceso"("idTipoProceso");


--
-- TOC entry 2024 (class 2606 OID 16656)
-- Name: GrupoOperador_fk; Type: FK CONSTRAINT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Operador"
    ADD CONSTRAINT "GrupoOperador_fk" FOREIGN KEY ("idGrupo") REFERENCES "GrupoOperador"("idGrupo");


--
-- TOC entry 2027 (class 2606 OID 16701)
-- Name: Juzgado_fk_Fuero; Type: FK CONSTRAINT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Juzgado"
    ADD CONSTRAINT "Juzgado_fk_Fuero" FOREIGN KEY ("idFuero") REFERENCES "Fuero"("idFuero");


--
-- TOC entry 2033 (class 2606 OID 16773)
-- Name: Movimiento_fk_Creador; Type: FK CONSTRAINT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Movimiento"
    ADD CONSTRAINT "Movimiento_fk_Creador" FOREIGN KEY ("Creador") REFERENCES "Operador"("idOperador") ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- TOC entry 2034 (class 2606 OID 16791)
-- Name: Movimiento_fk_TipoArchivo; Type: FK CONSTRAINT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Movimiento"
    ADD CONSTRAINT "Movimiento_fk_TipoArchivo" FOREIGN KEY ("idTipoArchivo") REFERENCES "TipoArchivo"("idTipoArchivo") ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- TOC entry 2025 (class 2606 OID 16824)
-- Name: Operador_fk_Persona; Type: FK CONSTRAINT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Operador"
    ADD CONSTRAINT "Operador_fk_Persona" FOREIGN KEY ("CUITCUIL") REFERENCES "Persona"("CUILCUIT") ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- TOC entry 2037 (class 2606 OID 16819)
-- Name: Parte_fk_Representado; Type: FK CONSTRAINT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Parte"
    ADD CONSTRAINT "Parte_fk_Representado" FOREIGN KEY ("Representado") REFERENCES "Persona"("CUILCUIT");


--
-- TOC entry 2026 (class 2606 OID 16677)
-- Name: Persona_fk_Aogado; Type: FK CONSTRAINT; Schema: public; Owner: mavignau
--

ALTER TABLE ONLY "Abogado"
    ADD CONSTRAINT "Persona_fk_Aogado" FOREIGN KEY ("CUILCUIT") REFERENCES "Persona"("CUILCUIT");


--
-- TOC entry 2174 (class 0 OID 0)
-- Dependencies: 5
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2015-07-19 20:59:22 GFT

--
-- PostgreSQL database dump complete
--

