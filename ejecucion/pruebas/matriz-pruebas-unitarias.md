# Matriz de pruebas unitarias

{% hint style="warning" %}
**Estado: Pendiente** · ID: **C-21** · Fecha límite: **domingo 22 nov 2026, 23:59** · Responsable: Camilo Mutis · Requiere Turnitin
{% endhint %}

**Qué pide la actividad:** cargar la matriz de pruebas unitarias en el formato adjunto por el docente en Moodle.

## Alcance previsto

Pruebas unitarias de los módulos críticos del código, alineadas con los casos de prueba de sistema [CP-01 a CP-16](plan-pruebas.md):

| Módulo | Qué se prueba | Requisitos |
| --- | --- | --- |
| Pipeline de datos | Control de calidad, normalización, redimensionamiento, partición por paciente | RF-002.1, RF-002.2 |
| Modelo | Carga de pesos, formato de la salida (ROI, clase, confianza) | RF-003 |
| Evaluación | Cálculo de métricas (F1, mAP, Dice, IoU, ECE, Brier) | RF-007, RF-008.1, RF-008.2 |
| API | Validación de archivos, respuestas 200/4xx, health check, no persistencia | RF-004, RNF-015.1, RNF-015.2 |

La cobertura de las pruebas automáticas sobre la API y la capa de IA se medirá con **pytest**.

## Matriz

*Se publicará cuando esté diligenciada.*
