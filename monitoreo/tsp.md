# Monitoreo y control con TSP

Entregable **C-24** (v1.0, 24/10/2026). Define los formatos, plantillas, métricas y herramientas con que el equipo System Force monitorea y controla ColorrectalAI con **Team Software Process (TSP)** entre el 28/09/2026 y el 11/12/2026, para los entregables C-01 a C-30.

## Fundamentos

TSP es el marco de proceso para equipos autodirigidos de 3 a 20 ingenieros formados en PSP (Humphrey, 2000). Cada ciclo tiene:

1. **Lanzamiento** — metas, roles y plan de tareas con horas estimadas.
2. **Ejecución** — cada integrante registra su tiempo y sus defectos; reunión semanal.
3. **Postmortem** — análisis de los datos para mejorar el siguiente ciclo.

El control se apoya en el **valor ganado**: cada tarea vale un porcentaje del proyecto proporcional a sus horas planeadas, y ese valor solo se gana cuando la tarea está terminada por completo.

## Ciclo de monitoreo y control

| Momento | Actividad | Formato | Responsable |
| --- | --- | --- | --- |
| Lanzamiento | Confirmar roles, estimar horas, distribuir el valor planeado y registrar riesgos | TASK, SCHEDULE, ITL | Líder y gestor de planeación |
| Diario | Registrar cada sesión de trabajo y cada defecto | LOGT, LOGD | Cada integrante |
| Cada revisión | Revisar el artefacto antes de entregarlo | INS, LOGD, listas de verificación | Gestor de calidad |
| Semanal | Actualizar tareas; calcular VG, SPI y desviación; revisar riesgos | TASK, SCHEDULE, WEEK, ITL | Gestor de planeación y líder |
| Cierre de hito | Calcular métricas del proceso y registrar lecciones aprendidas | SUMP, SUMQ | Gestor de calidad |

## Control del alcance

| Formato | Qué controla | Indicador |
| --- | --- | --- |
| Matriz de seguimiento de requisitos | Estado de los 27 requisitos de la ERS | % de requisitos aceptados; meta 100 % de los Must |
| Plan de tareas (TASK) | Entregables C-01 a C-30 | % de entregables terminados |
| Registro de cambios | Solicitudes de cambio con impacto y decisión | Cambios abiertos y aprobados |

## Control del tiempo

| Métrica | Fórmula | Umbral |
| --- | --- | --- |
| Valor planeado (VP) | Horas planeadas de la tarea / horas totales × 100 | — |
| Valor ganado (VG) | Suma del VP de las tareas terminadas | — |
| Índice de cronograma (SPI) | VG acumulado / VP acumulado | ≥ 0,90 (desviación ≤ 10 %) |
| Índice de costo (CPI) | Horas planeadas / horas reales de tareas terminadas | 0,90 a 1,10 |
| Cumplimiento de hitos | Hitos alcanzados en fecha / hitos programados | 100 %; retraso > 10 % se comunica al PP |

> **Ejemplo:** si el plan suma 400 horas y la tarea C-16 tiene 20, su VP es 5 %. Si a la semana 4 el VP acumulado es 40 % y el VG 34 %, el SPI es 0,85: la desviación del 15 % supera el umbral. Si ocurre una semana se reasigna trabajo; si se repite dos semanas, se replanean las tareas restantes y se registra una solicitud de cambio.

## Control de la calidad

En TSP la calidad se controla **antes** de entregar cada artefacto. Cada defecto se registra con su fase de inyección y de eliminación.

Procedimiento: el autor revisa con la lista de verificación → otro integrante inspecciona → el autor corrige → se entrega solo si no hay defectos mayores abiertos.

| Métrica | Fórmula | Umbral |
| --- | --- | --- |
| Pruebas aprobadas | Casos aprobados / casos ejecutados | 100 % de los Must |
| Cobertura de requisitos | Requisitos con ≥ 1 prueba aprobada / requisitos del alcance | 100 % de los Must |
| Rendimiento del proceso (yield) | Defectos removidos en revisiones / (revisiones + pruebas) | ≥ 70 % |
| Razón evaluación/falla (A/FR) | Tiempo de revisión / tiempo de pruebas | ≥ 2,0 |
| Densidad de defectos en pruebas | Defectos en pruebas / KLOC | ≤ 5 |
| Entregables con revisión por pares | Tareas revisadas / tareas terminadas | 100 % |

## Herramientas

* **Process Dashboard** — herramienta libre (GNU GPL) para PSP/TSP: registro de tiempo, defectos y tamaño, planeación, valor ganado e informes. Ver [Valor ganado](valor-ganado.md).
* **Libro de Excel** (`Formatos_Monitoreo_Control_TSP_ColorrectalAI.xlsx`) — consolida los datos del equipo y cubre seguimiento de requisitos, registro de cambios, ejecución de pruebas, riesgos, métricas de producto y listas de verificación.
* **Trello, GitHub y Moodle** — evidencia del estado de cada tarea y de sus revisiones.
