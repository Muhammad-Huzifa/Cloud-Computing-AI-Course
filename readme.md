# From Machine Learning to Production AI Deployment

**End-to-end model training, pipeline engineering, and cloud deployment**

## About This Repository

This repository contains the teaching and practice materials for a 12-week Huawei HCCDA-AI course. The course starts with Python and data handling, moves through machine learning and deep learning, and ends with model serving and cloud deployment.

Each topic is taught through short slides, guided exercises, live coding, and a complete reference notebook. The aim is to help students understand how each part works and then connect the parts into an end-to-end AI system.

Huawei HCCDA-AI provides the main course direction, but the practical work is cloud-flexible. Depending on the available accounts, credits, and computing resources, deployment may use Huawei Cloud, Microsoft Azure, Hugging Face Spaces, or another suitable cloud server. The underlying ideas of training, evaluation, API development, pipeline engineering, and deployment remain the same.

## Learning Method

Every week uses three notebooks with the same core concepts:

| Notebook | Purpose |
| --- | --- |
| `Student_Tasks.ipynb` | Guided questions and exercises for students to complete |
| `Live_Code.ipynb` | Code developed step by step during the class |
| `Perfect_Code.ipynb` | Clean and complete reference solution after the lesson |

This structure allows students to practise independently, follow the classroom implementation, and review a correct final version.

## Planned 12-Week Roadmap

| Week | Main Focus |
| --- | --- |
| 1 | Python foundations and the development environment |
| 2 | NumPy arrays and numerical computing |
| 3 | Pandas and structured data handling |
| 4 | Data cleaning, visualization, and exploratory analysis |
| 5 | Machine learning workflow and data preparation |
| 6 | Supervised learning: classification and regression |
| 7 | Model evaluation, feature engineering, and tuning |
| 8 | Neural networks and deep learning foundations |
| 9 | Applied AI with computer vision and natural language processing |
| 10 | Saving models and serving predictions through an API |
| 11 | Pipeline engineering and cloud deployment |
| 12 | End-to-end AI project: training, testing, and deployment |

The weekly sequence may be adjusted according to student progress and the practical requirements of the official course material.

## Repository Structure

```text
course-repository/
├── README.md
├── Week-1/
│   ├── Code/
│   │   ├── Student_Tasks.ipynb
│   │   ├── Live_Code.ipynb
│   │   └── Perfect_Code.ipynb
│   └── Slides/
│       └── Week_1_Slides.pdf
├── Week-2/
│   ├── Code/
│   └── Slides/
└── ...
```

Only the PDF version of each slide deck is included on GitHub. The editable PowerPoint files are kept locally.

## Main Tools

- Python and Jupyter notebooks
- NumPy, Pandas, Matplotlib, and Scikit-learn
- Deep learning frameworks introduced during the course
- Git, GitHub, and VS Code
- FastAPI or another suitable model-serving tool
- Huawei Cloud or an alternative cloud platform when required

## How to Use the Materials

1. Open the folder for the required week.
2. Read the slide PDF for the main concepts.
3. Attempt `Student_Tasks.ipynb` before checking the solution.
4. Follow or repeat the implementation in `Live_Code.ipynb`.
5. Use `Perfect_Code.ipynb` to review the complete approach.

## Course Goal

By the end of the 12 weeks, students should be able to prepare data, train and evaluate machine-learning models, build a prediction pipeline, expose a model through an API, and deploy it on an available cloud platform or server.

## Status

Course materials will be added and updated week by week.
