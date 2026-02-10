[![ORGAN-II: Poiesis](https://img.shields.io/badge/ORGAN--II-Poiesis-6a1b9a?style=flat-square)](https://github.com/organvm-ii-poiesis)

# Artist Toolkit and Templates

**Reusable creative infrastructure for artists working at the intersection of performance, installation, generative systems, and technology-mediated art.**

> *"A template is not a constraint — it is a scaffold that holds space for the work you haven't made yet."*

---

## Table of Contents

- [Purpose](#purpose)
- [Why This Exists](#why-this-exists)
- [Conceptual Approach](#conceptual-approach)
- [Repository Structure](#repository-structure)
- [Template Categories](#template-categories)
  - [Artist Prospecting](#artist-prospecting)
  - [Deployment Playbooks](#deployment-playbooks)
  - [Grant Resources](#grant-resources)
  - [General Templates](#general-templates)
- [Template Philosophy](#template-philosophy)
- [Theory Implemented from ORGAN-I](#theory-implemented-from-organ-i)
- [Integration with the ORGAN-II Ecosystem](#integration-with-the-organ-ii-ecosystem)
- [Planned Content and Roadmap](#planned-content-and-roadmap)
- [Migration Note](#migration-note)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Purpose

The art world runs on invisible infrastructure. Behind every successful grant application, every smooth festival load-in, every productive collaboration, there are documents — proposals, budgets, riders, agreements, project plans — that artists write and rewrite from scratch, project after project, year after year. The administrative burden of a creative practice is enormous, and it falls disproportionately on independent artists who lack institutional support.

**artist-toolkit-and-templates** is a response to that problem. It provides a curated library of reusable, field-tested templates and playbooks designed specifically for artists working with technology, performance, installation, and generative systems. These are not generic business templates adapted for creative use. They are documents born from the specific needs of artists who build interactive installations in unconventional venues, who write grant proposals for work that doesn't fit neatly into traditional categories, who negotiate collaboration agreements for projects that blur the line between software and sculpture.

This repository serves three audiences simultaneously:

1. **Working artists** who need practical documents they can adapt immediately — a festival rider that accounts for real-time audiovisual systems, a budget checklist that includes server costs alongside material costs, a project plan template that accommodates iterative creative processes rather than linear production timelines.

2. **Emerging practitioners** who are building their first professional infrastructure — artist bios written for different contexts, CVs structured for the art world rather than the tech industry, prospecting letters that communicate the value of technology-mediated art to curators and venue operators who may not speak that language.

3. **The broader ORGAN system** — this toolkit feeds directly into the creative pipelines defined by [metasystem-master](https://github.com/organvm-ii-poiesis/metasystem-master) and other ORGAN-II repositories, providing the professional scaffolding that surrounds and supports the artistic work itself.

## Why This Exists

Every artist maintains a private folder of templates — proposal boilerplates, budget spreadsheets, technical riders cobbled together from previous projects. These documents represent years of accumulated knowledge about how to navigate the practical side of creative practice. But they remain private, fragmented, and often poorly maintained because maintaining administrative documents is nobody's idea of a good time.

The insight behind this repository is that **professional creative infrastructure is a commons problem**. When every artist solves the same administrative challenges independently, the collective effort is enormous and the results are uneven. Some artists have excellent proposals and terrible riders. Others have meticulous budgets but no collaboration agreements. The quality of an artist's administrative documents often reflects their institutional access and mentorship networks more than the quality of their work.

By open-sourcing a comprehensive toolkit — one that reflects the specific needs of technology-mediated art practice — we lower the barrier to professional creative work. An artist working on their first interactive installation can start with a festival rider template that already accounts for power requirements, network connectivity, projection mapping specifications, and real-time system monitoring. They don't need to learn these considerations the hard way.

This is infrastructure work in the truest sense: invisible when it works, catastrophic when it fails, and most valuable when it is shared.

## Conceptual Approach

### Templates as Creative Scaffolding

The central design principle of this toolkit is that **templates should enable creative work, not constrain it**. A good template is like architectural scaffolding — it provides structure and support during construction, but the building it helps create can take any form. The scaffolding is not the architecture.

This means our templates are deliberately structured as frameworks rather than fill-in-the-blank forms. Each template includes:

- **Structural guidance** — the sections and information that stakeholders (funders, venues, collaborators) expect to see, organized in the order they expect to find it.
- **Contextual notes** — explanations of why each section exists, what purpose it serves, and how to adapt it for different situations. These notes are written as comments that can be removed from the final document.
- **Decision points** — explicit moments where the template asks the artist to make a choice rather than accepting a default. This prevents the homogenization that can happen when everyone uses the same template without thinking.
- **Examples from practice** — where appropriate, concrete examples drawn from technology-mediated art practice that illustrate how to translate artistic concepts into professional language.

### The Professional-Artistic Voice

One of the persistent challenges in technology-mediated art is communicating across discourse communities. The language that describes a generative audiovisual performance to a fellow artist is different from the language that describes it to a grant panel, which is different from the language that describes it to a venue's technical director. Each audience needs different information, framed in different terms, with different assumptions about shared knowledge.

Our templates are designed to help artists navigate these translations. The grant proposal template, for example, includes guidance on how to describe technical systems in terms that grant reviewers can evaluate — foregrounding artistic intent and cultural significance while providing enough technical detail to demonstrate feasibility. The festival rider template translates between artistic requirements and technical specifications, helping venue staff understand not just what equipment is needed but why.

This is not about dumbing things down or dressing things up. It is about effective communication — meeting each audience where they are and giving them what they need to say yes.

## Repository Structure

```
artist-toolkit-and-templates/
├── README.md
├── artist-prospecting/
│   ├── artist-bio-template.md        # Adaptable bio for different contexts
│   ├── cv-template.md                # Art-world CV structure
│   └── prospecting-letter-template.md # Outreach to curators/venues
├── deployment-playbooks/
│   ├── documentation-requirements.md  # What to document before, during, after
│   ├── festival-rider.md             # Technical rider for festival/venue contexts
│   └── indie-venue-setup.md          # Setup guide for non-traditional spaces
├── grant-resources/
│   ├── budget-checklist.md           # Comprehensive budget line items
│   ├── funding-landscape.md          # Overview of funding sources
│   └── proposal-template.md          # Grant proposal framework
├── templates/
│   ├── collaboration-agreement.md    # Terms for multi-artist projects
│   └── project-plan.md              # Iterative project planning framework
└── example-projects/
    └── .gitkeep                      # Planned: worked examples
```

## Template Categories

### Artist Prospecting

The prospecting suite addresses the fundamental challenge of self-presentation in creative practice. Most artists hate writing about themselves — it feels reductive, promotional, or both. These templates reframe self-presentation as a craft skill that can be practiced and refined, just like any other aspect of artistic practice.

**`artist-bio-template.md`** — A modular bio framework designed for adaptation across contexts. Rather than a single bio, this template helps artists maintain a set of interchangeable components (practice description, recent work, technical capabilities, conceptual framework) that can be assembled into bios of different lengths and emphases. A 50-word bio for a festival program requires different content than a 500-word bio for a grant application, but both should be drawn from the same source material.

**`cv-template.md`** — An art-world CV structure that accounts for the hybrid nature of technology-mediated practice. The traditional art CV (exhibitions, collections, publications) doesn't serve artists whose work spans software development, performance, installation, and research. This template provides a structure that presents technical and artistic achievements as integrated practice rather than separate careers.

**`prospecting-letter-template.md`** — A framework for cold outreach to curators, venue operators, festival directors, and other gatekeepers. The template addresses the specific challenge of introducing technology-mediated art to people who may be unfamiliar with the medium, providing language that connects technical capabilities to artistic and audience experiences.

### Deployment Playbooks

Deployment playbooks bridge the gap between artistic vision and physical reality. They address the practical logistics of presenting technology-mediated art in the real world — a domain where things go wrong in predictable ways that can be anticipated and mitigated.

**`documentation-requirements.md`** — A checklist of what to document before, during, and after a deployment. This includes technical documentation (system architecture, network diagrams, power requirements), process documentation (setup sequences, calibration procedures, teardown checklists), and archival documentation (high-quality capture, audience response, technical lessons learned). The emphasis is on creating documentation that serves future iterations of the work, not just the current deployment.

**`festival-rider.md`** — A technical rider template designed for technology-mediated art presented in festival and venue contexts. Standard performance riders don't account for the needs of interactive installations, real-time generative systems, or networked performances. This template covers power requirements (including clean power for sensitive electronics), network connectivity (bandwidth, latency, firewall considerations), spatial requirements (projection distances, sensor coverage areas, audience flow patterns), and environmental considerations (ambient light, acoustic conditions, temperature ranges for equipment).

**`indie-venue-setup.md`** — A practical guide for setting up technology-mediated art in non-traditional spaces — warehouses, galleries without technical infrastructure, outdoor sites, found spaces. This playbook addresses the specific challenges of these contexts: unreliable power, unknown network conditions, variable lighting, non-standard mounting surfaces, and the absence of dedicated technical staff. It emphasizes portable, resilient system design and provides decision trees for common setup challenges.

### Grant Resources

The grant resources suite addresses what is, for many artists, the most important and most dreaded aspect of professional practice: funding applications.

**`budget-checklist.md`** — A comprehensive list of budget line items relevant to technology-mediated art projects. Artists consistently underestimate costs because they forget categories — not just obvious ones like equipment and materials, but less visible ones like software licenses, cloud hosting, documentation and archival, accessibility accommodations, and post-project maintenance. This checklist is organized by project phase (development, production, deployment, documentation, maintenance) and includes notes on which costs are typically eligible for different funding sources.

**`funding-landscape.md`** — An overview of funding sources relevant to technology-mediated art, organized by type (government arts councils, private foundations, corporate sponsorship, academic research grants, crowdfunding), geography, and project type. This is not an exhaustive database but a navigational guide that helps artists identify which funding ecosystems are relevant to their practice and how to approach them.

**`proposal-template.md`** — A grant proposal framework structured around the common elements that most funders require, with specific guidance for technology-mediated art. The template addresses the persistent challenge of describing technical work in terms that non-technical reviewers can evaluate, providing strategies for foregrounding artistic intent and cultural significance while demonstrating technical feasibility and innovation.

### General Templates

**`collaboration-agreement.md`** — A framework for formalizing collaboration terms in multi-artist projects. Technology-mediated art frequently involves collaboration between people with different skill sets (visual artists, programmers, sound designers, performers), and these collaborations often begin informally. This template provides a lightweight structure for addressing the questions that informal collaborations tend to defer until they become problems: intellectual property, decision-making authority, credit, revenue sharing, and project dissolution.

**`project-plan.md`** — An iterative project planning framework designed for creative processes that don't follow linear production timelines. Traditional project management tools assume that scope is defined at the outset and execution follows a predetermined path. Creative projects — especially those involving generative systems and emergent behaviors — require planning frameworks that accommodate discovery, iteration, and the productive failure that is essential to artistic research. This template provides that framework.

## Template Philosophy

### Why Not Just Use Existing Templates?

There are plenty of template resources available for artists — from arts council websites, MFA programs, professional development organizations. What distinguishes this toolkit is its specificity to technology-mediated art practice and its integration into a larger creative system.

Generic artist templates assume a traditional studio practice: you make objects, you exhibit them, you sell them. The workflow is linear, the outputs are physical, and the professional infrastructure is well-established. Technology-mediated art breaks these assumptions in multiple ways:

- **The work is often ephemeral** — performances, installations, and generative systems exist in time and space, not as transportable objects.
- **The technical requirements are significant** — presenting the work requires infrastructure (power, network, computation) that traditional art venues may not provide.
- **The costs are different** — cloud hosting, software licenses, and equipment maintenance are ongoing costs that don't fit traditional art budgets.
- **The collaboration models are complex** — projects often involve people with fundamentally different skill sets and professional expectations.
- **The documentation challenges are unique** — capturing a real-time generative audiovisual performance requires different strategies than photographing a painting.

This toolkit addresses these specific needs because it is built from within the practice, not adapted from outside it.

### Templates and the Creative Pipeline

Within the ORGAN-II ecosystem, templates serve a specific architectural function. The creative pipeline flows from conceptual frameworks (defined in ORGAN-I repositories) through creative engines and performance systems (the core of ORGAN-II) to professional presentation and deployment. Templates sit at the interface between creative work and the professional world — they are the documents that translate artistic vision into the language of institutions, funders, venues, and collaborators.

This means templates are not standalone documents. They are designed to integrate with:

- **[metasystem-master](https://github.com/organvm-ii-poiesis/metasystem-master)** — the central coordination hub for ORGAN-II, which defines the creative systems that these templates help deploy and present.
- **Performance and installation systems** across ORGAN-II — the deployment playbooks directly support the physical presentation of work created with these systems.
- **ORGAN-III commercial products** — templates for client-facing art (proposals, agreements, project plans) feed into the commercial pipelines defined in ORGAN-III.

## Theory Implemented from ORGAN-I

The design of this toolkit draws on several theoretical frameworks developed within [ORGAN-I (Theoria)](https://github.com/organvm-i-theoria):

**Recursive self-documentation** — The toolkit practices what it preaches. Each template includes meta-documentation explaining its own design decisions, creating a recursive layer where the documentation of creative infrastructure is itself a form of creative infrastructure. This reflects ORGAN-I's broader investigation of self-referential systems.

**Ontological scaffolding** — ORGAN-I's work on ontological frameworks informs how templates structure knowledge. Rather than imposing a single organizational scheme, templates provide multiple entry points and organizational layers that users can traverse according to their needs. A grant proposal template, for example, can be read as a persuasive narrative, a technical specification, or a budget justification — three ontological frames applied to the same underlying project.

**The commons as creative medium** — ORGAN-I's theoretical work on shared creative resources directly motivates the open-source approach of this toolkit. The argument is not merely pragmatic (sharing is efficient) but conceptual (the commons itself is a creative medium, and contributing to shared infrastructure is a form of artistic practice).

## Integration with the ORGAN-II Ecosystem

This repository is one node in the ORGAN-II creative constellation:

| Repository | Role | Relationship to This Toolkit |
|-----------|------|------------------------------|
| [metasystem-master](https://github.com/organvm-ii-poiesis/metasystem-master) | Central creative coordination | Defines the systems these templates help deploy |
| core-engine | Creative computation engine | Deployment playbooks support its physical presentation |
| performance-sdk | Live performance framework | Festival rider and venue setup templates serve its deployment needs |
| artist-toolkit-and-templates | **This repo** — professional infrastructure | Provides the administrative scaffolding for all ORGAN-II work |

The toolkit is designed to be **engine-agnostic** — its templates work regardless of which creative systems an artist uses. But it is also **ecosystem-aware** — templates include integration points where artists working with ORGAN-II systems can reference their specific technical requirements, documentation standards, and deployment patterns.

## Planned Content and Roadmap

### Near-Term (Silver Sprint)

- [ ] Populate all existing template stubs with full content
- [ ] Add worked examples in `example-projects/` demonstrating real-world template usage
- [ ] Cross-reference templates with deployment playbooks (e.g., budget checklist references festival rider line items)

### Medium-Term (Gold Sprint)

- [ ] Add templates for generative art (visual) — parameter documentation, rendering pipeline specs, exhibition display requirements
- [ ] Add templates for generative audio — sound design documentation, spatialization riders, acoustic environment assessment
- [ ] Add templates for installation art — sensor layout documentation, interaction design specifications, maintenance schedules
- [ ] Create template generation scripts that pre-populate project-specific information from ORGAN-II system metadata
- [ ] Build a template validation workflow (GitHub Actions) that checks for completeness and consistency

### Long-Term

- [ ] Interactive template builder (web-based) integrated with ORGAN-III tooling
- [ ] Community-contributed template variants for different art-world contexts (European funding, US NEA, academic research, commercial commissions)
- [ ] Template analytics — which templates are most used, which sections are most modified, where artists diverge from the suggested structure
- [ ] Localization support for non-English-speaking art communities

## Migration Note

This repository supersedes the earlier [`artist-toolkits-templates`](https://github.com/organvm-ii-poiesis/artist-toolkits-templates) repository, which used a slightly different naming convention. The rename reflects the standardized naming scheme adopted across the ORGAN system during Phase -1 infrastructure work. All content and history from the predecessor have been preserved. If you have bookmarks or references to the old repository name, please update them to point here.

## Contributing

Contributions are welcome, particularly from practicing artists who can bring real-world experience to template design. The most valuable contributions are:

1. **Template refinements** based on actual use — if you used a template and found it missing something, that feedback is gold.
2. **Context-specific variants** — a festival rider for a European media arts festival has different conventions than one for a US gallery. Regional and contextual variants expand the toolkit's usefulness.
3. **Worked examples** — anonymized or fictionalized examples showing how a template was adapted for a specific project help future users understand the gap between template and finished document.
4. **Translations** — making templates accessible in languages beyond English is a meaningful contribution to the global art community.

Please open an issue before starting significant work to ensure alignment with the toolkit's design philosophy. All contributions should follow the principle that templates enable rather than constrain creative practice.

## License

[MIT](LICENSE) — Use these templates freely. Adapt them. Share them. The whole point is that professional creative infrastructure should be accessible to everyone.

## Author

**[@4444j99](https://github.com/4444j99)** — Artist, technologist, and systems thinker building infrastructure for creative practice.

Part of the [ORGAN system](https://github.com/meta-organvm) — an eight-organ creative-institutional architecture coordinating theory, art, commerce, orchestration, public process, community, and distribution.

---

*Templates are not the work. Templates hold space for the work. The difference matters.*
