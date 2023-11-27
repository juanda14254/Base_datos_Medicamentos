
CREATE TABLE Importador(
	id integer,
	nombre_importador varchar(500),
	PRIMARY KEY(id)
);

CREATE TABLE Imagen_comercial(
	Nombre_comercial varchar(500),
	Presentacion_comercial varchar(500),
	PRIMARY KEY(Nombre_comercial)
);

CREATE TABLE Forma_Farmaceutica_Imagen(
	Nombre_comercial varchar(500),
	Forma_farmaceutica varchar(500),
	PRIMARY KEY(Nombre_comercial,Forma_farmaceutica),
	FOREIGN KEY(Nombre_comercial) REFERENCES Imagen_comercial(Nombre_comercial)
);
CREATE TABLE Medicamento(
	IUM varchar(200),
	principio_activo varchar(500),
	unidad_de_medida varchar(300),
	concentracion integer,
	Nombre_comercial_imagen_comercial varchar(400),
	PRIMARY KEY(IUM),
	FOREIGN KEY(Nombre_comercial_imagen_comercial) REFERENCES Imagen_comercial(Nombre_comercial)
);

CREATE TABLE solicitud(
	num_solicitud integer,
	IUM_Medicamento varchar(200),
	id_Importador integer,
	fecha_autorizacion date,
      Tipo_solicitud varchar(300),
	PRIMARY KEY(num_solicitud),
	FOREIGN KEY (IUM_Medicamento) REFERENCES Medicamento(IUM),
	FOREIGN KEY (id_Importador) REFERENCES Importador(id)
);



copy  Importador(id,nombre_importador)
from 'C:/carga_masiva/Importador.csv'
with delimiter as ';' csv HEADER ENCODING'windows-1251';	

copy  Imagen_comercial(Nombre_comercial,Presentacion_comercial)
from 'C:/carga_masiva/Imagen_comercial.csv'
with delimiter as ';' csv HEADER ENCODING'windows-1251';	

copy Forma_Farmaceutica_Imagen(Nombre_comercial,Forma_farmaceutica )
from 'C:/carga_masiva/Forma_Farmaceutica_Imagen.csv'
with delimiter as ';' csv HEADER ENCODING'windows-1251';	

copy Medicamento(IUM,principio_activo,unidad_de_medida,concentracion,Nombre_comercial_imagen_comercial, Rango_de_costo_unitario)
from 'C:/carga_masiva/Medicamento.csv'
with delimiter as ';' csv HEADER ENCODING'windows-1251';	


copy solicitud(num_solicitud,IUM_Medicamento,id_Importador,fecha_autorizacion,Tipo_solicitud)
from 'C:/carga_masiva/solicitud.csv'
with delimiter as ';' csv HEADER ENCODING'windows-1251';	

