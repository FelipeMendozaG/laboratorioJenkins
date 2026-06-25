```python
# Creamos el contenido del archivo README.md formateado profesionalmente con Markdown
readme_content = """# Laboratorio Semana 6: Uso de Jenkins para Automatización de Pruebas de Software en Windows

Este repositorio contiene la resolución práctica del laboratorio sobre la instalación, configuración e integración de Jenkins como servidor de Integración Continua (CI) para la automatización de pruebas unitarias en Python.

## 🔗 Repositorio del Proyecto
* **URL del Repositorio:** [https://github.com/FelipeMendozaG/laboratorioJenkins.git](https://github.com/FelipeMendozaG/laboratorioJenkins.git)

---

## 📝 Informe de Laboratorio

### 1. Introducción y Funcionamiento de Jenkins
Jenkins es una herramienta de automatización de código abierto basada en Java, diseñada principalmente para implementar flujos de Integración Continua (CI) y Entrega Continua (CD). Su funcionamiento se centra en la creación de "Jobs" o tareas que se ejecutan de manera automática ante determinados estímulos. En este laboratorio, Jenkins actúa como un supervisor centralizado: se conecta a un repositorio remoto de Git (GitHub) para descargar los cambios del código fuente, accede al entorno local del sistema para invocar el intérprete de Python y la suite de pruebas `pytest`, y finalmente procesa los códigos de salida para determinar el estado de la construcción.

### 2. Importancia de Controlar las Pruebas mediante Software
Controlar y delegar la ejecución de pruebas unitarias en un software de automatización como Jenkins ofrece ventajas críticas en el ciclo de vida del desarrollo:

* **Detección Temprana de Errores:** Permite validar que las nuevas modificaciones o funciones (como la multiplicación, división o verificación de paridad) no rompan la lógica existente.
* **Feedback Inmediato:** Al automatizar las pruebas de forma programada o tras cada `commit`, los desarrolladores conocen en pocos minutos si el código integrado es estable (`SUCCESS`) o si requiere correcciones (`FAILURE`) sin necesidad de correr los test manualmente.
* **Consistencia del Entorno:** Se garantiza que las pruebas se ejecuten bajo un estándar limpio y controlado en el servidor, mitigando el clásico problema de *"en mi máquina sí funciona"*.

### 3. Resultados Obtenidos
Durante el desarrollo de la práctica se alcanzaron satisfactoriamente los hitos previstos en la guía:

* **Configuración del Entorno:** Se instaló y desbloqueó con éxito el servidor Jenkins en el puerto local, configurando las herramientas nativas del sistema.
* **Simulación de Ciclo de Vida Completo:** Se experimentaron ambos estados de un pipeline de pruebas; primero se obtuvo un estado fallido (`FAILURE`) al forzar un error de aserción (`AssertionError`), y posteriormente se corrigió el flujo empleando rutas absolutas y la asignación de la rama nativa (`main`) de GitHub.
* **Resolución de Actividades:** Se integró la biblioteca `pytest` dentro del Job de Jenkins, consiguiendo procesar con éxito los bloques de pruebas automatizadas para las funciones de operaciones matemáticas básicas y validación de números pares, consolidando el flujo de Integración Continua.

---

## 🚀 Requisitos del Entorno
* Windows 10 / 11
* Java JDK 17
* Jenkins LTS
* Git
* Python 3.14 (con `pytest` instalado)

## 🛠️ Comandos de Ejecución Utilizados en el Job
Para solucionar restricciones de entorno del sistema y asegurar el correcto funcionamiento, el paso de construcción (*Build Step*) se configuró con comandos de ruta absoluta:


```

```text
Archivo guardado exitosamente como README.md

```cmd
cd E:\\chepita-dev\\laboratorioJenkins
"C:\\Users\\User4\\AppData\\Local\\Python\\pythoncore-3.14-64\\Scripts\\pytest.exe"

