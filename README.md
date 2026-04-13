# Proyecto: Sistema de Tareas
**Alumno:** Brandon Alan Carrion Morales  
**Materia:** Diseño y Arquitectura de Software  
**Fecha:** 12 de Abril 2026

---

## ¿Qué problema resuelve mi aplicación?
Una aplicacion que registra tareas, ya sea que esten en progreso, pendiente o completada
---

## ¿Cuál era el problema del monolito?
Por lo que entendi, fallaron 120 de las 500 que se hicieron, sin embargo no solo fue eso sino que habia mucha latencia casi 1 segundo completo. Por logica
en un sistema grande, suponiendo y adaptandolo a mi proyecto tareas de algun corporativo gigante y sus sucursales, no se haran solo 500, son mas y pueden llegar a tardar mucho mas.

---

## ¿Qué responsabilidad tiene cada microservicio?
**Servicio A:**  
recibe la informacion y lo guarda en la tabla task de mi bd

**Servicio B:**  
procesa la informacion y la guarda en una tabla llamada notifications
---

## ¿Cómo se comunican los servicios?
servicio a manda una peticion a servicio b, este lo encuentra porque en el 

---

## Tablas en la base de datos
| Tabla | Servicio dueño | Qué guarda |
|-------|---------------|------------|
| [nombre] | Servicio A | ... |
| [nombre] | Servicio B | ... |

---

## ¿Qué pasa si el Servicio B se cae?
[Explicar con sus palabras qué observaron en la prueba de resiliencia]

---

## Cómo levantar el proyecto
```bash
# 1. Clonar el repositorio
git clone [url]

# 2. Entrar a la carpeta
cd nombre-apellido-microservicios/microservicios

# 3. Configurar las variables de entorno en docker-compose.yml
# (cambiar DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

# 4. Levantar
docker-compose up --build -d

# 5. Abrir en el navegador
http://IP_DE_TU_EC2:5000
________________________________________
Reflexión Final
[Un párrafo libre. ¿Qué fue lo más difícil? ¿Qué entendieron que antes no entendían? ¿En qué situación real usarían microservicios?]

---

## Checklist de Autoevaluación

Antes de entregar, el alumno debe marcar cada punto. Si alguno no está marcado, la entrega está incompleta:

MONOLITO [ ] El código del monolito original está en la carpeta /monolito [ ] El Dockerfile del monolito existe y es funcional [ ] Hay captura del docker build sin errores [ ] Hay captura del docker run con el contenedor corriendo [ ] Hay captura de Apache Benchmark mostrando saturación
README [ ] Explica el dominio de la aplicación [ ] Explica el problema del monolito con sus propias palabras [ ] Define la responsabilidad de cada servicio en una oración [ ] Explica la comunicación entre servicios [ ] Incluye los comandos para levantar el proyecto [ ] Incluye la reflexión final

---

## Lo que NO se acepta


- Repositorio sin estructura de carpetas — **no se revisa**
- Evidencias sin nombre descriptivo (foto1.png, captura.png) — **no cuentan**
- README con definiciones copiadas de internet o del chat — **cero en esa sección**
- Credenciales escritas directamente en el código — **descuento automático de 10 puntos**
- Las dos capturas de JSON (con B encendido y apagado) siendo idénticas — **la prueba de resiliencia no se realizó**
