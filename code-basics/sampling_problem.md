# A sampling problem

We will soon find that we will need to think about randomness and probability
in order to give sensible answer to many questions.

We start with a legal question, about race discrimination in jury selection.

## Attribution

This page is partly from `Jury_Selection` of the UC Berkeley course \- see the
license file on the main website.

## The problem - was jury selection biased?

In 1963, a court in Talladega County, Alabama sentenced a young black man
called Robert Swain to death. [^dp-note]. All 12 jurors in his trial were
white. He appealed his sentence, citing, among other factors, evidence of bias
in the process by which his jury was selected. At the time, only men aged 21
or older were allowed to serve on juries in Talladega County. In the county,
26% of the eligible jurors were black.

[^dp-note]:
    In the end [Alabama could not execute
    Swain](https://law.justia.com/cases/alabama/supreme-court/1973/274-so-2d-305-1.html)
    because of a [later Supreme Court
    ruling](https://en.wikipedia.org/wiki/Furman_v._Georgia) on another case.

In 1965, the Supreme Court of the United States [denied Swain's
appeal](https://en.wikipedia.org/wiki/Swain_v._Alabama). In its ruling, the
Court wrote "... the overall percentage disparity has been small and reflects
no studied attempt to include or exclude a specified number of Negroes."

The process of jury selection and the law around it is a little complex, but for now, let us ask the question whether we should find it surprising that Swain had no black men on his jury, when 26% of the eligible jurors were black.

The _disparity_ in this case was 0% (the percentage of black jurors on the
jury) compared to 26% (the percentage of black people eligible for jury
service). Is that disparity small?

How would we decide?

We will spend the next while building up the tools we need to answer this
question.
