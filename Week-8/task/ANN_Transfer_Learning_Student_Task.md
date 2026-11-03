# Student Task: Improve the Four-Class Image Classifier

## Context

Use the **same labelled image dataset** and folder structure as the supplied ANN/transfer-learning notebook. The instructor notebook uses 128 x 128 RGB images, four output classes, a frozen MobileNetV2 feature extractor, and a softmax classifier. Do not download a different dataset.

## Objective

Build a reproducible image classifier, measure its performance on unseen images, and run one controlled improvement experiment. Your work should show that you understand data loading, transfer learning, evaluation, and evidence-based model improvement.

## Student requirements

1. Copy the instructor notebook or create a new notebook in this folder. Set a relative `DATA_DIR` that points to the same four-class image folders.
2. Print the class names, number of images per class, and the train/validation/test split sizes. Use a fixed random seed.
3. Create a baseline with the same input size `(128, 128, 3)`, a frozen MobileNetV2 backbone, and a four-unit softmax output layer. Train for no more than 10 epochs.
4. Report training and validation accuracy/loss with a clearly labelled plot.
5. Evaluate on a held-out test set. Include accuracy, a confusion matrix, and a classification report. Show at least four example predictions, including one mistake if the test set contains mistakes.
6. Run **one** improvement experiment: add data augmentation, add dropout or regularization, unfreeze only the final MobileNetV2 block for fine-tuning, or compare a smaller CNN. Change one main idea at a time.
7. Compare the baseline and improved model in a small table. Explain whether the change improved generalization, using validation and test evidence rather than training accuracy alone.
8. Save the best model as `student_model.keras` and write a short README paragraph describing how to load it and predict one image.

## Constraints

- Keep the original dataset unchanged and do not commit downloaded model weights or generated caches.
- Use relative paths so another student can run the notebook from the repository.
- Do not claim a result without showing the metric or plot that supports it.
- If your computer cannot run the full experiment, reduce image count or epochs and explain the limitation.

## Submission checklist

- [ ] Completed notebook with outputs visible.
- [ ] Fixed seed and reproducible relative data path.
- [ ] Class distribution and split sizes.
- [ ] Baseline curves and held-out evaluation.
- [ ] Confusion matrix and classification report.
- [ ] One controlled improvement and comparison table.
- [ ] Four prediction examples.
- [ ] `student_model.keras` and a short loading/prediction note.

## Suggested grading rubric (20 points)

| Area | Points |
| --- | ---: |
| Data loading, split, and reproducibility | 4 |
| Correct baseline transfer-learning model | 4 |
| Evaluation evidence and visualizations | 5 |
| Controlled improvement and comparison | 4 |
| Code clarity, saved model, and explanation | 3 |

## Starter hints

Use `tf.keras.utils.image_dataset_from_directory` or the loader already present in the instructor notebook. Keep class order explicit, normalize consistently, and use `EarlyStopping` or `ModelCheckpoint` when helpful. A strong report can be concise: show the evidence, then explain what it means.
