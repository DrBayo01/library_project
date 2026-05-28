# Library Project

API REST de biblioteca personal construida con Django y Django REST Framework.

## Características

- Añadir, editar y eliminar libros
- Seguimiento del estado personal de lectura por libro (por leer, leyendo, terminado)
- Registro automático de fechas de inicio y término
- Cálculo de días leyendo un libro

## Tecnologías

- Python
- Django
- Django REST Framework
- pytest

## Instalación

1. Clonar el repositorio (git clone https://github.com/DrBayo01/library_project.git)
2. cd library_project
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

## Endpoints principales

| Método    | Endpoint     | Descripción             |
| --------- | ------------ | ----------------------- |
| GET       | /books/      | Listar todos tus libros |
| POST      | /books/      | Añadir un libro         |
| PUT/PATCH | /books/{id}/ | Editar un libro         |
| DELETE    | /books/{id}/ | Eliminar un libro       |

## Correr tests

pytest

## Roadmap

- [ ] Soporte Docker
- [ ] Cobertura completa de tests
- [x] Filtros por estado (`GET /books/?status=reading`)
- [ ] Notas y anotaciones por libro
- [ ] Estadísticas de lectura (libros terminados, promedio de días por libro)
- [ ] Autenticación JWT
- [ ] Documentación de la API con Swagger/OpenAPI
- [ ] Posterior desarrollo de frontend
