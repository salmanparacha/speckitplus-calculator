# Lecture Notes Boilerplate

> Use this template for each AI300 lecture note. Copy this file and rename it for each lecture.

---

## Headings

Use `#` for the main title, then `##`, `###` for smaller sections:

```markdown
# Main Heading (Lecture Title)
## Section Heading
### Subsection
#### Detail
```

**Why:** Creates a clear hierarchy. Helps you quickly scan and find topics later.

---

## Lists

### Unordered Lists (bullet points)

```markdown
- Item 1
- Item 2
  - Nested item
  - Another nested item
```

**Why:** Great for concepts, features, ideas without a specific order.

### Ordered Lists (numbered)

```markdown
1. First step
2. Second step
3. Third step
```

**Why:** Perfect for processes, steps, or things that happen in sequence.

### Checklists (task lists)

```markdown
- [ ] Not done
- [x] Completed
```

**Why:** Track what you've covered, what to practice, or project progress.

---

## Emphasis

```markdown
*Italic* or _Italic_
**Bold** or __Bold__
***Bold and Italic***
```

**Why:** Highlight key terms, important formulas, or emphasize critical concepts.

---

## Code

### Inline Code

Use backticks for small code snippets:

```markdown
Use `print()` to output text.
The variable `learning_rate` controls step size.
```

### Code Blocks

Use triple backticks for larger code blocks:

```markdown
```python
def train_model(model, data, epochs):
    for epoch in range(epochs):
        loss = forward_pass(model, data)
        backward_pass(model, loss)
```
```

**Why:** Keeps code separate from explanations. Adds syntax highlighting for readability.

---

## Blockquotes

```markdown
> Important note or concept
> Another line in the quote
```

**Why:** Draw attention to key insights, warnings, or important formulas.

---

## Tables

```markdown
| Model | Accuracy | Training Time |
|-------|----------|---------------|
| BERT  | 89%      | 4 hours       |
| GPT   | 92%      | 8 hours       |
```

**Why:** Compare results, track experiments, organize data clearly.

---

## Horizontal Rules

```markdown
---
```

**Why:** Separate major sections in your notes.

---

## Links

```markdown
[Link text](url)
```

Example: `[PyTorch Docs](https://pytorch.org/docs)`

**Why:** Reference external resources, papers, or related notes.

---

## Combined Example: Lecture Notes

```markdown
# Lecture 5: Backpropagation

## Key Concepts
- **Gradient descent**: Optimization algorithm
- **Chain rule**: Core mathematical principle
- **Learning rate`: Controls step size

## Algorithm Steps
1. Forward pass: Compute predictions
2. Compute loss: `L = (y - ŷ)²`
3. Backward pass: Calculate gradients
4. Update weights: `w = w - lr * ∂L/∂w`

## Formulas to Remember
> ∂L/∂w² = ∂L/∂a × ∂a/∂z × ∂z/∂w²

## Practice Tasks
- [ ] Implement backprop from scratch
- [ ] Compare with PyTorch autograd
- [ ] Visualize gradients

## Resources
- [CS231n Lecture 4](http://cs231n.stanford.edu)
- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com)

## Experiment Results
| Model | Loss | Accuracy |
|-------|------|----------|
| MLP-2 | 0.23 | 85%      |
| MLP-4 | 0.15 | 91%      |

---
```

---

## Quick Reference Card

| What you want | How to do it |
|---------------|--------------|
| Main title | `# Title` |
| Section | `## Section` |
| Bullet list | `- Item` |
| Numbered list | `1. Item` |
| Bold | `**text**` |
| Italic | `*text*` |
| Inline code | `` `code` `` |
| Code block | ` ```python code``` ` |
| Important note | `> Note` |
| Checkbox | `- [ ]` |
| Link | `[text](url)` |

---

## Tips for AI300 Course

1. **Start each lecture** with a `# Lecture X: [Topic]` heading
2. **Use `##`** for major sections (Concepts, Code, Formulas, Practice)
3. **Track progress** with checklists: `- [ ] Not started`, `- [x] Done`
4. **Code examples** should always be in code blocks with language specified
5. **Formulas** in blockquotes: `> L = Σ(y - ŷ)²`
6. **Tables** for comparing models, algorithms, or experiment results
7. **Links** to papers, docs, or related lectures
8. **Horizontal rules (`---`)** between major topics

---

Remember: **Structure > completeness**. Well-organized notes are more useful than disorganized comprehensive notes. You can always add details later.
