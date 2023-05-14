CREATE DATABASE IF NOT EXISTS proyecto_python;
use proyecto_python;

CREATE TABLE usuarios(
    id          int (255) auto_increment not null,
    nombre      varchar (100),
    apellidos   varchar(255),
    email       varchar(255) not null,
    password    varchar(255) not null,
    fecha       date not null,
    CONSTRAINT  pk_usuarios PRIMARY KEY (id), /*llave primaria*/
    CONSTRAINT  uq_email UNIQUE (email) /* campo unico*/
)ENGINE=InnoDb; /*Identidad referencial Relaciones entre tablas*/

CREATE TABLE notas (
    id              int(25)auto_increment not null,
    usuario_id      int(25) not null,/*llave forane relacionada*/
    titulo          varchar (255) not null,
    descripcion mediumtext,/*campo de texto*/
    fecha           date not null,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;