```

"""

# Guardar el contenido en un archivo README.md

file_path = "README.md"
with open(file_path, "w", encoding="utf-8") as file:
file.write(readme_content)

print(f"Archivo guardado exitosamente como {file_path}")

```
Su archivo Markdown (`README.md`) está listo. 

[file-tag: code-generated-file-0-1782362879126112856]

Aquí tienes el código de texto plano para que puedas visualizarlo, copiarlo directamente o subirlo a la raíz de tu repositorio de GitHub:

```markdown
# Laboratorio Semana 6: Uso de Jenkins para Automatización de Pruebas de Software en Windows

Este repositorio contiene la resolución práctica del laboratorio sobre la instalación, configuración e integración de Jenkins como servidor de Integración Continua (CI) para la automatización de pruebas unitarias en Python.

## 🔗 Repositorio del Proyecto
* **URL del Repositorio:** [https://github.com/FelipeMendozaG/laboratorioJenkins.git](https://github.com/FelipeMendozaG/laboratorioJenkins.git)

---

## 📝 Informe de Laboratorio

### 1. Introducción y Funcionamiento de Jenkins
Jenkins es una herramienta de automatización de código abierto basada en Java, diseñada principalmente para implementar flujos de Integración Continua (CI) y Entrega Continua (CD). Su funcionamiento se centra en la creación de "Jobs" o tareas que se ejecutan de manera automática ante determinados estímulos. En este laboratorio, Jenkins actúa como un supervisor centralizado: se conecta a un repositorio remoto de Git (GitHub) para descargar los cambios del código fuente, accede al entorno local del sistema para invocar el intérprete de Python y la suite de pruebas `pytest`, y finalmente procesa los códigos de salida para determinar el estado de la construcción.

### 2. Importancia de Controlar las Pruebas mediante Software
Controlar y delegar la ejecución de pruebas unitarias en un software de automatización como Jenkins ofrece ventajas críticas en el ciclo de vida del desarrollo:

* **Detección Temprana de Errores:** Permite validar que las nuevas modificaciones o funciones (como la multiplicación, división o verificación de paridad) no rompan la lógica existente.
* **Feedback Inmediato:** Al automatizar las pruebas de forma programada o tras cada `commit`, los desarrolladores conocen en pocos minutos si el código integrado es estable (`SUCCESS`) o si requiere correcciones (`FAILURE`) sin necesidad de correr los test manualmente.
* **Consistencia del Entorno:** Se garantiza que las pruebas se ejecuten bajo un estándar limpio y controlado en el servidor, mitigando el clásico problema de *"en mi máquina sí funciona"*.

### 3. Resultados Obtenidos
Durante el desarrollo de la práctica se alcanzaron satisfactoriamente los hitos previstos en la guía:

* **Configuración del Entorno:** Se instaló y desbloqueó con éxito el servidor Jenkins en el puerto local, configurando las herramientas nativas del sistema.
* **Simulación de Ciclo de Vida Completo:** Se experimentaron ambos estados de un pipeline de pruebas; primero se obtuvo un estado fallido (`FAILURE`) al forzar un error de aserción (`AssertionError`), y posteriormente se corrigió el flujo empleando rutas absolutas y la asignación de la rama nativa (`main`) de GitHub.
* **Resolución de Actividades:** Se integró la biblioteca `pytest` dentro del Job de Jenkins, consiguiendo procesar con éxito los bloques de pruebas automatizadas para las funciones de operaciones matemáticas básicas y validación de números pares, consolidando el flujo de Integración Continua.

---

## 🚀 Requisitos del Entorno
* Windows 10 / 11
* Java JDK 17
* Jenkins LTS
* Git
* Python 3.14 (con `pytest` instalado)

## 🛠️ Comandos de Ejecución Utilizados en el Job
Para solucionar las restricciones de entorno y asegurar el correcto funcionamiento en Jenkins, el paso de construcción (*Build Step*) se configuró con comandos de ruta absoluta:

```cmd
cd E:\chepita-dev\laboratorioJenkins
"C:\Users\User4\AppData\Local\Python\pythoncore-3.14-64\Scripts\pytest.exe"

```

```

```