# From Machine Learning to Production AI Deployment

End-to-end model training, pipeline engineering, and cloud deployment.

Teaching and practice materials for a planned 12-week Huawei HCCDA-AI course. The course starts with Python and data handling, then progresses toward model training, serving, and deployment. Practical deployment can use Huawei Cloud, Azure, Hugging Face Spaces, or another available platform.

## Published materials

| Published week | Materials |
| --- | --- |
| Week-1 | [Open week index](Week-1/README.md) |
| Week-2 | [Open week index](Week-2/README.md) |
| Week-3 | [Open week index](Week-3/README.md) |
| Week-4 | [Open week index](Week-4/README.md) |

Weeks 1 and 2 provide `Live_Code.ipynb` and `Student_Tasks.ipynb`. Weeks 3 and 4 currently contain topic-specific NumPy, Pandas, TensorFlow, and visualization notebooks. Their indexes show the actual available files. Later weeks are planned and are not advertised as published lessons.

## Setup

Use Python 3.11 in a separate environment. Clone and open the project root:

```bash
git clone https://github.com/Muhammad-Huzifa/machine-learning-deployment-course.git
cd machine-learning-deployment-course
python -m venv .venv
```

| Terminal | Activation |
| --- | --- |
| Windows Command Prompt | `.venv\Scripts\activate.bat` |
| Windows PowerShell | `.\.venv\Scripts\Activate.ps1` |
| Windows Git Bash | `source .venv/Scripts/activate` |
| Linux/macOS | `source .venv/bin/activate` |

```bash
python -m pip install -r requirements.txt
jupyter lab
```

For TensorFlow lessons, install `python -m pip install -r requirements-tensorflow.txt` in the lesson environment.

## How to study

Open the week's index, read the PDF slides, and run the lesson notebooks sequentially. Student task notebooks provide exercises; completed solutions are not required for every published lesson. For CSV examples, use the accompanying dataset folder and inspect the lesson's input path.

## Structure

| Path | Purpose |
| --- | --- |
| `Week-*/Code/` | Live lessons and student notebooks |
| `Week-*/Slides/` | PDF slide decks |
| `Week-*/dataset/` | Local CSV examples where available |
| `docs/ROADMAP.md` | Planned twelve-week sequence |

Slides and datasets are preserved. This pass corrects filenames and navigation, adds setup instructions, and distinguishes published material from planned coverage. Full lesson execution and cloud deployment have not been performed here.

Muhammad Huzifa — [GitHub](https://github.com/Muhammad-Huzifa)
