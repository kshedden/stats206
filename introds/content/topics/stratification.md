Stratification
==============

Data analysis is often conducted in settings with extreme
_heterogeneity_.  Heterogeneity refers to a setting where the data
being analyzed are obtained from analysis units (e.g. people) that are
different in many ways, some of which we know about and that may be
deeply related to the primary question being pursued, and many others of
which we do not know about or are less relevant for addressing the
question at-hand.

Heterogeneity is related to the notion
of "dispersion" (or to its synonym "variation") which we have already
discussed, but is usually taken to have a slightly distinct connotation.
Heterogeneity refers to dispersion that results from factors of secondary
interest, or that is an unintended consequence of the way that the data were collected.
As one example, suppose we are interested in the relationship
between marital status and wealth.  To assess this relationship, we
collect data on marital status and wealth for people of different races
who live in different states.  The variation in marital
status and in wealth are intrinsic to our research question -- if there
were no variation in these variables, we could not assess how they are related.  But
the variation by geographic location (i.e. state)
or by race may be of secondary interest.  In such a setting, these sources
of variation introduce heterogeneity to our study data, and in most
cases we would want to account for this somehow in the analysis.

As another example, let's consider the setting
of research with human subjects, and imagine that we are interested in
understanding the risk of dying from cancer.
We will use data from Japan for the year 2015, obtained from the World
Health Organization (WHO).  In Japan in 2015, a total of 370,322
people were reported to have died of cancer.  The population of Japan
in that year was 125,319,299.  Therefore, the overall rate of cancer
deaths in Japan was 296 deaths per 100,000 people. However, the rates
of cancer death are very different among different subpopulations
within Japan.  A very basic way to partition a human population is
based on age and biological sex.  The table below shows the numbers of
deaths, the population size, and the death rate per 100,000 people for
eight "strata" of the population of Japan, defined by sex and age.  We
have collapsed the ages into four intervals for simplicity here.

| Sex   | Variable   |    0-19     |     20-50   |   50-70     |    70+     |  All ages    |
| :--   |:--         |        --:  |        --:  |        --:  |       --:  |         --:  |
| F     | Deaths     |      191    |     5,498   |    32,810   |   112,338  |    150,837   |
| F     | Population | 10,606,814  |  22,547,623 | 17,016,127  | 14,125,979 |  64,296,542  |
| F     | Rate/100K  |      1.8    |     24.4    |    192.8    |    795.3   |     234.6    |
| M     | Deaths     |      241    |     4,307   |    57,092   |   157,845  |    219,485   |
| M     | Population | 11,155,528  | 23,356,641  | 16,612,487  |  9,898,100 |  61,022,756  |
| M     | Rate/100K  |      2.2    |     18.4    |    343.7    |   1594.7   |     359.7    |
| All   | Deaths     |      432    |     9,805   |    89,902   |   270,183  |    370,322   |
| All   | Population | 21,752,342  | 45,904,264  | 33,628,614  | 24,024,079 | 125,319,299  |
| All   | Rate/100K  |      2.0    |     21.4    |    267.3    |   1124.6   |     295.5    |

The table shows us that the death rate of 296 per 100,000 is actually
composed of a female-specific rate of 235 per 100,000, and a
male-specific rate of 360 per 100,000.  Or, if we focus on age, we see
rates ranging from 2 per 100,000 for 0-19 year olds to 1,125 per
100,000 for people aged 70 and over.  Looking across the eight strata,
we see rates as low as 1.8 per 100,000 (for young females), and as
high as 1,595 per 100,000 (for older males).

The purpose of this illustration is to show that over-summarizing data
can hide potentially interesting findings.  Although it is not
incorrect to report the overall cancer death rate in Japan as 296 per
100,000, this is a heavily summarized result.  Most individual people
in Japan have a risk of dying of cancer in one year that is either
much less than, or much greater than this number, depending on their
sex and age.

The overall rate of death (296 per 100,000) may be referred to as the
"marginal" cancer death rate.  The other death rates are "stratified",
or _conditional_.  The conditional rates can be conditioned on age
(and marginal with respect to sex), or conditioned on sex (and
marginal with respect to age), or conditioned on both age and sex.
The stratum-level statistics may be referred to as _disaggregated_,
while the statistics calculated for the overall population are
_aggregated_.
