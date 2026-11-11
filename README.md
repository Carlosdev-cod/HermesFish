<p align="center">
  <img src="assets/icon.svg" width="120" height="120" alt="HermesFish Logo">
</p>

<h1 align="center">HermesFish (Elephant-Goldfish Model para Hermes Agent)</h1>

<p align="center">
  <strong>Diseña con la memoria de un elefante. Revisa con la mirada fresca de un pez dorado.</strong>
</p>

<p align="center">
  <em>Plugin nativo y suite de habilidades multi-agente para arquitectura, diseño técnico y revisión de código en Hermes Agent, Claude Code, Codex y Antigravity.</em>
</p>

---

## ¿Qué es HermesFish?

**HermesFish** es una adaptación y extensión directa para **Hermes Agent** del marco de trabajo *Elephant-Goldfish Model (EGM)* desarrollado originalmente por Google.

Al construir software con agentes de IA, las conversaciones largas tienden a acumular sesgos, acuerdos implícitos no comprobados o "ceguera de taller". HermesFish resuelve esto separando las responsabilidades en dos roles claros:

1. **Elephant (El Elefante)**: El agente principal con todo el contexto del repositorio y la conversación, responsable de explorar ideas, entender requerimientos y redactar la especificación técnica.
2. **Goldfish (El Pez Dorado)**: Subagentes independientes lanzados en contextos completamente limpios (sin historial previo ni sesgos) para evaluar críticamente el documento, detectar puntos ciegos, suposiciones no justificadas y riesgos de implementación.

---

## Compatibilidad de Primera Clase con Hermes Agent

A diferencia de los paquetes tradicionales pensados solo para Claude o Codex, **HermesFish incluye soporte nativo para Hermes Agent**:

- **Plugin Nativo de Hermes**: Cuenta con `plugin.yaml` y su punto de entrada en Python (`__init__.py`).
- **Herramientas de Agente**: Expone herramientas nativas (`egm_review`, `egm_drift_report`, `egm_brainstorm`).
- **Orquestación Limpia**: Aprovecha la herramienta `delegate_task` de Hermes para ejecutar evaluadores en paralelo con aislamiento real de contexto.
- **Retrocompatibilidad**: Conserva total compatibilidad como suite de skills (`SKILL.md`) para Claude Code, OpenAI Codex y Google Antigravity.

---

## Instalación

### En Hermes Agent (Plugin Nativo)

Puedes clonarlo directamente en tu carpeta de plugins de Hermes:

```bash
# 1. Clonar en la carpeta de plugins de Hermes
git clone https://github.com/Carlosdev-cod/HermesFish ~/.hermes/plugins/hermesfish

# 2. Habilitar el plugin en Hermes
hermes plugins enable hermesfish
```

O como suite de habilidades (skills):

```bash
hermes skills install Carlosdev-cod/HermesFish/skills/egm-review
```

### En otros entornos

* **Antigravity CLI**:
  ```bash
  agy plugin install https://github.com/Carlosdev-cod/HermesFish
  ```
* **Claude Code**:
  ```bash
  claude plugin marketplace add Carlosdev-cod/HermesFish
  claude plugin install egm@egm
  ```
* **Codex CLI**:
  ```bash
  codex plugin marketplace add Carlosdev-cod/HermesFish
  codex plugin add egm@egm
  ```

---

## Flujo de Trabajo

### 1. Explorar la idea (Brainstorming)
Antes de escribir una sola línea de código, analiza requerimientos y compensaciones:
```text
/egm-brainstorm Diseñar arquitectura de cola de mensajes para sincronización offline
```
El agente explorará el problema contigo y generará un resumen de conceptos (`concepts_brief.md`).

### 2. Redactar la especificación (Draft)
Convierte el brief en un diseño técnico completo y detallado:
```text
/egm-draft
```
Genera `design_draft.md` solicitando tu retroalimentación en puntos críticos.

### 3. Revisión Goldfish con ojos frescos (Review)
Ejecuta la revisión independiente en 5 fases rigurosas:
```text
/egm-review docs/designs/nueva_feature.md
```
Los evaluadores analizan:
- **Zoom Out**: Alineación de alto nivel y necesidad real del componente.
- **Comprehension**: Claridad y eliminación de ambigüedades.
- **Design Critique**: Suposiciones no probadas, cuellos de botella y fallas potenciales.
- **Implementation Readiness**: Si los detalles son suficientes para implementar sin inventar nada.

### 4. Detección de Desviación (Drift Report)
Verifica periódicamente si el código fuente ha divergido de la documentación arquitectónica:
```text
/egm-drift-report docs/designs/
```

---

## Habilidades y Personas Incluidas

* `egm-review`: Orquestador del protocolo de revisión Goldfish.
* `egm-brainstorm`: Sesión interactiva de ideación arquitectónica.
* `egm-draft`: Redacción estructurada de especificaciones técnicas.
* `egm-drift-report`: Detección de código desalineado con las especificaciones.
* `egm-resolve`: Resolución metódica de discrepancias post-revisión.
* `egm-review-loop`: Bucle automatizado de diseño y revisión.
* `egm-bootstrap`: Inicialización de estándares arquitectónicos en repositorios nuevos.

---

## Licencia

Distribuido bajo licencia **Apache-2.0**, respetando el trabajo original de Google y extendido para el ecosistema de agentes abiertos con **Hermes Agent**.
