# Arun Kumar Bhardwaj — Resume

Source for my resume, built with [RenderCV](https://github.com/rendercv/rendercv) using the **engineeringresumes** theme (same layout style as a clean RenderCV engineering CV).

RenderCV takes a YAML input file (`Arun_Kumar_Bhardwaj_CV.yaml`) and generates a professional PDF.

## Resume PDF

- **[View/Download Resume](https://drive.google.com/file/d/YOUR_FILE_ID/view?usp=drive_link)**: Latest version (Google Drive) — replace `YOUR_FILE_ID` after secrets are set
- Local PDF: [`rendercv_output/Arun_Kumar_Bhardwaj_CV.pdf`](./rendercv_output/Arun_Kumar_Bhardwaj_CV.pdf)

Auto-update on push to `main` (YAML changes) or manual workflow dispatch: see [`docs/GOOGLE_DRIVE_SETUP.md`](./docs/GOOGLE_DRIVE_SETUP.md).

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
