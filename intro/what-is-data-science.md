# What is data science?

The combination of the words _data_ and _science_ do not give much hint as to what _data science_ might mean. Most science has data, and most work in science is analyzing data.

Because the name _data science_ can cover such a broad range of subjects, it
has proved difficult to define.

We can make the definition very broad. For example, the UC Berkeley data
science textbook has [this
definition](https://www.inferentialthinking.com/chapters/intro/what-is-data-science)

> Data Science is about drawing useful conclusions from large and diverse data
> sets through exploration, prediction, and inference.

As you will see, we do not think this very broad definition captures what is
really new in the data science movement. We prefer to define data science as
a new _culture_ of data analysis - like this:

> Data science is an approach to data analysis with a foundation in code
> and algorithms.

Why do we choose this definition? And does it matter?

We start with the second question. If data science is important, then we need
the right definition in order to chose what we do and teach.

## Does data science matter?

Even if data science is hard to define, it has significant influence
in planning for education, and science.

David Donoho is an eminent statistician at Stanford University. He
recently wrote an article reflecting on data science, how it was
defined, and what it could mean. He was worried that data science
would be defined in a narrow way, in terms of big data and machine
learning. He was worried because he thought that data science was
important - that it should be:

> ... the really important intellectual event of the next fifty years.

{cite}`donoho201550`

For Donoho, data science is the rediscovery of the powerful methods of data
exploration and analysis used and taught by statisticians such as John W. Tukey
{cite}`tukey1962future`. These methods will be revolutionary for the future
of data analysis.

Meanwhile, educators, especially in the United States, have concluded that data
science techniques are fundamental to the future of education. A 2018 report
of the National Academies of Science Engineering and Medicine recommended that:

> ... academic institutions should encourage the development of a basic
> understanding of data science in all undergraduates

{cite}`natacad2018ds`

## The origins of data science

The phrase "data science" has been around for a long time
{cite}`press2013history`
but its meaning in current use is very
recent. As it is currently used, the phrase "data science" comes from the job
title "data scientist", and the job title came from the tech industry. D.J.
Patil, at LinkedIn, and Jeff Hammerbacher, at Facebook, noticed that they had
a "new breed" of data analysts - these were scientists who could code. Thomas
Davenport and Patil later described this phenomenon in a famous article "Data
Scientist: The Sexiest Job of the 21st Century" {cite}`davenport2012data`. One
section of the article is "Who are these people":

> ... what data scientists do is make discoveries while swimming in data ...
> At ease in the digital realm, they are able to bring structure to large
> quantities of formless data and make analysis possible. ... Data scientists’
> most basic, universal skill is the ability to write code.

Most had come to code through their scientific work:

> Some of the best and brightest data scientists are PhDs in esoteric fields
> like ecology and systems biology. George Roumeliotis, the head of a data
> science team at Intuit in Silicon Valley, holds a doctorate in astrophysics.

These people needed a new job title, because they were so much more effective
than other data analysts. Because they could code, they were able to analyze a
much wider range of data, and they could build programs to do difficult tasks
such as the analysis of big data sets.

Soon after these articles, data scientist started to become a very valuable job
title, with many companies competing to find people who could do this work.

## A new culture

Data scientists in industry were not doing anything new, in an academic sense.
They were applying skills that they had learned in academia. Central to these
skills was the ability to build analyses in code. It turned out that doing
this led naturally to many of the powerful practices discovered and described
by statisticians like John W. Tukey {cite}`tukey1962future` and Leo Breiman
{cite}`breiman2001statistical`.

## What's new in data science?

What are these practices, that make data scientists in so effective in industry and academia?

The foundation is code. At heart, the novelty in the work of data scientists is not novelty at all - it is just the discovery that being able to use code makes a huge difference to the analyses that you can do, and the conclusions that you can draw. Analysis based on code is:

- Versatile. Code allows us to analyze big, messy, mixed, and
  complex data \- put more simply, it allows us to analyze real
  data.
- Realistic. The real work of analysis is working with real data.
  Much of this work is cleaning, reorganizing, collating and
  exploring. It is both complex and repetitive; it can only be done
  effectively with code. If you can code, then you can do this
  work, describe it, and teach it.
- Collaborative. Programmers have been working for many years on
  methods for effective collaboration. Data scientists learn these
  methods, and apply them, so they become more transparent, more
  efficient, and better at working together in teams.
- Reproducible. Much analysis that does not use code, uses
  graphical interfaces. These are famous for making it difficult to
  record your analysis, or describe it to someone else. Analyses
  based on code are naturally reproducible, because you can run the
  code again, to produce the same result, and you can give someone
  your code, so they can do the same thing.
- Easier to understand. Coding allows us to shift our emphasis from
  the relatively difficult mathematics behind the old-school
  statistical tests, such as t-test and ANOVA, to more direct
  methods such as resampling, including permutation tests and
  bootstrap estimation. Code gives us a language to describe these
  methods in a simple and direct way, and this
  makes the ideas clearer and easier to generalize.

## Why now?

Donoho and others have pointed out that much of what is distinctive in the new
culture of data analysis was already part of the analysis described by John W.
Tukey, in the mid-20th century. Why have these methods only now started to
take hold? We believe it is largely to do with the advances in the tools of
scientific computing. Over the last 20 years we have seen the growth of a new
generation of programming languages with clear, powerful syntax, such as
Python. Another language widely used in data science is R, the statistical
programming language. The originators of R were thinking specifically of data
analysis when designing the language. Python and R are free, and open source,
so they have benefited from the explosion of productivity in [open-source
software](https://en.wikipedia.org/wiki/Open-source_software_development). As
these languages have developed, they have attracted more scientist-programmers,
who build new libraries for data analysis and statistics. Meanwhile
programmers in industry have learned the hard way, how difficult it can be to
write clear and effective code, and there is a substantial body of thought and
practice on process for writing and sharing code. This process spread into the
world of open-source programming, leading to a great increase in the quality
and efficiency of academic code. The combination of richer, clearer languages,
better libraries, and better working process have made it possible to do much
more with code than was previously possible. As a result, many more scientists
can write good code, and therefore, many more scientists use code for data
analysis. Eventually, these scientists appeared in companies that had
difficult problems in data analysis, and showed how effective these skills
could be. These were the data scientists described by Patil and Hammerbacher.

## Elements of data science

If we are right, then data science is defined by what data scientists
do. What do do they do?

- They collate data from many sources;
- They clean up messy data, and use it to try to recover meaningful
  information. But they are sceptical, and know when the data cannot
  be trusted for strong conclusions.
- They explore data, to find errors, and unexpected patterns. They
  will likely use different ways to make graphs and graphics from the
  data, to diagnose and summarize.
- They work hard to understand the process that generated the data, to
  make their conclusions meaningful.
- They understand variation, and the problems and limitations for
  drawing conclusions from noisy and incomplete data.
- They often try and predict what new data will look like, from old
  data. They will use old and new methods to do this, including
  methods from machine learning and statistics.

## Conclusion

Data science is new, and we are still working out what it is. At the
moment, it is best defined by what a data scientist does. A data
scientist uses programming as the basis for a deeper, more flexible
approach to data analysis.

## References

```{bibliography} /bib/course_refs.bib
:filter: docname in docnames
```
