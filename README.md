---
description: >-
  Módulo experimental de detección asistida por IA sobre imágenes de endoscopia,
  parte del ecosistema ONCO-AI_USC 2026 B.
---

# ColorrectalAI

{% hint style="warning" %}
**Uso académico y experimental.** ColorrectalAI no realiza diagnóstico médico, no sustituye el criterio de profesionales de la salud y no es un dispositivo médico autorizado.
{% endhint %}

## ¿Qué es ColorrectalAI?

ColorrectalAI es uno de los módulos de la línea **Clínica AI Web** del ecosistema **ONCO-AI_USC 2026 B**. Es una plataforma web que, mediante visión por computador y un modelo de detección/segmentación basado en **YOLO**, identifica **regiones de interés (ROI)** en imágenes de endoscopia, presenta una **clasificación experimental** y muestra el **nivel de confianza** del modelo.

El propósito es construir un **artefacto académico reproducible** que permita estudiar detección, confianza, explicabilidad, rendimiento e interacción humano–IA.

## Datos generales

| Campo | Información |
| --- | --- |
| Universidad | Universidad Santiago de Cali — Facultad de Ingeniería |
| Programa | Ingeniería de Sistemas |
| Curso | Gestión de Proyectos de TI |
| Propietario del proyecto (docente) | Ing. Jair Enrique Castro Sanclemente |
| Director de proyecto | Edwin Cabezas Cuero |
| Equipo | System Force |
| Periodo | 2026-2 (septiembre – diciembre 2026) |
| Metodología de gestión | PM² adaptada al contexto académico, planeación según PMBOK 6.ª ed. |
| Metodología de desarrollo | Team Software Process (TSP) |
| Dataset | PolypGen (Synapse), licencia CC BY 4.0 |

## Entregables del producto

| ID | Entregable |
| --- | --- |
| E01 | Dataset documentado |
| E02 | Pipeline reproducible |
| E03 | Modelo baseline YOLO |
| E04 | API de inferencia |
| E05 | Interfaz web |
| E06 | Informe de evaluación y registro de experimentos |
| E07 | Pruebas |
| E08 | Documentación técnica y guía de reproducción |
| E09 | Aviso de uso experimental |

## Cómo navegar esta documentación

La documentación sigue la misma organización del tablero de Trello del proyecto:

* **Elección del líder del proyecto** — acta de elección y equipo.
* **Inicio** — formulación del proyecto, acta de inicio y matriz de interesados.
* **Planeación** — planes de alcance, tiempo, costos, calidad y dirección; EDT, cronograma, hitos, ERS y MoSCoW.
* **Ejecución** — requisitos, datos, modelo IA, desarrollo del software, integración y pruebas.
* **Monitoreo y control** — metodología TSP y valor ganado.
* **Cierre** — acta de cierre, lecciones aprendidas y documentación final.
* **Trazabilidad** — matriz de trazabilidad y acta de inicio corregida.

Cada página indica arriba su **estado** (Terminado, En curso o Pendiente), su código (C-xx), su responsable y su fecha. Las entregas futuras ya tienen su página con lo que deben contener. El resumen está en [Estado de la documentación](estado.md).
