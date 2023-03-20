# Todo


Page on official name, variable name for module import.  Covering:

```{python}
import numpy
import numpy as np
# Why does `from np import cos` fail?
from numpy import cos
```

Add page / section on `Series.value_counts`.

Cover:

* bar charts
* histograms
* scatter plots
* maybe maps.

Explain and `.copy()` for Pandas Series.

Move to "what's my best guess" idea for sum of squared deviations.

Need to slow down a bit for the mean / sum of squares discussion.

Remove, de-emphasize or at least comment on t-test calculation, including in
exercise.

Introduction to probability.

Better introduction to functions, and docstrings.

Extend discussion of lists and tuples.

Consider introduction to dictionaries.

Use `method='powell'` in all calls to `minimize`.

Explain with references in `using_minimize` page.  Add
<https://scipy-lectures.org/advanced/mathematical_optimization/#choosing-a-method>.

Merge intro to function and functions page.

Use student ratings dataset to demonstrate regression, residuals "controlling for".

Break logistic regression page into least-squares, and logit pages.

Least square page moves from straight line prediction, to straight line
clipped at 0 and 1.  Show that adding values at left and right causes changes
in unclipped portion of line.

## Add back returning early clause

This section lost from refactor of conditional_statement page.  Put back
somewhere?

### Interlude - returning early

Remember the simpler version of our function:

```{python}
def classify(x):
    if x > 0:
        result = 'Positive'
    elif x == 0:
        result = 'Zero'
    else:
        result = 'Negative'
    return result
```

You can see that, if `x` is greater than 0, then we reach `result
= 'Positive'`.  In fact, when we get to that line, our work is done, and we might as well leave function world and send back the result.  We can do that by using another `return` statement, like this:

```{python}
def classify_returning_early(x):
    if x > 0:
        return 'Positive'
    elif x == 0:
        return 'Zero'
    else:
        return 'Negative'
```

This will work exactly the same way as the original version above.  This way, as soon as we have the answer we need, we are breaking out of function world, and sending back the answer.

Notice that we do not need a final `return` statement any more, because our
`if` statement has covered all possible values.  Therefore, we will always
`return` inside the `if` statement, and we will never reach any statements
that follow the `if` statement.

Here is the new version in action:

```{python}
print(classify_returning_early(3))
print(classify_returning_early(-3))
print(classify_returning_early(0))
```

This is a common pattern, where we break out of function world as soon as we
have the answer we need.

## Boolean indexing to set values

Add more on this in
https://lisds.github.io/textbook/data-frames/boolean_indexing.html#setting-values-with-boolean-arrays
and add somewhere for Pandas indexing.

## Orphan pages

* `iteration/arrays_and_axes.Rmd`
* `permutation/lists.Rmd`
* `useful-pandas/merge_and_sql.Rmd`
* `wild-pandas/df_sums.Rmd`
* `wild-pandas/two_by_two_tables.Rmd`

## Move links, think about Pandas pages

Many links to pages in `wild-pandas` should go somewhere else.  See `_toc.yml`.  In general, review arrangement of Pandas pages.

## Link to loss function

<https://en.wikipedia.org/wiki/Loss_function>

Think about terms - stinkiness, loss, cost.  Use them consistently.

## Consider using DSFE module

EOM.
