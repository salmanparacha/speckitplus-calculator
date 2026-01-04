# Linear Regression - Flashcards

## Core Terminology

Q: What is the goal of linear regression?
A: To model the linear relationship between explanatory variables and a continuous target.

Q: What does the intercept term represent in linear regression?
A: The predicted target value when all input features are zero.

Q: Define residual in the context of regression.
A: The difference between the observed target value and the model’s prediction.

Q: What is the hypothesis function for multiple linear regression?
A: \( \hat{y} = w_0 + w_1 x_1 + \dots + w_n x_n \).

Q: What loss function is most commonly minimized during training?
A: Mean Squared Error (MSE).

## Key Concepts

Q: Why is multicollinearity a problem for linear regression?
A: It inflates coefficient variance, making estimates unstable and hard to interpret.

Q: How do ridge and lasso regression modify linear regression?
A: They add penalty terms on coefficients to reduce variance and combat overfitting.

Q: What assumption does homoscedasticity refer to?
A: That residuals have constant variance across all predicted values.

Q: How does feature scaling help gradient descent training?
A: It improves convergence speed by keeping gradients balanced across dimensions.

Q: Why are residual plots useful?
A: They reveal violations of linearity, constant variance, or independence assumptions.

## Relationships & Comparisons

Q: How does polynomial regression relate to linear regression?
A: It augments features with polynomial terms but still fits a linear model in the expanded feature space.

Q: Contrast ridge vs. lasso regularization.
A: Ridge uses L2 penalties to shrink coefficients; lasso uses L1 penalties that can drive some coefficients to zero.

Q: What differentiates simple from multiple linear regression?
A: Simple uses one explanatory variable, while multiple uses two or more.

---
Source: notes/linear-regression.md
Card count: 13
