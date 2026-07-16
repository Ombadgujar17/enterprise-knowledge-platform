from pathlib import Path

from app.graph.builder import build_graph


def main() -> None:
    graph = build_graph()

    output_dir = Path("docs/architecture")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "langgraph_workflow.png"

    image = graph.get_graph().draw_mermaid_png()

    output_path.write_bytes(image)

    print(f"✅ Graph saved to: {output_path}")


if __name__ == "__main__":
    main()