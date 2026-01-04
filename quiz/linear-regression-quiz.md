# Linear Regression - Quiz

## Instructions
Answer all questions. Review explanations after completing the quiz.

---

## Multiple Choice

**Q1.** Which assumption do ordinary least squares models rely on to keep coefficient estimates unbiased?
- A) The design matrix is orthogonal
- B) Errors have zero mean and are uncorrelated with features
- C) Features follow a Gaussian distribution
- D) The learning rate is constant

**Q2.** A business analyst fits a linear regression model with advertising spend (TV, radio, online) as predictors. Which improvement best addresses multicollinearity if TV and radio spend are highly correlated?
- A) Increase the polynomial degree of each predictor
- B) Drop one of the correlated predictors or combine them into a single feature
- C) Use a larger learning rate in gradient descent
- D) Add more intercept terms to the model

**Q3.** What does the R² metric represent in linear regression?
- A) The average magnitude of residuals
- B) The proportion of variance in the target explained by the features
- C) The slope of the best-fit line
- D) The regularization strength

**Q4.** When training with gradient descent, why is feature scaling recommended?
- A) It increases model bias, reducing variance
- B) It ensures the intercept equals zero
- C) It keeps gradients balanced across dimensions, improving convergence
- D) It guarantees a global optimum

**Q5.** Which modification to linear regression directly penalizes large coefficient magnitudes to reduce overfitting?
- A) Feature normalization
- B) Ridge regression
- C) Adding interaction terms
- D) Increasing dataset size

---

## True/False

**Q6.** Linear regression cannot model non-linear relationships under any transformation. (True/False)

**Q7.** Homoscedasticity means the variance of residuals changes with the predicted value. (True/False)

---

## Short Answer

**Q8.** Describe a diagnostic you would run to detect violations of the linearity assumption and explain how you would interpret it.

---

# Answer Key

## Q1
**Answer:** B
**Explanation:** OLS assumes errors have zero mean and are uncorrelated with features; otherwise estimates become biased. (Reference: notes/linear-regression.md:13-33)

## Q2
**Answer:** B
**Explanation:** Removing or combining correlated predictors reduces multicollinearity and stabilizes coefficient estimates. (Reference: notes/linear-regression.md:29-33)

## Q3
**Answer:** B
**Explanation:** R² measures the proportion of target variance explained by the predictors. (Reference: notes/linear-regression.md:34-49)

## Q4
**Answer:** C
**Explanation:** Scaling features yields comparable gradient magnitudes, leading to faster convergence when using gradient descent. (Reference: notes/linear-regression.md:45-48)

## Q5
**Answer:** B
**Explanation:** Ridge regression adds an L2 penalty that shrinks coefficients and controls variance. (Reference: notes/linear-regression.md:29-33, 41-48)

## Q6
**Answer:** False
**Explanation:** Polynomial or other feature transformations let linear regression model non-linear relationships while remaining linear in parameters. (Reference: notes/linear-regression.md:37-41)

## Q7
**Answer:** False
**Explanation:** Homoscedasticity means constant residual variance; changing variance indicates heteroscedasticity. (Reference: notes/linear-regression.md:41-48)

## Q8
**Answer:** Plot residuals versus fitted values; a random scatter suggests linearity holds, while systematic patterns (curves or funnels) indicate violations requiring feature transformations or different models. (Reference: notes/linear-regression.md:45-48)

---
Source: notes/linear-regression.md
Question count: 8
Difficulty: Basic
