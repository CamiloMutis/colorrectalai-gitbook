# Riesgos y supuestos

## Registro de riesgos

Riesgos R01 a R08 tomados del Acta de Constitución (sección 3.8). El líder del equipo los revisa cada semana en el formato ITL (probabilidad e impacto de 1 a 5; exposición = P × I).

| ID | Riesgo | Estado |
| --- | --- | --- |
| R01 | Dataset insuficiente o con licencia que no permita su uso académico | Abierto |
| R02 | Recursos computacionales o herramientas insuficientes dentro del presupuesto académico | Abierto |
| R03 | Fuga de información entre entrenamiento y prueba | Abierto |
| R04 | Baja disponibilidad del equipo durante el semestre | Abierto |
| R05 | Dificultades para integrar el modelo con la API y la interfaz web | Abierto |
| R06 | Que el resultado se interprete como clínicamente válido o que el módulo se presente como dispositivo médico | Abierto |
| R07 | Problema de generalización, sesgo o confianza mal calibrada del modelo | Abierto |
| R08 | Documentación insuficiente para reproducir los experimentos | Abierto |

Estrategias de respuesta posibles: **Evitar / Aceptar / Reducir / Transferir** (amenazas) y **Explotar / Aceptar / Mejorar / Compartir** (oportunidades).

## Supuestos

Condiciones de trabajo de la formulación inicial que deben validarse durante el desarrollo; los que no se cumplan pueden convertirse en riesgos.

* Se dispondrá de un dataset público y desidentificado con calidad suficiente para experimentos de detección.
* La licencia del dataset permitirá su uso con fines académicos.
* El equipo contará con recursos computacionales suficientes para entrenar y ejecutar al menos un modelo baseline.
* Las herramientas de software serán accesibles dentro del presupuesto académico, con costo cercano a cero.
* Los integrantes tendrán disponibilidad para cumplir las actividades del semestre.
* La integración entre el modelo y la plataforma web podrá hacerse mediante una API o mecanismo equivalente.
* El proyecto mantendrá su carácter experimental y educativo y no será presentado como dispositivo médico.
* La documentación del pipeline permitirá reproducir los experimentos principales.
