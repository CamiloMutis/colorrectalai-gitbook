# ERS según la norma ISO/IEC/IEEE 29148-2018

{% hint style="success" %}
**Estado: Terminado** · ID: **C-12** · Entregado: **18 oct 2026** · Responsable: Edwin Cabezas
{% endhint %}

{% hint style="info" %}
📄 El documento completo se puede leer dentro de esta página, sin descargarlo, en [Documento completo](#documento-completo).
{% endhint %}

La Especificación de Requisitos de Software (ERS) de ColorrectalAI, según la norma ISO/IEC/IEEE 29148-2018, define **27 requisitos**: 16 funcionales (RF) y 11 no funcionales (RNF). Cada uno está trazado a una prioridad MoSCoW, un entregable y un caso de prueba.

Estados del ciclo de vida de un requisito: **especificado → en desarrollo → implementado → verificado → aceptado**. Un requisito solo se marca como verificado cuando su caso de prueba está aprobado.

## Requisitos funcionales

| ID | Requisito | Prioridad | Entregable | Prueba |
| --- | --- | --- | --- | --- |
| RF-001.1 | Dataset público, anonimizado y desidentificado (PolypGen) | Must | E01 | CP-01 |
| RF-001.2 | Documentación del dataset: procedencia, licencia, población, modalidad, etiquetas, versión, criterios y sesgos | Must | E01 | CP-01 |
| RF-002.1 | Preprocesamiento: control de calidad, desidentificación, normalización y redimensionamiento | Must | E02 | CP-02 |
| RF-002.2 | Delimitación de ROI, aumento de datos y partición por paciente | Must | E02 | CP-03 |
| RF-003 | Modelo baseline de detección/segmentación basado en YOLO | Must | E03 | CP-04 |
| RF-004 | API o servicio de inferencia modelo–plataforma web | Must | E04 | CP-05, CP-06 |
| RF-005.1 | Carga y visualización de imágenes en la interfaz web | Must | E05 | CP-07 |
| RF-005.2 | Presentación de ROI, clasificación experimental y confianza | Must | E05 | CP-07, CP-08 |
| RF-006 | Explicabilidad visual de las regiones relevantes | Should | E05 | CP-07 |
| RF-007 | Calibración de la confianza (Brier Score y/o ECE) | Should | E06 | CP-09 |
| RF-008.1 | Evaluación de clasificación: sensibilidad, especificidad, F1, ROC-AUC, PR-AUC | Must | E06 | CP-09 |
| RF-008.2 | Evaluación de detección (mAP, localización) y segmentación (Dice, IoU) | Must | E06 | CP-09 |
| RF-009 | Medición de latencia, errores y disponibilidad | Could | E06 | CP-10, CP-12 |
| RF-010 | Evaluación de usabilidad (SUS u otro instrumento validado) | Could | E06 | CP-15 |
| RF-011 | Repositorio Git con ramas, pull requests y versiones etiquetadas | Must | E08 | CP-16 |
| RF-012 | Documentación técnica y guía de reproducción | Must | E08 | CP-16 |

## Requisitos no funcionales

| ID | Requisito | Prioridad | Entregable | Prueba |
| --- | --- | --- | --- | --- |
| RNF-013.1 | Rendimiento: inferencia en ≤ 5 s (percentil 95) | Must | E04, E07 | CP-10 |
| RNF-013.2 | Capacidad: al menos 5 usuarios concurrentes sin superar 013.1 | Could | E04, E07 | CP-11 |
| RNF-014.1 | Usabilidad: interfaz en español, sin capacitación previa; SUS ≥ 68 | Could | E05, E06 | CP-15 |
| RNF-014.2 | Compatibilidad con Chrome, Firefox y Edge; ROI legible desde 1366×768 | Should | E05 | CP-14 |
| RNF-015.1 | Privacidad: solo imágenes públicas desidentificadas, sin almacenamiento persistente | Must | E04 | CP-13 |
| RNF-015.2 | Seguridad: validación de archivos (JPEG/PNG, ≤ 10 MB) y HTTPS fuera del entorno local | Must | E04, E05 | CP-06 |
| RNF-016.1 | Ética: aviso visible de uso experimental; licencia del dataset y Ley 1581 de 2012 | Must | E09 | CP-08 |
| RNF-017.1 | Disponibilidad ≥ 95 % en pruebas y demostraciones; errores sin mensajes técnicos | Could | E04, E07 | CP-12 |
| RNF-018.1 | Reproducibilidad: semillas fijas, versiones de dependencias y datos registradas | Must | E02, E08 | CP-16 |
| RNF-019.1 | Mantenibilidad: módulos desacoplados, código documentado y revisado por PR | Should | E08 | CP-16 |
| RNF-021.1 | Calidad del modelo: umbrales aprobados antes de evaluar; reporte de limitaciones y sesgos | Must | E06 | CP-09 |

## Casos de prueba

La ERS (sección 3.3) define los casos de prueba **CP-01 a CP-16**, detallados en el [Plan de pruebas](../ejecucion/pruebas/plan-pruebas.md). La prioridad de cada requisito está en el [Diagrama MoSCoW](moscow.md) y su trazabilidad completa en la [Matriz de trazabilidad](../trazabilidad/matriz-trazabilidad.md).

## Documento completo

{% embed url="https://drive.google.com/file/d/1rd516FzNu8k5FJQCpdyoIpXxmuCNWzgR/preview" %}
