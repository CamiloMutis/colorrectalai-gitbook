# Plan de calidad y métricas

Metas y tolerancias de calidad del producto definidas en el Plan de Gestión de la Calidad V1.0. Las mide el Tester (QA) según la frecuencia de cada métrica.

## Métricas del modelo

| Métrica | Sentido | Meta | Tolerancia | Nota |
| --- | --- | --- | --- | --- |
| Sensibilidad (recall) | ≥ | 0,80 | 0,75 | |
| Especificidad | ≥ | 0,80 | 0,75 | |
| F1 | ≥ | 0,75 | 0,70 | |
| ROC-AUC | ≥ | 0,85 | 0,80 | |
| PR-AUC | ≥ | 0,75 | 0,70 | |
| mAP@0.5 (detección) | ≥ | 0,60 | 0,55 | |
| Dice (segmentación) | ≥ | 0,70 | 0,65 | Solo si el baseline es de segmentación |
| IoU (segmentación) | ≥ | 0,60 | 0,55 | Solo si el baseline es de segmentación |
| ECE | ≤ | 0,10 | 0,15 | |
| Brier Score | ≤ | 0,15 | 0,20 | |

Frecuencia: al cerrar cada ciclo de entrenamiento.

## Métricas del sistema y del proceso

| Métrica | Frecuencia | Meta | Tolerancia | Nota |
| --- | --- | --- | --- | --- |
| Latencia por imagen (s) | Cada prueba de integración | ≤ 2 | 3 | La ERS fija p95 ≤ 5 s; umbral pendiente de unificar (SC-01) |
| Tasa de errores del sistema | Cada prueba de integración | ≤ 2 % | 5 % | |
| Usabilidad (SUS) | Evaluación con usuarios | ≥ 68 | 60 | Desde 60 se acepta con plan de mejora |
| Casos de prueba críticos aprobados | Al terminar cada componente | 100 % | 100 % | Sin tolerancia |
| Diferencia de mAP@0.5 al reproducir | Antes de la entrega final | ≤ 0,02 | 0,02 | Ningún paciente compartido entre entrenamiento y prueba |
| Pantallas de resultado con aviso experimental | Cada versión de la interfaz | 100 % | 100 % | Sin tolerancia |

{% hint style="warning" %}
**Solicitud de cambio SC-01:** unificar el umbral de latencia, que difiere entre la ERS (p95 ≤ 5 s) y el Plan de Gestión de la Calidad (≤ 2 s).
{% endhint %}

## Indicadores de evaluación

| Dimensión | Métrica | Propósito |
| --- | --- | --- |
| Clasificación | Sensibilidad, especificidad, F1, ROC-AUC, PR-AUC | Medir desempeño del modelo |
| Detección | mAP y métricas de localización | Evaluar identificación de lesiones |
| Segmentación | Dice, IoU | Evaluar delimitación de ROI |
| Calibración | Brier Score, ECE | Evaluar confiabilidad de la confianza |
| Sistema | Latencia, errores, disponibilidad | Evaluar calidad operacional |
| Usabilidad | SUS u otro instrumento validado | Evaluar experiencia de usuario |
