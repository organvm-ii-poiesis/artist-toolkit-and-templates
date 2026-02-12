"""Tests for the template engine."""

import pytest

from src.template_engine import Template, TemplateLibrary, TemplateVariable


def _sample_template(**overrides) -> Template:
    defaults = {
        "name": "grant-application",
        "description": "Standard grant application template",
        "category": "grants",
        "content": "Project: {{project_name}}
By: {{author}}
Optional: {{notes}}",
        "variables": [
            TemplateVariable(name="project_name", description="Project name", required=True),
            TemplateVariable(name="author", description="Author name", required=True),
            TemplateVariable(name="notes", description="Additional notes", required=False, default="N/A"),
        ],
    }
    defaults.update(overrides)
    return Template(**defaults)


class TestTemplate:
    def test_required_variables(self):
        t = _sample_template()
        assert len(t.required_variables) == 2

    def test_optional_variables(self):
        t = _sample_template()
        assert len(t.optional_variables) == 1

    def test_validate_all_present(self):
        t = _sample_template()
        missing = t.validate({"project_name": "ORGAN", "author": "Test"})
        assert missing == []

    def test_validate_missing_required(self):
        t = _sample_template()
        missing = t.validate({"author": "Test"})
        assert "project_name" in missing

    def test_render_success(self):
        t = _sample_template()
        result = t.render({"project_name": "ORGAN", "author": "Test"})
        assert "Project: ORGAN" in result
        assert "By: Test" in result
        assert "Optional: N/A" in result

    def test_render_with_optional(self):
        t = _sample_template()
        result = t.render({"project_name": "ORGAN", "author": "Test", "notes": "Important"})
        assert "Optional: Important" in result

    def test_render_missing_raises(self):
        t = _sample_template()
        with pytest.raises(ValueError, match="Missing required"):
            t.render({"author": "Test"})


class TestTemplateLibrary:
    def test_add_and_get(self):
        lib = TemplateLibrary()
        lib.add(_sample_template())
        assert lib.get("grant-application") is not None

    def test_get_not_found(self):
        lib = TemplateLibrary()
        assert lib.get("nonexistent") is None

    def test_by_category(self):
        lib = TemplateLibrary()
        lib.add(_sample_template(category="grants"))
        lib.add(_sample_template(name="other", category="proposals"))
        assert len(lib.by_category("grants")) == 1

    def test_categories(self):
        lib = TemplateLibrary()
        lib.add(_sample_template(category="grants"))
        lib.add(_sample_template(name="other", category="proposals"))
        assert lib.categories == ["grants", "proposals"]

    def test_search(self):
        lib = TemplateLibrary()
        lib.add(_sample_template())
        results = lib.search("grant")
        assert len(results) == 1
