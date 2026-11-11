# Referente teórico

## Inteligencia artificial

Técnicas computacionales orientadas a resolver tareas asociadas al razonamiento, reconocimiento de patrones, aprendizaje o toma de decisiones. En ColorrectalAI, la IA se usa como componente de análisis de imágenes y **no como sustituto de la decisión médica**.

## Aprendizaje automático y aprendizaje profundo

El aprendizaje automático construye modelos que identifican patrones a partir de datos. El aprendizaje profundo usa redes neuronales de múltiples capas para aprender representaciones complejas. En imágenes médicas se aplican a clasificación, detección y segmentación.

## Visión por computador

Busca extraer información significativa de imágenes y videos. En el proyecto es la base tecnológica para transformar una imagen endoscópica en una salida estructurada con **localización, clasificación experimental y confianza**.

## Detección de objetos y YOLO

La detección de objetos identifica instancias relevantes y localiza su posición mediante regiones delimitadoras. La familia **YOLO (You Only Look Once)** realiza la detección en una sola etapa, lo que favorece el procesamiento eficiente. ONCO-AI_USC 2026 B establece YOLO/segmentación como enfoque para ColorrectalAI.

## Segmentación y región de interés

La segmentación delimita los píxeles que pertenecen a una estructura o lesión. La **región de interés (ROI)** es el área considerada relevante por el modelo. La salida de ColorrectalAI debe mostrar dónde se encontró la región relevante, no solo un resultado textual.

## Explicabilidad de IA

Proporciona información para comprender por qué un modelo genera determinada salida. Visualizar las regiones relevantes complementa la predicción y facilita el análisis académico del comportamiento del modelo.

## Confianza y calibración

La confianza de un modelo no debe asumirse como una probabilidad fiable. La calibración estudia si los niveles de confianza corresponden con la frecuencia real de aciertos. Se usan **Brier Score** y **Expected Calibration Error (ECE)**.

## Métricas de evaluación

| Dimensión | Métricas |
| --- | --- |
| Clasificación | Sensibilidad, especificidad, F1, ROC-AUC, PR-AUC |
| Detección | mAP y métricas de localización |
| Segmentación | Dice, IoU |
| Calibración | Brier Score, ECE |
| Sistema | Latencia, errores, disponibilidad |

Estas métricas evalúan distintas dimensiones del producto y evitan reducir su calidad a *accuracy*.
