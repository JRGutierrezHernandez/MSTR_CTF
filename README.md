# 🖥️ Monitor del Sistema en Tiempo Real (Python + Web)
<img width="847" height="310" alt="Captura de pantalla 2026-02-23 043453" src="https://github.com/user-attachments/assets/83f88a39-9862-4726-8c26-7697cf19af64" />

Aplicación web que muestra el uso del sistema en tiempo real (CPU y memoria RAM) utilizando un backend en Python con ejecución concurrente mediante hilos.

El sistema obtiene información real del equipo y la muestra en un panel web que se actualiza automáticamente cada segundo.

## 🚀 Características

✔ Monitoreo en tiempo real del CPU

✔ Monitoreo en tiempo real de la memoria RAM

✔ Backend en Python con Flask

✔ Uso de hilos (threading) para monitoreo continuo

✔ Interfaz web dinámica

✔ Comunicación cliente-servidor

✔ Actualización automática sin recargar la página

✔ Diseño tipo dashboard moderno

## 🧠 Tecnologías utilizadas

Python

Flask

psutil

threading (concurrencia)

HTML5

CSS3

JavaScript (Fetch API)
Funcionamiento del sistema

El sistema está dividido en dos partes principales:

🔹 Backend

Un hilo independiente se ejecuta continuamente en segundo plano obteniendo información del sistema mediante la librería psutil.
Estos datos se almacenan en memoria y se exponen mediante una API REST.

🔹 Frontend

La página web realiza peticiones periódicas al servidor para obtener los datos actualizados y mostrarlos en pantalla sin recargar la página.

⚡ Concurrencia implementada

Se utiliza un hilo en segundo plano para monitorear el sistema de forma continua sin bloquear el servidor web.

Esto permite:

Recolección constante de datos

Respuesta rápida del servidor

Actualización en tiempo real

## 📊 Datos monitoreados

Uso del CPU (%)

Uso de memoria RAM (%)

## 🎯 Objetivo del proyecto

Demostrar el uso de:

Programación concurrente con hilos

Monitoreo del sistema en tiempo real

Arquitectura cliente-servidor

Integración backend + frontend

## 📌 Posibles mejoras futuras

Gráficas en tiempo real

Historial de uso del sistema

Lista de procesos activos

Temperatura del CPU

Alertas por uso alto

WebSockets en tiempo real

Panel estilo administrador de tareas
