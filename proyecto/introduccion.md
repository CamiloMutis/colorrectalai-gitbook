# Introducción

La inteligencia artificial (IA) aplicada al análisis de imágenes médicas ha adquirido relevancia como herramienta de apoyo en diferentes áreas de la medicina. En el campo de la endoscopia digestiva, los sistemas de **detección asistida por computador (CADe)** se han estudiado especialmente para identificar pólipos y neoplasias colorrectales.

Una revisión sistemática y metaanálisis de ensayos clínicos aleatorizados que reunió **33 estudios y 27.404 pacientes** encontró una reducción significativa de las tasas de pólipos y adenomas omitidos con colonoscopia asistida por IA, aunque también señaló la necesidad de continuar estudiando sus beneficios a largo plazo, costos y posibles falsos positivos (Lou et al., 2023).

Estos resultados muestran el potencial de la IA como mecanismo de asistencia, pero no significan que un modelo experimental pueda reemplazar el criterio del especialista. La literatura también ha identificado riesgos asociados con sobre-detección, resección innecesaria de lesiones no neoplásicas, sesgos, problemas de generalización y confianza inadecuadamente calibrada. Por ello, el desarrollo de soluciones de IA médica requiere considerar no solo el desempeño algorítmico, sino también la trazabilidad, explicabilidad, interacción humano–IA y condiciones de uso.

## ColorrectalAI dentro de ONCO-AI_USC 2026 B

ColorrectalAI es uno de los módulos de la línea **Clínica AI Web** del ecosistema ONCO-AI_USC 2026 B. El proyecto general propone integrar visión por computador, aprendizaje profundo, análisis de imágenes médicas, IA y simulación gamificada en una plataforma web orientada a investigación y educación.

ColorrectalAI se enfoca específicamente en **imágenes de endoscopia** y contempla el uso de modelos de detección/segmentación, particularmente **YOLO**, para:

* identificar regiones de interés (ROI),
* presentar una clasificación experimental, y
* mostrar el nivel de confianza del modelo.

## Propósito

Desarrollar un artefacto académico reproducible que permita estudiar el desempeño técnico de un modelo de visión por computador aplicado a imágenes de endoscopia. El sistema se plantea como una herramienta experimental y educativa: no pretende realizar diagnóstico médico, no sustituye el criterio de profesionales de la salud y no se presenta como dispositivo médico autorizado.

## Relevancia para la Ingeniería de Sistemas

El proyecto integra en un mismo producto ingeniería de software, gestión de proyectos, inteligencia artificial, procesamiento de imágenes, trazabilidad y evaluación. ColorrectalAI no se limita a entrenar un modelo: busca construir un flujo reproducible que relacione **datos, modelo, detección, explicación, confianza y resultados**.
