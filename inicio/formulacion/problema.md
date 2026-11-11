# Planteamiento del problema

La colonoscopia es un procedimiento en el que la identificación visual de lesiones depende, entre otros factores, de las condiciones de la imagen, la calidad de la exploración y la experiencia del especialista. La literatura sobre sistemas CADe muestra que la asistencia de IA puede mejorar la detección de determinadas lesiones, pero también evidencia limitaciones y posibles efectos no deseados: incrementos en la detección de pólipos y adenomas pequeños junto con preocupaciones por falsos positivos y sobre-detección (Barua et al., 2021; Lou et al., 2023).

Desde la perspectiva tecnológica, el problema no consiste únicamente en determinar si una imagen contiene una lesión. Un sistema de apoyo debe ser capaz de:

1. procesar la imagen,
2. localizar visualmente la región relevante,
3. producir una clasificación experimental, y
4. comunicar una medida de confianza.

Además, el desempeño debe evaluarse con métricas apropiadas y con una separación adecuada entre datos de entrenamiento, validación y prueba para reducir el riesgo de fuga de información.

El documento general de ONCO-AI_USC 2026 B identifica problemas de **generalización, sesgo, calibración, explicabilidad e interpretabilidad** al transferir modelos de IA desde conjuntos controlados hacia escenarios reales, y establece que los resultados deben estudiarse como evidencia experimental y no como diagnóstico clínico.

## Pregunta de ingeniería

{% hint style="info" %}
¿Cómo diseñar e implementar un módulo web experimental basado en visión por computador que permita detectar y señalar regiones de interés en imágenes de endoscopia, presentar una clasificación y nivel de confianza, y evaluar reproduciblemente su desempeño técnico dentro de un contexto educativo?
{% endhint %}

## Pertinencia e impacto

El proyecto permite estudiar de manera controlada la integración entre un modelo de IA y una aplicación web, documentando el pipeline de datos, entrenamiento, validación y evaluación. Su impacto esperado es principalmente **académico**: aportar un artefacto reproducible que permita analizar capacidades y limitaciones de la IA aplicada a imágenes médicas sin atribuirle funciones diagnósticas que excedan su alcance.
