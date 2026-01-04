# Linear Regression

## Overview
Linear regression models the relationship between a numerical target variable and one or more explanatory variables by fitting a linear equation. It provides interpretable coefficients, efficient training, and serves as a foundation for many statistical learning techniques.

## Key Concepts (Remember)
- **Dependent Variable (y)**: Continuous value predicted by the model.
- **Independent Variable(s) (x)**: Features used to explain variations in y.
- **Hypothesis Function**: \( \hat{y} = w_0 + w_1 x_1 + \dots + w_n x_n \).
- **Residual**: Difference between observed and predicted values \( y - \hat{y} \).
- **Mean Squared Error (MSE)**: Average of squared residuals, the common loss for training.

## Understanding the Concepts (Understand)
Linear regression assumes a linear relationship between inputs and the target. The model fit minimizes the sum of squared residuals, leading to closed-form coefficient estimates via the normal equation or iterative optimization such as gradient descent. Interpreting coefficients reveals how a one-unit increase in a feature impacts the prediction when other features are held constant. The intercept captures the expected target value when all features are zero.

## Practical Applications (Apply)
### Example 1: House Price Prediction
Given size, number of rooms, and neighborhood indicators, linear regression approximates market prices, enabling quick valuation and sensitivity analysis.

### Example 2: Forecasting Sales
Model future sales using advertising spend, seasonal dummy variables, and historical demand to guide budgeting decisions and scenario planning.

## Deep Dive (Analyze)
### Component Breakdown
- **Design Matrix (X)**: Rows represent observations; columns represent features including a bias term.
- **Parameter Vector (w)**: Contains coefficients estimated by minimizing MSE.
- **Error Term (ε)**: Captures noise or factors not explained by the model.

### Relationships
- Multicollinearity inflates coefficient variance and destabilizes interpretations.
- Feature scaling affects gradient descent convergence, though not closed-form solutions.
- Regularization (e.g., ridge, lasso) extends linear regression by penalizing coefficient magnitude to control variance.

## Critical Assessment (Evaluate)
### Strengths
- Fast to train and easy to interpret.
- Works well when the true relationship is approximately linear.
- Provides statistical diagnostics (R², confidence intervals) under classical assumptions.

### Limitations
- Fails to capture non-linear relationships without engineered features.
- Sensitive to outliers, which can skew coefficient estimates.
- Assumes homoscedastic, independent errors; violations reduce reliability.

### Best Practices
- Inspect residual plots to validate linearity and constant variance assumptions.
- Standardize or normalize features when using gradient-based optimization.
- Apply regularization or feature selection to mitigate multicollinearity and overfitting.

## Extend Your Learning (Create)
### Practice Questions
1. How would you diagnose and address heteroscedasticity in a regression model?
2. What feature transformations could help linear regression capture non-linear effects?

### Further Exploration
- Study ridge vs. lasso regression and their impact on coefficient shrinkage.
- Explore polynomial features to model curved relationships.

## References
- Hastie, Tibshirani, Friedman. *Elements of Statistical Learning*.
- Montgomery, Peck, Vining. *Introduction to Linear Regression Analysis*.
