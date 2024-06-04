---
orphan: true
---

# Student ratings averages by course

These data are directly from the [supplementary
material](https://www.tandfonline.com/doi/suppl/10.1080/02602938.2016.1276155)
of {cite}`rosen2018correlations`, with thanks.

There is a [freely available post
print](https://asrosen.com/wp-content/uploads/2018/07/postprint_rmp-1.pdf) of
the paper on [Andrew Rosen's website](https://asrosen.com).

The paper studies ratings from <https://www.ratemyprofessors.com>, for the
190,006 US professors that had at least 20 student ratings.

Each row of the data table gives the mean ratings for all professors in a given discipline; thus there is one row per discipline.

Quoting from the paper above:

> Students on RateMyProfessors rate professors based on three main key
> criteria: clarity, helpfulness, and easiness. These criteria are mandatory
> fields when a review is submitted, and the rating scale ranges from 1 to 5 in
> integer increments with 1 being the worst rating and 5 being the best rating.
> Professors are then assigned an overall quality score that is simply the
> average of their clarity and helpfulness scores.

Given that background, the column names are self-explanatory:

- Discipline
- Number of Professors
- Clarity
- Helpfulness
- Overall Quality
- Easiness

There are two data files containing the same data:

- Original {download}`average ratings per course in Excel <disciplines_SI.xlsx>`
- {download}`Average ratings per course in CSV format <rate_my_course.csv>`.
  This is the Excel file above saved in CSV format; see the [Github dataset
  page](https://github.com/matthew-brett/datasets/tree/master/good_and_easy)
  for more detail.

## References

```{bibliography} /bib/course_refs.bib
:filter: docname in docnames
```
