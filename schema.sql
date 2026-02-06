-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION pg_database_owner;

COMMENT ON SCHEMA public IS 'standard public schema';

-- DROP SEQUENCE public.alimentacao_id_seq;

CREATE SEQUENCE public.alimentacao_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.compras_id_seq;

CREATE SEQUENCE public.compras_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.dinosauros_id_seq;

CREATE SEQUENCE public.dinosauros_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.especies_id_seq;

CREATE SEQUENCE public.especies_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.funcionarios_id_seq;

CREATE SEQUENCE public.funcionarios_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.habitats_id_seq;

CREATE SEQUENCE public.habitats_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.incidentes_id_seq;

CREATE SEQUENCE public.incidentes_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.ingressos_id_seq;

CREATE SEQUENCE public.ingressos_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.recintos_id_seq;

CREATE SEQUENCE public.recintos_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.visitantes_id_seq;

CREATE SEQUENCE public.visitantes_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;-- public.funcionarios definição

-- Drop table

-- DROP TABLE public.funcionarios;

CREATE TABLE public.funcionarios (
	id serial4 NOT NULL,
	nome varchar(100) NOT NULL,
	cargo varchar(50) NULL,
	CONSTRAINT funcionarios_pkey PRIMARY KEY (id)
);


-- public.habitats definição

-- Drop table

-- DROP TABLE public.habitats;

CREATE TABLE public.habitats (
	id serial4 NOT NULL,
	nome varchar(100) NULL,
	clima varchar(50) NULL,
	continente varchar(50) NULL,
	descricao text NULL,
	CONSTRAINT habitats_pkey PRIMARY KEY (id)
);


-- public.ingressos definição

-- Drop table

-- DROP TABLE public.ingressos;

CREATE TABLE public.ingressos (
	id serial4 NOT NULL,
	tipo varchar(20) NULL,
	preco numeric(8, 2) NULL,
	data_ingresso date NOT NULL,
	CONSTRAINT ingressos_pkey PRIMARY KEY (id),
	CONSTRAINT ingressos_tipo_check CHECK (((tipo)::text = ANY ((ARRAY['normal'::character varying, 'vip'::character varying, 'premium'::character varying])::text[])))
);


-- public.recintos definição

-- Drop table

-- DROP TABLE public.recintos;

CREATE TABLE public.recintos (
	id serial4 NOT NULL,
	nome varchar(100) NOT NULL,
	area numeric(10, 2) NULL,
	capacidade int4 NULL,
	clima_controlado bool DEFAULT false NULL,
	nivel_seguranca int4 DEFAULT 3 NULL,
	CONSTRAINT recintos_nivel_seguranca_check CHECK (((nivel_seguranca >= 1) AND (nivel_seguranca <= 5))),
	CONSTRAINT recintos_pkey PRIMARY KEY (id)
);


-- public.especies definição

-- Drop table

-- DROP TABLE public.especies;

CREATE TABLE public.especies (
	id serial4 NOT NULL,
	nome_pop varchar(100) NOT NULL,
	nome_sci varchar(100) NOT NULL,
	periodo varchar(50) NULL,
	tipo varchar(20) NULL,
	gene_sapo bool DEFAULT false NULL,
	numero_oficial int4 DEFAULT 0 NOT NULL,
	habitat_id int4 NULL,
	CONSTRAINT especies_pkey PRIMARY KEY (id),
	CONSTRAINT especies_tipo_check CHECK (((tipo)::text = ANY ((ARRAY['carnivoro'::character varying, 'herbivoro'::character varying, 'onivoro'::character varying])::text[]))),
	CONSTRAINT especies_habitat_id_fkey FOREIGN KEY (habitat_id) REFERENCES public.habitats(id)
);


-- public.funcionario_recinto definição

-- Drop table

-- DROP TABLE public.funcionario_recinto;

