from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

root = Path(__file__).resolve().parents[2]
out = root / "output" / "pdf" / "Week-8_ANN_Transfer_Learning_Student_Task.pdf"
out.parent.mkdir(parents=True, exist_ok=True)
navy = colors.HexColor("#17324D")
blue = colors.HexColor("#2B6CB0")
ink = colors.HexColor("#25313C")
muted = colors.HexColor("#5B6875")
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Title2", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=22, leading=27, textColor=navy, alignment=TA_CENTER, spaceAfter=8))
styles.add(ParagraphStyle(name="Sub2", parent=styles["Normal"], fontSize=10.5, leading=15, textColor=muted, alignment=TA_CENTER, spaceAfter=16))
styles.add(ParagraphStyle(name="H12", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=navy, spaceBefore=12, spaceAfter=6))
styles.add(ParagraphStyle(name="B2", parent=styles["BodyText"], fontSize=9.5, leading=14, textColor=ink, spaceAfter=5))
styles.add(ParagraphStyle(name="Call2", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=10, leading=14, textColor=navy, backColor=colors.HexColor("#EAF2F8"), borderColor=blue, borderWidth=0.7, borderPadding=8, spaceBefore=5, spaceAfter=8))

def p(text, style="B2"):
    return Paragraph(text, styles[style])

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#D7E0E8"))
    canvas.line(18*mm, 14*mm, 192*mm, 14*mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(muted)
    canvas.drawString(18*mm, 8*mm, "Huawei HCCDA-AI Course | Week 8")
    canvas.drawRightString(192*mm, 8*mm, f"Page {doc.page}")
    canvas.restoreState()

story = [p("Student Task", "Title2"), p("Improve the Four-Class Image Classifier", "Sub2")]
story.append(p("Use the <b>same labelled image dataset</b> and folder structure as the supplied ANN/transfer-learning notebook. The instructor workflow uses 128 x 128 RGB images, four output classes, a frozen MobileNetV2 feature extractor, and a softmax classifier.", "Call2"))
story += [p("Objective", "H12"), p("Build a reproducible image classifier, measure performance on unseen images, and run one controlled improvement experiment. Your work should demonstrate data loading, transfer learning, evaluation, and evidence-based model improvement."), p("Student requirements", "H12")]
req = [
    "Copy the instructor notebook or create a new notebook in this folder. Set a relative <font name='Courier'>DATA_DIR</font> pointing to the same four-class image folders.",
    "Print class names, images per class, and train/validation/test split sizes. Use a fixed random seed.",
    "Create a baseline with input size <font name='Courier'>(128, 128, 3)</font>, a frozen MobileNetV2 backbone, and a four-unit softmax output. Train for no more than 10 epochs.",
    "Report training and validation accuracy/loss with a clearly labelled plot.",
    "Evaluate on a held-out test set with accuracy, a confusion matrix, and a classification report. Show at least four example predictions, including one mistake when available.",
    "Run one improvement experiment: augmentation, dropout/regularization, fine-tuning only the final MobileNetV2 block, or a smaller CNN. Change one main idea at a time.",
    "Compare baseline and improved model in a small table. Explain whether the change improved generalization using validation and test evidence, not training accuracy alone.",
    "Save the best model as <font name='Courier'>student_model.keras</font> and write a short README paragraph showing how to load it and predict one image.",
]
for i, item in enumerate(req, 1):
    story.append(p(f"<b>{i}.</b> {item}"))
story += [p("Constraints", "H12")]
for item in ["Keep the original dataset unchanged and do not commit downloaded weights or generated caches.", "Use relative paths so another student can run the notebook from the repository.", "Do not claim a result without showing the metric or plot that supports it.", "If your computer cannot run the full experiment, reduce image count or epochs and explain the limitation."]:
    story.append(p("&#8226; " + item))
story.append(p("Submission checklist", "H12"))
items = ["Completed notebook with outputs visible.", "Fixed seed and reproducible relative data path.", "Class distribution and split sizes.", "Baseline curves and held-out evaluation.", "Confusion matrix and classification report.", "One controlled improvement and comparison table.", "Four prediction examples.", "student_model.keras and a loading/prediction note."]
check = [[p("Checklist item"), p("Done")]] + [[p(x), p("[ ]")] for x in items]
t = Table(check, colWidths=[155*mm, 19*mm], repeatRows=1)
t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), navy), ("TEXTCOLOR", (0,0), (-1,0), colors.white), ("GRID", (0,0), (-1,-1), 0.35, colors.HexColor("#C8D4DF")), ("VALIGN", (0,0), (-1,-1), "MIDDLE"), ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7), ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5)]))
story.append(t)
story += [p("Suggested grading rubric (20 points)", "H12")]
rubric = [[p("Area"), p("Points")], [p("Data loading, split, and reproducibility"), p("4")], [p("Correct baseline transfer-learning model"), p("4")], [p("Evaluation evidence and visualizations"), p("5")], [p("Controlled improvement and comparison"), p("4")], [p("Code clarity, saved model, and explanation"), p("3")]]
r = Table(rubric, colWidths=[155*mm, 19*mm], repeatRows=1)
r.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), navy), ("TEXTCOLOR", (0,0), (-1,0), colors.white), ("GRID", (0,0), (-1,-1), 0.35, colors.HexColor("#C8D4DF")), ("ALIGN", (1,1), (1,-1), "CENTER"), ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7), ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5)]))
story.append(r)
story += [p("Starter hints", "H12"), p("Use <font name='Courier'>tf.keras.utils.image_dataset_from_directory</font> or the loader already present in the instructor notebook. Keep class order explicit, normalize consistently, and use <font name='Courier'>EarlyStopping</font> or <font name='Courier'>ModelCheckpoint</font> when helpful. A strong report can be concise: show the evidence, then explain what it means.")]
doc = SimpleDocTemplate(str(out), pagesize=A4, rightMargin=18*mm, leftMargin=18*mm, topMargin=16*mm, bottomMargin=20*mm)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(out)
