# Resultados esperados y conclusiones

## Resultado principal

Un **módulo web funcional de ColorrectalAI** integrado al ecosistema ONCO-AI_USC 2026 B, que permita cargar o procesar una imagen de endoscopia y presentar una salida experimental con la región de interés, la clasificación y el nivel de confianza.

## Resultados específicos

* Dataset seleccionado, documentado y preparado para experimentación.
* Pipeline reproducible de preprocesamiento, entrenamiento, validación y prueba.
* Modelo baseline de detección/segmentación.
* API o servicio de inferencia que conecte el modelo con la plataforma web.
* Interfaz web para visualizar imágenes y resultados.
* Registro de métricas y experimentos.
* Evaluación de clasificación/detección y, si aplica, segmentación.
* Evaluación de calibración mediante Brier Score y/o ECE.
* Medición de latencia y errores del sistema.
* Documentación técnica y guía de reproducción.

## Indicadores de evaluación

| Dimensión | Métrica | Propósito |
| --- | --- | --- |
| Clasificación | Sensibilidad, especificidad, F1, ROC-AUC, PR-AUC | Medir desempeño del modelo |
| Detección | mAP y métricas de localización | Evaluar identificación de lesiones |
| Segmentación | Dice, IoU | Evaluar delimitación de ROI |
| Calibración | Brier Score, ECE | Evaluar confiabilidad de la confianza |
| Sistema | Latencia, errores, disponibilidad | Evaluar calidad operacional |
| Usabilidad | SUS u otro instrumento validado | Evaluar experiencia de usuario |

## Supuestos del proyecto

Condiciones de trabajo que deben validarse durante el desarrollo; los que no se cumplan pueden convertirse en riesgos.

* Se dispondrá de un dataset público y desidentificado con calidad suficiente para experimentos de detección.
* La licencia del dataset permitirá su uso con fines académicos.
* El equipo contará con recursos computacionales suficientes para entrenar y ejecutar al menos un modelo baseline.
* Las herramientas de software serán accesibles dentro del presupuesto académico, con costo cercano a cero.
* Los integrantes tendrán disponibilidad para cumplir las actividades del semestre.
* La integración entre el modelo y la plataforma web podrá hacerse mediante una API o mecanismo equivalente.
* El proyecto mantendrá su carácter experimental y educativo y no será presentado como dispositivo médico.
* La documentación del pipeline permitirá reproducir los experimentos principales.

## Conclusiones

ColorrectalAI es técnicamente viable como módulo académico si se mantiene un alcance controlado, se usan datos apropiados y se documentan con rigor las etapas de preparación, entrenamiento, evaluación e integración. El éxito del proyecto no debe medirse solo por la exactitud del modelo, sino por la capacidad de construir un producto reproducible que permita estudiar **detección, confianza, explicabilidad, rendimiento e interacción con la IA**.
