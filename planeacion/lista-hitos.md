# Lista de hitos

{% hint style="success" %}
**Estado: Terminado** · ID: **C-08** · Hito 006 · Entregado: **11 oct 2026** · Responsable: Camilo Mutis
{% endhint %}

Entregable 2.2 del Plan de Gestión del Cronograma (v1.0, 11 de octubre de 2026). Los hitos son eventos de duración cero que marcan la aceptación o verificación de una fase, decisión o entregable.

* **Obligatorio:** exigido por el curso, por PM² (puerta de fase) o por un entregable E01–E09.
* **Opcional:** agrega valor si el tiempo y los recursos lo permiten; no bloquea el cierre.
* Fechas con **(\*)** son estimadas por el equipo y se confirman en la línea base del cronograma.

{% hint style="info" %}
El documento completo se puede leer al final de esta página, en [Documento completo](#documento-completo).
{% endhint %}

## Fase de Inicio

| N.º | Hito | Fecha | Verificación |
| --- | --- | --- | --- |
| 001 | Líder del proyecto elegido | 8 sep 2026 | Acta de elección firmada por los cinco integrantes, en Trello. |
| 002 | Acta de Constitución aprobada | 13 sep 2026 | Acta aprobada por el PP y cargada en Trello. |
| 003 | Gobernanza e interesados definidos | 4 oct 2026 | Sección 6 y matriz de interesados en versión final, revisadas por el DP. |
| 004 | Puerta de fase «Listo para planificar» (RfP) | 4 oct 2026 | Decisión del DP en el acta semanal; sin objeciones del PP. |

## Fase de Planificación

| N.º | Hito | Fecha | Verificación |
| --- | --- | --- | --- |
| 005 | Plan de Gestión del Alcance entregado (matriz de trazabilidad y EDT) | 11 oct 2026 | Carga en Moodle aceptada por Turnitin; RF/RNF trazados a E01–E09. |
| 006 | Plan de Gestión del Cronograma entregado (actividades e hitos) | 11 oct 2026 | Carga en Moodle aceptada por Turnitin. |
| 007 | Cronograma aprobado (línea base del tiempo) | 18 oct 2026 | Gantt en Moodle; el DP congela la línea base. |
| 008 | Plan de Gestión de la Calidad entregado | 18 oct 2026 | Documento en Moodle aceptado por Turnitin. |
| 009 | Plan de Gestión de Costos entregado | 18 oct 2026 | Tarjeta «Plan de Costos» terminada en Trello. |
| 010 | Plan para la Dirección del Proyecto aprobado | 18 oct 2026 | Documento consolidado; aprobación del PP. |
| 011 | Puerta de fase «Listo para ejecutar» (RfE) | 25 oct 2026 (\*) | El DP declara las líneas base aprobadas; cambios por ECP → DP → PP. |

## Fase de Ejecución

| N.º | Hito | Fecha | Verificación |
| --- | --- | --- | --- |
| 012 | **E01** Dataset documentado (PolypGen, CC BY 4.0) | 1 nov 2026 (\*) | Ficha del dataset revisada; particiones por paciente; cita de Ali et al. (2023). |
| 013 | Backlog y arquitectura del módulo definidos | 1 nov 2026 (\*) | Backlog en Trello trazado a la matriz y MoSCoW v2; diagrama de arquitectura en el repositorio. |
| 014 | Diseño de la API y de la interfaz aprobado | 4 nov 2026 (\*) | Mockups revisados contra RF y RNF; contrato de la API documentado. |
| 015 | Umbrales de evaluación acordados | 8 nov 2026 (\*) | Acta con umbrales aprobados antes del primer entrenamiento (RNF-021.1). |
| 016 | **E02** Pipeline reproducible operativo | 8 nov 2026 (\*) | Otro integrante reproduce el pipeline desde un clonado limpio. |
| 017 | **E03** Modelo baseline YOLO entrenado | 15 nov 2026 (\*) | Pesos versionados; métricas vs. umbrales; mapa de explicabilidad y calibración. |
| 018 | **E04** API de inferencia disponible | 19 nov 2026 (\*) | p95 ≤ 5 s, 5 usuarios concurrentes, rechazo de archivos inválidos con 4xx, sin almacenamiento persistente. |
| 019 | **E05** Interfaz web y **E09** aviso de uso experimental | 22 nov 2026 (\*) | Flujo completo en Chrome, Firefox y Edge; interfaz en español; aviso en todas las vistas. |
| 020 | Sistema integrado | 22 nov 2026 (\*) | Prueba E2E por QA y levantamiento con Docker siguiendo solo el README. |
| 021 | **E07** Pruebas aprobadas | 26 nov 2026 (\*) | Informe de pruebas firmado por QA sin defectos críticos abiertos. |
| 022 | **E06** Informe de evaluación entregado | 26 nov 2026 (\*) | Métricas frente a umbrales; limitaciones y sesgos reportados. |
| 023 | Revisión independiente de calidad (ACP) — *opcional* | 27 nov 2026 (\*) | Informe o acta del revisor externo. |
| 024 | Demo desplegada en servicio gratuito — *opcional* | 27 nov 2026 (\*) | URL pública con disponibilidad ≥ 95 %. |
| 025 | **E08** Documentación técnica y guía de reproducción | 29 nov 2026 (\*) | README por módulo; repositorio con PR revisados y versión etiquetada. |

## Fase de Cierre

| N.º | Hito | Fecha | Verificación |
| --- | --- | --- | --- |
| 026 | Puerta de fase «Listo para cerrar» (RfC) | 29 nov 2026 (\*) | Todos los Must en estado «verificado». |
| 027 | Presentación final y aceptación del producto | Semana final (\*) | Sustentación; el PP acepta los entregables. |
| 028 | Acta de Cierre firmada | Semana final (\*) | Acta de cierre en Trello y Moodle. |

## Resumen

| Fase | Hitos | Obligatorios | Opcionales |
| --- | --- | --- | --- |
| Inicio | 001–004 | 4 | 0 |
| Planificación | 005–011 | 7 | 0 |
| Ejecución — Análisis y arquitectura | 012–013 | 2 | 0 |
| Ejecución — Diseño | 014–015 | 2 | 0 |
| Ejecución — Construcción e integración | 016–020 | 5 | 0 |
| Ejecución — Validación final | 021–025 | 3 | 2 |
| Cierre | 026–028 | 3 | 0 |
| **Total** | | **26** | **2** |

## Documento completo

{% embed url="https://docs.google.com/document/d/1YQE6vWYev0fOClXx1h1YeGpgltghe-7JVTN53YgyYE8/preview" %}
