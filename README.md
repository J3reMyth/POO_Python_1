# 📌 Práctica Clientes

## 🚀 Ejecución del Programa

Para ejecutar este programa, simplemente ejecuta el archivo `app.py`:

```bash
python app.py
```

---

## 📂 Estructura de Carpetas

```
practicaClientes/
│-- clases/
│   │-- __init__.py
│   │-- classClientes.py
│   │-- classEmpleados.py
│   │-- classPersona.py
│   (Clases que contienen los atributos de clientes y empleados)
│   (Las clases Clientes y Empleados heredan atributos de la clase Persona)
│
│-- datos/
│   │-- empleados.txt
│   │-- clientes.txt
│   (Archivos de datos, si no existen, el programa los crea automáticamente)
│
│-- modulos/
│   │-- __init__.py
│   │-- modClientes.py
│   │-- modEmpleados.py
│   (Módulos para agregar o consultar datos de clientes y empleados)
│
│-- app.py
│   (Archivo principal del programa)
```

---

## 📜 Descripción

Este programa gestiona información de clientes y empleados utilizando archivos de texto para almacenar los datos. Las clases están organizadas en módulos para facilitar su mantenimiento y escalabilidad.

---

## 🛠 Requisitos

- Python 3.x
