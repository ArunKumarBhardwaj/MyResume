# Arun Kumar Bhardwaj — Resume

Source for my resume, built with [RenderCV](https://github.com/rendercv/rendercv) using the **engineeringresumes** theme (same layout style as a clean RenderCV engineering CV).

RenderCV takes a YAML input file (`Arun_Kumar_Bhardwaj_CV.yaml`) and generates a professional PDF.

## Resume PDF

Public repo — anyone can open or download:

- **[View](https://github.com/ArunKumarBhardwaj/MyResume/blob/main/rendercv_output/Arun_Kumar_Bhardwaj_CV.pdf)**
- **[Download](https://github.com/ArunKumarBhardwaj/MyResume/raw/main/rendercv_output/Arun_Kumar_Bhardwaj_CV.pdf)**

The PDF updates whenever `rendercv_output/` is pushed to `main` (or via the Generate Resume Actions workflow when the YAML changes).

## Quick Start

```bash
pipx install "rendercv[full]"
# or: python -m venv .venv && .venv/bin/pip install "rendercv[full]"
rendercv render Arun_Kumar_Bhardwaj_CV.yaml
```

Watch mode:

```bash
rendercv render --watch Arun_Kumar_Bhardwaj_CV.yaml
```

## Source

- **[Arun_Kumar_Bhardwaj_CV.yaml](./Arun_Kumar_Bhardwaj_CV.yaml)** — experience, projects, skills, education

## Built With

- [RenderCV](https://docs.rendercv.com/) — CV generator from YAML
