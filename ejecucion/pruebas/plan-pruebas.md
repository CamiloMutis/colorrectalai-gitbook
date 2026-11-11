# Plan de pruebas

{% hint style="warning" %}
**Estado: Pendiente** · ID: **C-22** · Fecha límite: **domingo 29 nov 2026, 23:59** · Responsable: Camilo Mutis
{% endhint %}

**Qué pide la actividad:** adjuntar el Plan de Pruebas en la plantilla PMBOK 6.ª ed. de Moodle (resumen ejecutivo, alcance, funcionalidades a probar, pruebas de regresión, criterios de aceptación y rechazo, criterios de suspensión y reanudación, ambientes de prueba, recursos y entrenamiento, matriz de responsabilidades, cronograma y riesgos).

## Tipos de prueba exigidos

| Funcionales | Casos actuales | No funcionales | Casos actuales |
| --- | --- | --- | --- |
| Del sistema | CP-02, CP-04, CP-07 | Rendimiento | CP-10 |
| De integración | CP-05 | Seguridad | CP-06, CP-13 |
| De aceptación | CP-01, CP-08, CP-09 | Usabilidad | CP-15 |
| De regresión | *Por definir* | Carga | CP-11 |
| | | Estrés | *Por definir* |
| | | Compatibilidad | CP-14 |

{% hint style="info" %}
Faltan casos para **regresión** y **estrés**. CP-03, CP-12 y CP-16 (análisis, fiabilidad y reproducibilidad) se mantienen como pruebas adicionales.
{% endhint %}

## Casos de prueba de la ERS

Casos de prueba **CP-01 a CP-16** definidos en la ERS (sección 3.3). El Tester (QA) registra cada ejecución; si un caso falla, se crea el defecto en el registro de defectos.

| ID | Caso | Requisitos | Tipo | Resultado esperado |
| --- | --- | --- | --- | --- |
| CP-01 | Verificar dataset y ficha | RF-001.1, RF-001.2 | Inspección | Ficha completa; licencia CC BY 4.0 confirmada; sin datos identificables |
| CP-02 | Preprocesamiento | RF-002.1 | Funcional | Imágenes válidas normalizadas; inválidas descartadas con registro |
| CP-03 | Partición por paciente | RF-002.2 | Análisis | Intersección vacía entre entrenamiento y prueba |
| CP-04 | Inferencia del baseline | RF-003 | Funcional | Detecciones con clase y confianza; pesos y configuración versionados |
| CP-05 | Solicitud válida a la API | RF-004 | Integración | Respuesta 200 en JSON con ROI, clase, confianza y versión del modelo |
| CP-06 | Entradas inválidas | RF-004, RNF-015.2 | Seguridad | Rechazo con 4xx y mensaje en español; health check en OK |
| CP-07 | Flujo completo en la interfaz | RF-005.1, RF-005.2, RF-006 | Funcional | Con pólipo: ROI, clase, confianza y región resaltada; sin pólipo: mensaje explícito |
| CP-08 | Aviso y lenguaje no diagnóstico | RNF-016.1, RF-005.2 | Inspección | Aviso visible; ningún texto presenta el resultado como diagnóstico |
| CP-09 | Métricas del modelo | RF-007, RF-008.1, RF-008.2, RNF-021.1 | Análisis | Métricas calculadas y comparadas con los umbrales aprobados |
| CP-10 | Latencia | RNF-013.1, RF-009 | Rendimiento | p95 ≤ 5 s en 100 inferencias consecutivas |
| CP-11 | Concurrencia | RNF-013.2 | Rendimiento | 5 solicitudes simultáneas durante 5 min sin errores 5xx; p95 ≤ 5 s |
| CP-12 | Disponibilidad y errores | RNF-017.1, RF-009 | Fiabilidad | Disponibilidad ≥ 95 %; errores en JSON sin trazas internas |
| CP-13 | Privacidad | RNF-015.1 | Seguridad | Directorio temporal vacío; ninguna imagen ni dato personal guardado |
| CP-14 | Compatibilidad y contraste | RNF-014.2 | Compatibilidad | Sin errores en Chrome, Firefox y Edge; contraste ≥ 4.5:1 |
| CP-15 | Usabilidad (SUS) | RF-010, RNF-014.1 | Usabilidad | SUS medio ≥ 68; 80 % completa la tarea sin ayuda |
| CP-16 | Reproducibilidad | RF-011, RF-012, RNF-018.1, RNF-019.1 | Reproducibilidad | Resultado dentro de ±2 p.p. de mAP@0.5; README y PR revisados |

## Estado actual

| Estado | Cantidad | % |
| --- | --- | --- |
| No ejecutada | 16 | 100 % |
| Aprobada | 0 | 0 % |
| Fallida | 0 | 0 % |
| Bloqueada | 0 | 0 % |

{% hint style="info" %}
**Indicadores:** % de pruebas aprobadas (meta: 100 % de los Must) y cobertura de requisitos (requisitos con al menos una prueba aprobada).
{% endhint %}
