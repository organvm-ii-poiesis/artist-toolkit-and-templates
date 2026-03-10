"""Template engine for generating project documents."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class TemplateVariable:
    """A variable that can be filled in a template."""
    name: str
    description: str
    required: bool = True
    default: str = ""


@dataclass
class Template:
    """A document template with fillable variables."""
    name: str
    description: str
    category: str
    content: str
    variables: list[TemplateVariable] = field(default_factory=list)

    @property
    def required_variables(self) -> list[TemplateVariable]:
        return [v for v in self.variables if v.required]

    @property
    def optional_variables(self) -> list[TemplateVariable]:
        return [v for v in self.variables if not v.required]

    def validate(self, values: dict[str, str]) -> list[str]:
        """Check if all required variables are provided. Returns list of missing variable names."""
        missing = []
        for var in self.required_variables:
            if var.name not in values or not values[var.name]:
                missing.append(var.name)
        return missing

    def render(self, values: dict[str, str]) -> str:
        """Render the template with provided values."""
        missing = self.validate(values)
        if missing:
            raise ValueError(f"Missing required variables: {', '.join(missing)}")

        result = self.content
        for var in self.variables:
            placeholder = "{{" + var.name + "}}"
            value = values.get(var.name, var.default)
            result = result.replace(placeholder, value)
        return result


@dataclass
class TemplateLibrary:
    """A collection of templates organized by category."""
    templates: list[Template] = field(default_factory=list)

    def add(self, template: Template) -> None:
        self.templates.append(template)

    def by_category(self, category: str) -> list[Template]:
        return [t for t in self.templates if t.category == category]

    def get(self, name: str) -> Template | None:
        for t in self.templates:
            if t.name == name:
                return t
        return None

    @property
    def categories(self) -> list[str]:
        return sorted(set(t.category for t in self.templates))

    def search(self, query: str) -> list[Template]:
        q = query.lower()
        return [
            t for t in self.templates
            if q in t.name.lower() or q in t.description.lower()
        ]
