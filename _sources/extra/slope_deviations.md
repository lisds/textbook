# Mathematics for the least-squares slope

This page follows on from the page on [mean squared
deviations](mean_sq_deviations). Like that page, is assumes a lot more maths
than the standard flow of the course. In particular, it assumes that you
know the basics of finding the
[derivative](https://en.wikipedia.org/wiki/Derivative) of a function.

Please make sure you have read and understand the mean squared deviation page, because this page builds on that argument.

You should also check the page on [means and slopes](../mean-slopes/mean_and_slopes) for
the problem we are trying to solve.

In our problem, we have $n$ $x$ values ${x_1, x_2, ..., x_n}$, that we want to
use to predict $n$ corresponding $y$ values ${y_1, y_2, ..., y_n}$. For
example, in terms of the mean and slopes page, we have 158 hemoglobin
concentration values, so $n = 158$ and we can write our hemoglobin values as
${x_1, x_2, ..., x_{158}}$. We have 158 packed cell volume values, and we can
write these as ${y_1, y_2, ..., y_{158}}$.

We decide we will use a straight line going through the origin to predict
our $y$ points from our $x$ points. We define this line with its _slope_
$s$. This is the number of units that $y$ increases for every unit increase in
$x$. Our predicted values will therefore be $s x_1, s x_2, ..., s x_n$.

We want to choose $s$ such that it minimizes the sum of squared prediction
errors. We define the prediction error for the first value as the actual value
$y_1$ minus the prediction for that value $s x_1$. We have $n$ prediction
errors $y_1 - s x_1, y_2 - s x_2, ..., y_n - s x_n$. The thing we want to
minimize is the sum of squared prediction error for a particular slope $s$,
defined as:

$$
\begin{equation}
SSE_s \triangleq \sum{ (y_i - s x_i)^2}
\end{equation}
$$ (sse_s)

The $\triangleq$ symbol means *is defined as*.

This is the general formula for the specific plot we saw at the end of [mean
and slope page](../mean-slopes/mean_and_slopes), where the value for $s$ is on
the horizontal axis, and the value for $SSE_s$ is on the vertical axis.

We want to find the value of $s$ that gives the smallest value for $SSE_s$.

The plot turned out to be U-shaped; we want to find the horizontal axis
location ($s$ value) corresponding to the bottom of the U (minimum of the
corresponding $SSE_s$ values).

We follow the same scheme as for the [mean squared deviations](mean_sq_deviations) page; we transform the formula in {eq}`sse_s` above
into a formula for the *gradient* of the line that {eq}`sse_s` represents,
by taking the derivative.  When the *derivative* of equation {eq}`sse_s` is equal to zero, it means the *gradient* of {eq}`sse_s` is 0, and this is
true when we are at a peak or a trough of {eq}`sse_s`.  We want the
trough.

First we expand {eq}`sse_s`, and use the [laws of
sums](http://matthew-brett.github.io/teaching/some_sums.html) to simplify the
result:


$$

SSE_s \triangleq \sum (y_i - s x_i)^2 \implies \\
= \sum (y_i^2 - 2 y_i s x_i + s^2 x_i^2) \implies \\
= \sum y_i^2 - 2 s \sum y_i x_i + s^2 \sum x_i^2

$$

Now differentiate with respect to $s$:


$$

\begin{equation}
\frac{\partial SSE_s}{\partial s} = -2 \sum y_i x_i + 2 s \sum x_i^2
\end{equation}

$$ (dsse_s)

Find the zero(s) for equation {eq}`dsse_s`:


$$

2 \sum y_i x_i = 2 s \sum x_i^2 \implies \\
\frac{\sum y_i x_i}{\sum x_i^2} = s

$$

Equation {eq}`dsse_s` only has one zero.

We take the second derivative of {eq}`dsse_s` to see if the solution to
$s$ is at a trough (with a positive second derivative) or a peak (with a
negative second derivative).


$$

\frac{\partial ^2SSE_s}{\partial s^2} = 2 \sum x_i^2

$$

$\sum x_i^2$ is always positive; this means that the second derivative is
always positive, and therefore, it is also positive at our zero point $s =
\frac{\sum y_i x_i}{\sum x_i^2}$.  So, equation {eq}`sse_s` only has a one
trough, at $s = \frac{\sum y_i x_i}{\sum x_i^2}$, and no peaks.

This is the value $s$ for the slope that minimizes the sum of squared errors,
also called the sum of squared deviations, also called the sum of squared
prediction errors.
