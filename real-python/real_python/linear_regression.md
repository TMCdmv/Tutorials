###<center>Linear Regression Tutorial</center>
#### Regression Theory
Regression creates a model representing a relationship between a set of variables. In linear regression, the model is a *line*.  
- The variables of interest, i.e. the one being forecast, is called the dependent variable. It is also called the response or output. This variable is designated as $y$
- The other variables or the independent variables. They are also called inputs, regressors, or predictors.  A set $x = x_1, x_2, ..., x_r)$ represent these independent variables or predictors.

A line is *fitted* to the above DATa using the formula:

$$
y = \beta_0 + \beta_1x_1 + \beta_2x_2 + ... + \beta_rx_r + \epsilon
$$ (1) General linear regression formula

The $\beta$ coefficients are the *regression* coefficients and $\epsilon$ is the *random error*  

Regression ***estimates*** the regression coefficients or predicted weights. The estimates of the $\beta$ coefficients are designated as $b_0, b_1,..., b_r$. These estimated coefficients now define the *estimated regression function*  

$$
f(x) = b_0 + b_1x_1 + b_2x_2 + ... + b_rx_r
$$ (2) General *estimated* linear regression formula

THe estimated response, $f(x_i)$ should be as close as possible to the actual response $y_i$. The difference between the actual and predicted response for each observation are called the residuals. Regression determines the best predicted weights (regression coefficients) that minimize the residuals. The usual technique is to *minimize* the ***sum of squared residuals***, or ***SSR***:  

$$
\forall i \in (1, 2, 3, ..., n), \\
SSR = \sum_i(y_i - f(x_i))^2
$$ (3) Definition of sum of squared residuals 

#### Regression Performance  

The variation of the actual responses $y_0, y_1, ..., y_n)$ is due to the dependence on the predictions $x_i$ *plus* an inherent variance of the output.  

$R^2$, the coefficient of determination, tell how much of the variation in $y_i$ can be explained by the dependence on $x_i$ for the particular model used. A larger indicates a better fit - the model can better explain the variation in outputs with different inputs. A $R^2 = 1$ corresponds to a $SSR = 0$ - a perfect fit.

A graph of a simple regression model (only one input variable):

<img src=fig-lin-reg.webp width=500 >  

