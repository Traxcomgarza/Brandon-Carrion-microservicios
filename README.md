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
servicio a manda una peticion a servicio b, este lo encuentra porque en el Docker le pusimos un nombre
con ese nombre Docker lo encuentra sin necesidad de poner la ip.

---

## Tablas en la base de datos
| Tabla | Servicio dueño | Qué guarda |
|-------|---------------|------------|
| task          | Servicio A | titulo, descripcion y estado de la tarea |
| notificacions | Servicio B | id y titulo de la tarea procesada |

---

## ¿Qué pasa si el Servicio B se cae?
El sistema de tareas sigue funcionando, pero el de notificaciones no, entonces manda un mensaje de 
"servicio b no disponible"
---

## Cómo levantar el proyecto
```bash
# 1. Clonar el repositorio
git clone https://github.com/Traxcomgarza/Brandon-Carrion-microservicios.git

# 2. Entrar a la carpeta
cd Brandon-carrion-microservicios/microservicios

# 3. Configurar las variables de entorno en docker-compose.yml
# (cambiar DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
#*En mi caso yo use archivos dotenv uno en la raiz y otro en la carpeta de microservicios.

# 4. Levantar
docker-compose up --build -d

# 5. Abrir en el navegador
http://IP_DE_TU_EC2:5000
________________________________________
Reflexión Final
Un párrafo libre. ¿Qué fue lo más difícil? ¿Qué entendieron que antes no entendían? ¿En qué situación real usarían
 microservicios?
Uno de lo mas dificil fue trabajar con las versiones y distitos repositorios, ya que yo al inicio cargaba las
llaves a los repositorios esto miismo genero un conflicto, mi solucion fue cargar esa llave pero a mi perfil,
con eso logre que se solucionara el problema de hacer pull o push que reconocia a otros repositorios. Tambien
lo mas dificil a mi parecer fue usar docker, ya que no conocia todos sus comandos, aqui si pedi ayuda a la IA
para agilizar todo, como crear las imagenes, las propiedades de los Dockerfiles y el yaml, la IA tiene errores,
pero con ojo humano logras entender en que se equivoca o que puedes hacer para agilizarlo mejor, por ejemplo
al intentar correr el yaml me daba un codigo para correrlo en la consola y visualizar las peticiones y no de
fondo.  En un proyecto pasado no logre que funcionara, pero gracias a este proyecto logre entenderlo mejor.

Usaria los microservicios si tengo millones de peticiones, para empresas pequeñas no se nota mucho la
diferencia, si un negocio de tal vez 500 personas al dia o en el ejemplo que fueron 500 al mismo tiempo,
no conviene invertir tanto en esto, pero por ejemplo en un juego si se cae algo continua y mas en juegos
competitivos, de igual forma en bancos y otro sistema como amazon si falla la wishlist aun puedes comprar
 los productos buscandolos.

---

## Checklist de Autoevaluación

Antes de entregar, el alumno debe marcar cada punto. Si alguno no está marcado, la entrega está incompleta:

MONOLITO [✓] El código del monolito original está en la carpeta /monolito [✓] El Dockerfile del monolito
existe y es funcional [✓] Hay captura del docker build sin errores [✓] Hay captura del docker run con el
contenedor corriendo [✓] Hay captura de Apache Benchmark mostrando saturación
README [✓] Explica el dominio de la aplicación [✓] Explica el problema del monolito con sus propias palabras
[✓] Define la responsabilidad de cada servicio en una oración [✓] Explica la comunicación entre servicios [✓]
Incluye los comandos para levantar el proyecto [✓] Incluye la reflexión final

---

## Lo que NO se acepta


- Repositorio sin estructura de carpetas — **no se revisa**
- Evidencias sin nombre descriptivo (foto1.png, captura.png) — **no cuentan**
- README con definiciones copiadas de internet o del chat — **cero en esa sección**
- Credenciales escritas directamente en el código — **descuento automático de 10 puntos**
- Las dos capturas de JSON (con B encendido y apagado) siendo idénticas — **la prueba de resiliencia no se realizó**
