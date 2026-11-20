from strictdoc.core.project_config import ProjectConfig


def create_config() -> ProjectConfig:
    return ProjectConfig(
        project_title="Brake controller requirements",
        include_doc_paths=["reqs/**"],
    )
