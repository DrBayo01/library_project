<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="300" height="160">
  </a>

<h3 align="center">Library Project (Vaultly)</h3>

  <p align="center">
    Una API REST desarrollada con DRF para gestionar una biblioteca personal y dar seguimiento al progreso de lectura de cada libro.
    <br />
    Este proyecto está diseñado como base escalable para sistemas de tracking de lectura, permitiendo registrar estados, tiempos de lectura y evolución del usuario a lo largo de sus lecturas.
    <br />
    <a href="https://github.com/DrBayo01/library_project"><strong>Explora la documentación »</strong></a>
    <br />
    <br />
    <a href="https://github.com/DrBayo01/library_project/issues/new?labels=bug&template=bug-report---.md">Reportar un Bug</a>
    &middot;
    <a href="https://github.com/DrBayo01/library_project/issues/new?labels=enhancement&template=feature-request---.md">Solicitar Feature</a>
  </p>
</div>



<details>
  <summary>Tabla de contenidos</summary>
  <ol>
    <li>
      <a href="#sobre-el-proyecto">Sobre el proyecto</a>
      <ul>
        <li><a href="#construido-con">Construido con</a></li>
      </ul>
    </li>
    <li>
      <a href="#primeros-pasos">Primeros Pasos</a>
      <ul>
        <li><a href="#requisitos">Requisitos</a></li>
        <li><a href="#instalación-con-docker">Instalación con Docker</a></li>
        <li><a href="#instalación-local">Instalación local</a></li>
      </ul>
    </li>
    <li><a href="#roadmap-del-proyecto">Roadmap del proyecto</a></li>
    <li><a href="#contribuir-al-proyecto">Contribuir al proyecto</a></li>
  </ol>
</details>



## Sobre el proyecto

Llevo un buen tiempo leyendo, y siempre he llevado una lista de mis lecturas en papel. Pero tras mucho tiempo, me he dado cuenta que se me olvidó cuando fue exactamente que comencé y terminé cada uno. Pensaba que con solo llevar el registro bastaba. Fue entonces cuando pensé: "No sería mala idea poder registrar mis lecturas pero además poder tener algunos datos extra para cada uno".

Este proyecto lo hice pensando en eso para uso personal, y he decidido que cualquiera que necesite algo similar pueda usarlo y/o mejorarlo.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



### Construido con

* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]
* [![Django REST Framework][DRF]][DRF-url]
* [![PostgreSQL][PostgreSQL]][PostgreSQL-url]
* [![Docker][Docker]][Docker-url]
* [![Pytest][Pytest]][Pytest-url]
* [![GitHub Actions][GitHubActions]][GitHubActions-url]

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



## Primeros pasos

Sigue las siguientes instrucciones para levantar el proyecto en local.

### Requisitos

Asegurate de tener instalado:
* Python 3.11+
* Docker y Docker Compose
* Git

### Instalación con Docker

1. Clona el repositorio
   ```sh
   git clone https://github.com/DrBayo01/library_project.git
   ```
2. Ve al directorio
   ```sh
   cd library_project
   ```
3. Levanta el contenedor en segundo plano
   ```sh
   docker compose up --build -d
   ```
4. Crea un superusuario de Django (con este podrás interactuar con la API)
   ```sh
   docker compose exec backend python manage.py createsuperuser
   ```
5. Accede a la api del proyecto
   ```http
   http://localhost:8000/api/
   ```
6. Log in con el superusuario dentro del panel de DRF

### Instalación local

1. Clona el repositorio
   ```sh
   git clone https://github.com/DrBayo01/library_project.git
   ```
2. Ve al directorio
   ```sh
   cd library_project
   ```
3. Crea un ambiente virtual
   ```sh
   python -m venv venv
   ```
4. Activa el ambiente
   ```sh
   source venv/bin/activate #Linux/Mac
   venv/Script/Activate.ps1 #Windows
   ```
5. Instala las dependencias del proyecto
   ```sh
   pip install -r requirements.txt
   ```
6. Migra la base de datos
   ```sh
   python manage.py migrate
   ```
7. Crea un superusuario de Django (con este podrás interactuar con la API)
   ```sh
   python manage.py createsuperuser
   ```
8. Ejecuta el servidor
   ```sh
   python manage.py runserver
   ```
9. Accede a la api del proyecto
   ```http
   http://localhost:8000/api/
   ```
10. Log in con el superusuario dentro del panel de DRF


<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



## Roadmap del proyecto

- [ ] Soporte Docker
  - [x] Implementar contenedores para backend
  - [ ] Implementar PostgreSQL en el proyecto
- [ ] Cobertura completa de tests
- [x] Filtros por estado (`GET /books/?status=reading`)
- [ ] Notas y anotaciones por libro
- [ ] Estadísticas de lectura (libros terminados, promedio de días de lectura por libro)
- [ ] Autenticación JWT
- [ ] Documentación de la API con Swagger/OpenAPI
- [ ] Posterior desarrollo de frontend

Consulta [open issues](https://github.com/DrBayo01/library_project/issues) para ver una lista completa de las funciones propuestas (y los problemas conocidos).

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



## Contribuir al proyecto

Las contribuciones son lo que hace que la comunidad de código abierto sea un lugar increíble para aprender, inspirarse y crear. Cualquier contribución que realices es **muy apreciada.**

Si tienes alguna sugerencia que pueda mejorar este proyecto, por favor haz un fork del repositorio y crea un pull request. También puedes abrir un issue con la etiqueta "enhancement".
¡No olvides darle una estrella al proyecto! ¡Gracias de nuevo!

1. Haz un fork del proyecto
2. Crea tu rama de funcionalidad (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Sube los cambios a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



[contributors-shield]: https://img.shields.io/github/contributors/DrBayo01/library_project.svg?style=for-the-badge
[contributors-url]: https://github.com/DrBayo01/library_project/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DrBayo01/library_project.svg?style=for-the-badge
[forks-url]: https://github.com/DrBayo01/library_project/network/members
[stars-shield]: https://img.shields.io/github/stars/DrBayo01/library_project.svg?style=for-the-badge
[stars-url]: https://github.com/DrBayo01/library_project/stargazers
[issues-shield]: https://img.shields.io/github/issues/DrBayo01/library_project.svg?style=for-the-badge
[issues-url]: https://github.com/DrBayo01/library_project/issues
[license-shield]: https://img.shields.io/github/license/DrBayo01/library_project.svg?style=for-the-badge
[license-url]: https://github.com/DrBayo01/library_project/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/byron-mu%C3%B1oz-086440224/
[product-screenshot]: images/screenshot.png

[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[DRF]: https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white
[DRF-url]: https://www.django-rest-framework.org/
[PostgreSQL]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/
[Docker]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[Pytest]: https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white
[Pytest-url]: https://docs.pytest.org/
[GitHubActions]: https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white
[GitHubActions-url]: https://github.com/features/actions