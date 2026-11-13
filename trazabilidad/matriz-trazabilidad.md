# Matriz de trazabilidad de requisitos

{% hint style="success" %}
**Estado: Terminado** · ID: **C-04** · Hito 005 · Versión: **v1.1** · Responsable: System Force
{% endhint %}

{% hint style="info" %}
📄 El documento completo se puede leer dentro de esta página, sin descargarlo, en [Documento completo](#documento-completo).
{% endhint %}

Relaciona cada requisito con el objetivo del proyecto, el entregable, el diseño, el desarrollo, la estrategia de pruebas y su prioridad. El archivo completo (*Matriz de Trazabilidad ColorrectalAI v1.1*) está adjunto en Trello, lista **Trazabilidad**.

## Requisito → objetivo → entregable → prueba

| Requisito | Objetivo | Entregable | Prueba | Prioridad |
| --- | --- | --- | --- | --- |
| RF-001.1 Dataset público y desidentificado | OE1 | E01 | CP-01 | Must |
| RF-001.2 Ficha del dataset | OE1 | E01 | CP-01 | Must |
| RF-002.1 Preprocesamiento | OE2 | E02 | CP-02 | Must |
| RF-002.2 ROI, aumento y partición por paciente | OE2 | E02 | CP-03 | Must |
| RF-003 Modelo baseline YOLO | OE3 | E03 | CP-04 | Must |
| RF-004 API de inferencia | OE2/OE3 | E04 | CP-05, CP-06 | Must |
| RF-005.1 Carga y visualización | OE3 | E05 | CP-07 | Must |
| RF-005.2 ROI, clase y confianza | OE3 | E05 | CP-07, CP-08 | Must |
| RF-006 Explicabilidad | OE2/OE3 | E05 | CP-07 | Should |
| RF-007 Calibración | OE4 | E06 | CP-09 | Should |
| RF-008.1 Métricas de clasificación | OE4 | E06 | CP-09 | Must |
| RF-008.2 Métricas de detección y segmentación | OE4 | E06 | CP-09 | Must |
| RF-009 Desempeño operacional | OE4 | E06 | CP-10, CP-12 | Could |
| RF-010 Usabilidad | OE4 | E06 | CP-15 | Could |
| RF-011 Control de versiones | OE2/OE3/OE4 | E08 | CP-16 | Must |
| RF-012 Documentación y reproducción | OE2/OE4 | E08 | CP-16 | Must |

Los requisitos no funcionales y su trazabilidad están en la [ERS](../planeacion/ers.md).

## Trazabilidad por componente

| Componente | Actividad | Evidencia |
| --- | --- | --- |
| Datos | Selección y documentación del dataset | Ficha del dataset + licencia |
| IA | Entrenamiento y evaluación | Modelo + logs + métricas |
| Software | Implementación web | Repositorio + API + interfaz |
| Calidad | Pruebas | Casos de prueba + resultados |
| Reproducibilidad | Documentación | README + versión/tag |
| Ética | Delimitación académica | Aviso de uso experimental |

## Estado de los requisitos

Estados: **especificado → en desarrollo → implementado → verificado → aceptado**.

| Estado | Cantidad |
| --- | --- |
| Especificado | 27 |
| En desarrollo | 0 |
| Implementado | 0 |
| Verificado | 0 |
| Aceptado | 0 |

{% hint style="info" %}
**Meta:** 100 % de los requisitos Must aceptados al cierre del proyecto.
{% endhint %}

## Documento completo

{% embed url="https://drive.google.com/file/d/1rM44zrw3_MCgSZfYVYRgXk3PcowgV5Si/preview" %}
