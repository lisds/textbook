---
orphan: true
---

# Brexit survey dataset

See: <https://github.com/odsti/brexit_survey>.

Several pages in this course use the data from the 2016 Hansard Survey. The
survey was soon after the Brexit referendum, so we often refer to it as the
**Brexit Survey**.

Every year, the [Hansard
Society](https://www.hansardsociety.org.uk/research/audit-of-political-engagement)
sponsors a survey on political engagement in the UK.

They put topical questions in each survey. For the 2016 / 7 survey, they asked
about how people voted in the Brexit referendum, and about the respondents age.

There is one row per respondent.

The file {download}`brexit_survey.csv` contains these data from the survey.
The columns are:

- `brexit_vote`: respondents' report of their vote in the Brexit referendum.
  Result is categorical with any of these values:
  - "Remain"
  - "Leave"
  - "Did not vote"
  - "Too young"
  - "Can't remember"
  - "Refused"
- `age`: age in years.
