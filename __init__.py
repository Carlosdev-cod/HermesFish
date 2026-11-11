import os
import sys
from pathlib import Path

PLUGIN_DIR = Path(__file__).resolve().parent
AGENTS_DIR = PLUGIN_DIR / "agents"
SKILLS_DIR = PLUGIN_DIR / "skills"

def egm_review(target_file: str, step: str = "interactive") -> str:
    """Ejecuta el protocolo de revisión EGM (Goldfish Review) sobre un archivo de diseño o especificación.

    Args:
        target_file: Ruta absoluta o relativa al documento de diseño (Markdown).
        step: Modo de ejecución: 'interactive', 'uninterrupted', 'feature_spec', o 'implementation'.
    """
    path = Path(target_file).expanduser()
    if not path.is_absolute():
        path = (Path.cwd() / path).resolve()

    if not path.exists():
        return f"Error: No se encontró el archivo de diseño en '{path}'."

    content_preview = path.read_text(encoding="utf-8", errors="replace")[:500]

    return (
        f"Iniciando protocolo HermesFish (Goldfish Review) para: {path}\n"
        f"Modo seleccionado: {step}\n"
        f"Archivo detectado ({len(content_preview)} caracteres de muestra):\n"
        f"--------------------------------------------------\n"
        f"{content_preview}...\n"
        f"--------------------------------------------------\n"
        f"Para completar la revisión multi-agente, el orquestador principal debe invocar "
        f"a los subagentes evaluadores (Zoom-Out, Comprehension, Design Critic, Implementation Readiness) "
        f"usando `delegate_task` en contextos limpios basándose en las plantillas de `agents/`."
    )

def egm_drift_report(docs_dir: str = "docs/designs") -> str:
    """Compara los documentos de especificación contra el código fuente real para detectar drift arquitectónico.

    Args:
        docs_dir: Directorio donde se ubican las especificaciones o documentos de diseño.
    """
    path = Path(docs_dir).expanduser()
    if not path.is_absolute():
        path = (Path.cwd() / path).resolve()

    if not path.exists():
        return f"Aviso: La ruta de documentos '{path}' no existe en el directorio de trabajo."

    doc_files = list(path.glob("**/*.md"))
    if not doc_files:
        return f"No se encontraron archivos Markdown en '{path}' para analizar."

    summary = [f"HermesFish Drift Report: Analizando {len(doc_files)} documento(s) en {path}:"]
    for doc in doc_files:
        summary.append(f"- {doc.name} ({doc.stat().st_size} bytes)")

    summary.append(
        "\nInstrucción de análisis: Comparar cada componente referenciado en las specs con el árbol "
        "de archivos del repositorio para identificar APIs cambiadas, endpoints deprecados o módulos no implementados."
    )
    return "\n".join(summary)

def egm_brainstorm(topic: str) -> str:
    """Inicia una sesión estructurada de brainstorming arquitectónico antes de redactar código o specs.

    Args:
        topic: Tema, problema o arquitectura a explorar.
    """
    return (
        f"Iniciando sesión HermesFish Brainstorming para: '{topic}'.\n"
        f"1. El agente 'Elephant' mantiene el hilo contextual y define los requerimientos.\n"
        f"2. Subagentes 'Goldfish' evalúan riesgos, suposiciones no declaradas y alternativas técnicas.\n"
        f"3. Las decisiones acordadas se sintetizan en un borrador de conceptos."
    )

def register(ctx):
    """Punto de entrada nativo para Hermes Agent."""
    ctx.register_tool(
        name="egm_review",
        toolset="hermesfish",
        description="Revisa y valida documentos de arquitectura y especificaciones mediante el protocolo EGM Goldfish.",
        schema={
            "type": "object",
            "properties": {
                "target_file": {
                    "type": "string",
                    "description": "Ruta al archivo Markdown de especificación o diseño técnico."
                },
                "step": {
                    "type": "string",
                    "description": "Fase o modo de revisión (ej. 'interactive', 'uninterrupted').",
                    "default": "interactive"
                }
            },
            "required": ["target_file"]
        },
        handler=egm_review
    )

    ctx.register_tool(
        name="egm_drift_report",
        toolset="hermesfish",
        description="Detecta desviaciones (drift) entre la documentación de diseño y el código fuente real del proyecto.",
        schema={
            "type": "object",
            "properties": {
                "docs_dir": {
                    "type": "string",
                    "description": "Ruta a la carpeta de especificaciones o diseños (por defecto 'docs/designs').",
                    "default": "docs/designs"
                }
            }
        },
        handler=egm_drift_report
    )

    ctx.register_tool(
        name="egm_brainstorm",
        toolset="hermesfish",
        description="Inicia un brainstorming guiado con evaluación de compensaciones y alternativas técnicas.",
        schema={
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "Tema, arquitectura o feature a debatir."
                }
            },
            "required": ["topic"]
        },
        handler=egm_brainstorm
    )
