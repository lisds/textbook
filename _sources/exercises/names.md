---
jupyter:
  anaconda-cloud: {}
  jupytext:
    text_representation:
      extension: .Rmd
      format_name: rmarkdown
      format_version: '1.0'
      jupytext_version: 0.8.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.6.5
---

# Exercises on names

This page has some exercises that relate most directly to the
[names](../code-basics/Names) section.

Here are some assignment statements. Are these valid names?  Why - or why not?
When you have an answer, try the names in a Notebook cell, and see what you
get:

```
five = 5
```

```
Five = 5
```

```
five_Point_three = 5
```

```
five3 = 5
```

```
_five_ = 5
```

```
five_3 = 5
```

```
five.3 = 5
```

```
3five = 5
```

```
five-point-three = 5
```

Look at these blocks of lines below, and try and work out what each of these
expressions will return.  Are they valid expressions?  Will they give an
error?

Don't enter the lines into the notebook until you have worked out your answer.
When you do have an answer, try entering the expression as cells in the
notebook:

```
a = 5
b = 3
a + b * 4
```

```
a = 5
a = a + 3
a
```

```
a = 5
b = a + 3
a = 3
b
```

```
first_variable = 5
second_variable = first_variable + 3
first_variable = 3
second_variable
```

```
a = 5
a * 3 * c
```

```
a = 5
a 5 + 4 * 3
```

This one is more tricky, and uses stuff you have not yet seen.  Look at this and try and predict what you would see, after you run these two statements.  Then try running them in a Notebook or in Python.  What do you see?  Why?

```
my_variable == 5
my_variable * 4
```

Hint: look carefully at the equals in the first statement.  You may want to do
a web-search to see what is going on.
