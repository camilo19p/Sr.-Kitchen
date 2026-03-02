# 🍽️ Sr. Kitchen

[![Java](https://img.shields.io/badge/Java-17%2B-blue)](https://www.java.com)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.x-green)](https://spring.io/projects/spring-boot)
[![MongoDB](https://img.shields.io/badge/MongoDB-NoSQL-47A248)](https://www.mongodb.com)
[![Docker](https://img.shields.io/badge/Docker-Container-blue)](https://www.docker.com)
[![HTML5](https://img.shields.io/badge/HTML5-%23E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/es/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-%231572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/es/docs/Web/CSS)

## 📋 Descripción del Proyecto

**Sr. Kitchen** es un aplicativo web diseñado para optimizar la operación de restaurantes de pequeña y mediana escala. Automatiza y centraliza la gestión de **compras**, **ventas**, **inventarios**, **pedidos** y **reportes financieros**, eliminando procesos manuales propensos a errores y permitiendo decisiones más rápidas y basadas en datos reales.

- **Backend**: Java 17+ con Spring Boot (API REST robusta y escalable)  
- **Base de datos**: MongoDB (esquema flexible para productos, pedidos e inventarios)  
- **Frontend**: HTML5, CSS3, JavaScript + framework moderno (responsive e intuitivo)  
- **Despliegue**: Docker + Docker Compose (portabilidad y facilidad de instalación)  

**Autores:**  
- Camilo Andrés Martínez Peña  
- Jesús David Caldera Baldovino  
- Carlos Andrés Ruiz Herrera  
- Jose Manuel Ayola Arbeláez  

## ✨ Características principales

- Gestión completa de **productos** e **ingredientes** (CRUD completo)  
- Registro y seguimiento de **pedidos** con máquina de estados (pendiente → en preparación → servido → pagado)  
- Control de **inventario** en tiempo real + alertas automáticas de stock bajo  
- Registro de **compras** y **ventas** con actualización automática de existencias  
- **Dashboard** con KPIs clave: ventas del día/mes, ingresos, productos más vendidos, ticket promedio  
- Generación de **reportes** financieros y operativos (exportables)  
- Sistema de **roles y permisos**: Administrador vs. Mesero  
- Interfaz **responsive** y amigable para uso en tablets y computadoras  
- Despliegue sencillo con **Docker**  
- **Próximamente**: pronóstico de demanda, recomendaciones de compra y análisis predictivo  

## 🛠️ Tecnologías utilizadas

| Capa              | Tecnología                          | Propósito                              |
|-------------------|-------------------------------------|----------------------------------------|
| Backend           | Java 17+, Spring Boot 3.x           | Lógica de negocio y API REST           |
| Base de datos     | MongoDB                             | Almacenamiento NoSQL flexible          |
| Frontend          | HTML5, CSS3, JavaScript + framework | Interfaz moderna y responsive          |
| Contenerización   | Docker, Docker Compose              | Portabilidad y despliegue rápido       |
| Gestión de dependencias | Maven                         | Construcción y paquetes                |
| Análisis / Reportes | Power BI (dashboard separado)     | Visualización avanzada de datos        |

## 🖼️ Capturas de pantalla

### Sistema Web (Backend + Frontend)

- **Dashboard principal**  
  ![Dashboard](capturas/captura1.png)

- **Login**  
  ![Login](capturas/captura2.png)

## 📊 Dashboard Analítico en Power BI

Complemento analítico del sistema: análisis histórico y visual de ventas, platos estrella, rendimiento por mesero y tendencias mensuales.

**[➡️ Abrir Dashboard Interactivo de Sr. Kitchen](https://app.powerbi.com/view?r=eyJrIjoiZmVmZDc1N2QtZTMwOS00MjUyLWE2NDUtYzA4ODIxN2I0MzA2IiwidCI6IjlkMTJiZjNmLWU0ZjYtNDdhYi05MTJmLTFhMmYwZmM0OGFhNCIsImMiOjR9)**

- Creado con **Power BI Desktop** (Power Query + DAX)  
- Publicado en **Power BI Service**  
- Datos 100% ficticios generados para demostración y portafolio

## 🚀 Cómo ejecutar el aplicativo

### Opción recomendada: Docker

1. Clona el repositorio
   ```bash
   git clone https://github.com/camilo19p/Sr.-Kitchen.git
   cd Sr.-Kitchen

📜 Licencia y Derechos de Autor
© 2025–2026 Camilo Andrés Martínez Peña y colaboradores
Todos los derechos reservados.
Este software (código fuente, documentación, capturas, recursos asociados) está protegido por derechos de autor.
Prohibido (sin autorización escrita previa de los autores):

Copiar, reproducir, modificar o crear obras derivadas
Distribuir, publicar o subir a otros repositorios/plataformas
Uso comercial, institucional o educativo sin permiso expreso
Eliminar o alterar esta nota de derechos de autor

Para solicitar licencia, colaboración, permiso de uso o más información:
✉️ martinezcamilo25p@gmail.com