CREATE TABLE public.funcionario_recinto (
	funcionario_id int4 NOT NULL,
	recinto_id int4 NOT NULL,
	CONSTRAINT funcionario_recinto_pkey PRIMARY KEY (funcionario_id, recinto_id),
	CONSTRAINT funcionario_recinto_funcionario_id_fkey FOREIGN KEY (funcionario_id) REFERENCES public.funcionarios(id),
	CONSTRAINT funcionario_recinto_recinto_id_fkey FOREIGN KEY (recinto_id) REFERENCES public.recintos(id)
);


-- public.visitantes definição

-- Drop table

-- DROP TABLE public.visitantes;

CREATE TABLE public.visitantes (
	id serial4 NOT NULL,
	nome varchar(100) NOT NULL,
	idade int4 NULL,
	ingresso_id int4 NULL,
	CONSTRAINT visitantes_pkey PRIMARY KEY (id),
	CONSTRAINT visitantes_ingresso_id_fkey FOREIGN KEY (ingresso_id) REFERENCES public.ingressos(id)
);


-- public.compras definição

-- Drop table

-- DROP TABLE public.compras;

CREATE TABLE public.compras (
	id serial4 NOT NULL,
	visitante_id int4 NULL,
	ingresso_id int4 NULL,
	data_compra timestamp DEFAULT now() NOT NULL,
	CONSTRAINT compras_pkey PRIMARY KEY (id),
	CONSTRAINT compras_ingresso_id_fkey FOREIGN KEY (ingresso_id) REFERENCES public.ingressos(id),
	CONSTRAINT compras_visitante_id_fkey FOREIGN KEY (visitante_id) REFERENCES public.visitantes(id)
);


-- public.dinosauros definição

-- Drop table

-- DROP TABLE public.dinosauros;

CREATE TABLE public.dinosauros (
	id serial4 NOT NULL,
	nome varchar(100) NOT NULL,
	especie_id int4 NULL,
	data_nascimento date NULL,
	peso numeric(8, 2) NULL,
	altura numeric(6, 2) NULL,
	recinto_id int4 NULL,
	sexo bpchar(1) DEFAULT 'F'::bpchar NOT NULL,
	CONSTRAINT dinosauros_pkey PRIMARY KEY (id),
	CONSTRAINT dinosauros_sexo_check CHECK ((sexo = ANY (ARRAY['F'::bpchar, 'M'::bpchar]))),
	CONSTRAINT dinosauros_especie_id_fkey FOREIGN KEY (especie_id) REFERENCES public.especies(id),
	CONSTRAINT dinosauros_recinto_id_fkey FOREIGN KEY (recinto_id) REFERENCES public.recintos(id)
);


-- public.incidentes definição

-- Drop table

-- DROP TABLE public.incidentes;

CREATE TABLE public.incidentes (
	id serial4 NOT NULL,
	"data" timestamp NOT NULL,
	tipo varchar(50) NULL,
	dino_id int4 NULL,
	recinto_id int4 NULL,
	visitante_id int4 NULL,
	CONSTRAINT incidentes_pkey PRIMARY KEY (id),
	CONSTRAINT incidentes_dino_id_fkey FOREIGN KEY (dino_id) REFERENCES public.dinosauros(id),
	CONSTRAINT incidentes_recinto_id_fkey FOREIGN KEY (recinto_id) REFERENCES public.recintos(id),
	CONSTRAINT incidentes_visitante_id_fkey FOREIGN KEY (visitante_id) REFERENCES public.visitantes(id)
);


-- public.alimentacao definição

-- Drop table

-- DROP TABLE public.alimentacao;

CREATE TABLE public.alimentacao (
	id serial4 NOT NULL,
	dino_id int4 NULL,
	"data" timestamp DEFAULT now() NOT NULL,
	alimento varchar(100) NULL,
	quantidade_kg numeric(8, 2) NULL,
	CONSTRAINT alimentacao_pkey PRIMARY KEY (id),
	CONSTRAINT alimentacao_dino_id_fkey FOREIGN KEY (dino_id) REFERENCES public.dinosauros(id)
);