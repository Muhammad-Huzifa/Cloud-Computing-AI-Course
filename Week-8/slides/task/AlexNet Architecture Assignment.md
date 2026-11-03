# Task: Create the AlexNet Architecture

## Objective

Implement the original AlexNet convolutional neural network architecture and document how data moves through each layer.

## Requirements

1. Use an input image size of `227 × 227 × 3`.
2. Include the five convolutional layers, three max-pooling layers, and three fully connected layers from the original AlexNet design.
3. Use ReLU activations after the convolutional and fully connected layers.
4. Include the original Local Response Normalization layers where appropriate, or clearly explain why they are omitted.
5. Use a final classification layer whose number of outputs matches the selected dataset.
6. Record the output shape after every layer and calculate the total number of trainable parameters.
7. Train the model, report training and validation accuracy/loss, and include at least one confusion matrix or classification report.

## Suggested Layer Sequence

| Stage | Layer | Main configuration |
|---|---|---|
| 1 | Conv + ReLU | 96 filters, `11 × 11`, stride 4 |
| 2 | Max Pool | `3 × 3`, stride 2 |
| 3 | Conv + ReLU | 256 filters, `5 × 5`, padding 2 |
| 4 | Max Pool | `3 × 3`, stride 2 |
| 5 | Conv + ReLU | 384 filters, `3 × 3`, padding 1 |
| 6 | Conv + ReLU | 384 filters, `3 × 3`, padding 1 |
| 7 | Conv + ReLU | 256 filters, `3 × 3`, padding 1 |
| 8 | Max Pool | `3 × 3`, stride 2 |
| 9 | Fully Connected + ReLU | 4096 units |
| 10 | Fully Connected + ReLU | 4096 units |
| 11 | Classifier | Dataset-specific output units with softmax |

## Deliverables

- Source code or a notebook that builds and trains AlexNet.
- A layer-by-layer architecture table with output shapes and parameter counts.
- Training results and a short discussion of overfitting, regularization, and model performance.
- A brief comparison between AlexNet and the CNN model used in this week’s work.

## Submission Checklist

- [ ] Model runs from a clean environment.
- [ ] Dataset and preprocessing are described.
- [ ] Output shapes and parameter counts are verified.
- [ ] Results include validation metrics.
- [ ] Code and documentation are committed to the repository.
