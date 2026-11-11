# Acta de inicio

{% hint style="success" %}
**Estado: Terminado** · ID: **C-01** · Hito 002 · Versión vigente: **v1.0 corregida (04-10-2026)** · Responsable: System Force
{% endhint %}

Acta de Constitución del Proyecto (plantilla PM² OPM2-03 v3.0.1). Fue aprobada por el Propietario del Proyecto (hito 002, 13 sep 2026) y luego ajustada; la [versión corregida](../trazabilidad/acta-inicio-corregida.md) está en Trello. Los riesgos del acta (sección 3.8) están en el [Plan para la dirección del proyecto](../planeacion/plan-direccion.md#riesgos).

## Declaración del alcance

Desarrollar un módulo web experimental, integrado al ecosistema ONCO-AI_USC 2026 B, que identifique regiones de interés en imágenes de endoscopia mediante visión por computador y un modelo de detección/segmentación (YOLO), presente una clasificación experimental con su nivel de confianza y permita evaluar su desempeño técnico en un contexto académico y reproducible, **sin validez clínica**.

## Dentro del alcance

* Selección, documentación y preparación de un dataset público y desidentificado de imágenes de endoscopia (ficha del dataset, licencia, población, etiquetas, versión, criterios de inclusión/exclusión y posibles sesgos).
* Pipeline reproducible de visión por computador: control de calidad, normalización, redimensionamiento, delimitación de ROI, aumento de datos, partición por paciente, entrenamiento, validación y prueba.
* Modelo baseline de detección/segmentación basado en YOLO.
* API o servicio de inferencia que conecta el modelo con la plataforma web.
* Interfaz web para cargar una imagen y visualizar la ROI, la clasificación experimental y el nivel de confianza, con aviso visible de uso experimental.
* Evaluación del modelo y del sistema: clasificación, detección y segmentación; calibración (Brier Score y/o ECE); latencia y errores; usabilidad (SUS u otro instrumento validado).
* Registro de métricas y experimentos, documentación técnica y guía de reproducción.

## Fuera del alcance

* Recomendaciones terapéuticas o presentar el resultado con validez clínica; el sistema no sustituye el criterio de profesionales de la salud.
* Uso de historias clínicas reales o de datos identificables de pacientes.
* Presentar o prestar el módulo como servicio asistencial, de telesalud o telemedicina (Resolución 2654 de 2019), o como dispositivo médico autorizado.
* Implementación clínica del módulo.

## Criterios de éxito

{% hint style="info" %}
El éxito no se mide únicamente por la exactitud del modelo, sino por la capacidad de construir un producto reproducible.
{% endhint %}

**Criterios críticos** (su ausencia impide considerar el proyecto exitoso):

* El módulo web permite cargar o procesar una imagen de endoscopia y presenta la región de interés, la clasificación experimental y el nivel de confianza.
* La interfaz incluye una advertencia visible de que el resultado es un experimento académico y no sustituye el criterio de profesionales de la salud.
* Solo se usan datasets públicos, anonimizados y desidentificados, con licencia cumplida y procedencia registrada.
* La partición entrenamiento/validación/prueba se hace por paciente cuando la estructura de los datos lo permite.
* Los experimentos principales pueden reproducirse a partir de la documentación (README, entorno, scripts y versión/tag).

**Criterios del producto:**

* Resultados reportados con las métricas definidas: clasificación (sensibilidad, especificidad, F1, ROC-AUC, PR-AUC), detección (mAP), segmentación (Dice, IoU) y calibración (Brier Score y/o ECE).
* Latencia y errores del sistema medidos y registrados.
* Usabilidad evaluada con SUS u otro instrumento validado.
* Casos de prueba ejecutados con resultados documentados.
* Costo del proyecto cercano a cero.

## Entregables

| ID | Entregable | Descripción |
| --- | --- | --- |
| E01 | Dataset documentado | Dataset público y desidentificado, preparado para experimentación, con ficha (procedencia, licencia, población, etiquetas, versión, criterios y sesgos). |
| E02 | Pipeline reproducible | Scripts o notebooks de control de calidad, normalización, ROI, aumento de datos, partición por paciente, entrenamiento, validación y prueba, con logs. |
| E03 | Modelo baseline YOLO | Modelo de detección/segmentación entrenado, con sus parámetros, versión y métricas. |
| E04 | API de inferencia | Servicio que recibe una imagen y devuelve ROI, clasificación experimental y nivel de confianza. |
| E05 | Interfaz web | Módulo web para cargar imágenes y visualizar ROI, clasificación y confianza, integrado a ONCO-AI_USC 2026 B. |
| E06 | Informe de evaluación y registro de experimentos | Métricas de clasificación, detección/segmentación, calibración, latencia, errores y usabilidad. |
| E07 | Pruebas | Casos de prueba y resultados de su ejecución. |
| E08 | Documentación técnica y guía de reproducción | README, configuración del entorno y versión/tag del repositorio. |
| E09 | Aviso de uso experimental | Advertencia visible en la interfaz de que el resultado es un experimento académico. |
