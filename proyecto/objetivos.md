# Objetivos

## Objetivo general

Desarrollar un módulo experimental de detección asistida por inteligencia artificial (ColorrectalAI) sobre imágenes de endoscopia, integrado al ecosistema ONCO-AI_USC 2026 B, mediante técnicas de visión por computador, detección/segmentación y una plataforma web, con el fin de identificar regiones de interés y evaluar su desempeño técnico en un contexto académico y reproducible.

## Objetivos específicos

| ID | Objetivo |
| --- | --- |
| **OE1** | **Analizar** los requerimientos funcionales y no funcionales de ColorrectalAI, junto con el dataset público, su licencia y las restricciones éticas y normativas, para definir el alcance y el backlog del módulo dentro de la arquitectura de ONCO-AI 2026 B. |
| **OE2** | **Diseñar** la arquitectura del módulo, el pipeline de visión por computador (control de calidad, normalización, delimitación de ROI, aumento de datos y partición por paciente), la API de inferencia y los prototipos de la interfaz web, garantizando la trazabilidad entre requerimientos y componentes. |
| **OE3** | **Construir** el modelo baseline de detección o segmentación basado en YOLO, el servicio de inferencia y la interfaz web que permita cargar imágenes de endoscopia y visualizar la región de interés, la clasificación experimental y el nivel de confianza, aplicando control de versiones y documentación reproducible. |
| **OE4** | **Evaluar** el modelo y el sistema mediante métricas de clasificación, detección, segmentación, calibración, desempeño operacional y usabilidad, registrando los resultados como evidencia experimental que respalde la reproducibilidad del proyecto. |

Cada objetivo específico está trazado a los requisitos en la [matriz de trazabilidad](../planeacion/requisitos.md).
