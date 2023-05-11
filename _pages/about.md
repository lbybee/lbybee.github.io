---
permalink: /
title: "About"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
I am a PhD candidate in financial economics at the Yale School of Management.  A core contention of my research is that novel empricial measurement is central to scientific progress.  My current focus is on developing measures of beliefs with applications to asset pricing and behavioral economics.

Before Yale, I was a researcher at the Booth School of Business, received a master's degree in statistics from the University of Michigan, and completed my undergraduate degree in economics at the University of Chicago.

Education
======
* B.A. in Economics, University of Chicago, 2013
* M.S. in Statistics, University of Michigan, 2017
* Ph.D in Financial Economics, Yale School of Management

Papers
======
1. [Surveying Generative AI's Economic Expectations](../files/survey_AI.pdf)\
   This version: April 2023\
   \[[Paper](../files/survey_AI.pdf)\] \[[SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4430515)\] \[[ArXiv](https://arxiv.org/abs/2305.02823)\]
   <details><summary>Abstract</summary>
I introduce a survey of economic expectations formed by querying a large language model (LLM)’s expectations of various financial and macroeconomic variables based on a sample of news articles from the Wall Street Journal between 1984 and 2021. I find the resulting expectations closely match existing surveys including the Survey of Professional Forecasters (SPF), the American Association of Individual Investors, and the Duke CFO Survey. Importantly, I document that LLM based expectations match many of the deviations from full-information rational expectations exhibited in these existing survey series. The LLM’s macroeconomic expectations exhibit under reaction commonly found in consensus SPF forecasts. Additionally, its return expectations are extrapolative, disconnected from objective measures of expected returns, and negatively correlated with future realized returns. Finally, using a sample of articles outside of the LLM’s training period I find that the correlation with existing survey measures persists – indicating these results do not reflect memorization but generalization on the part of the LLM. My results provide evidence for the potential of LLMs to help us better understand human beliefs and navigate possible models of nonrational expectations.
   </details>

2. [Narrative Asset Pricing: Interpretable Systematic Risk Factors from News Text](../files/narrative_AP.pdf) (with Bryan Kelly and Yinan Su)\
   Forthcoming at *Review of Financial Studies*\
   This version: May 2023\
   \[[Paper](../files/narrative_AP.pdf)\] \[[SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3895277)\] \[[Code](https://github.com/lbybee/regipca)\] \[[Data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/VIWCTK)\]
   <details><summary>Abstract</summary>
We estimate a narrative factor pricing model from news text of The Wall Street Journal. Our empirical method integrates topic modeling (LDA), latent factor analysis (IPCA), and variable selection (group lasso). Narrative factors achieve higher out-of-sample Sharpe ratios and smaller pricing errors than standard characteristic-based factor models and predict future investment opportunities in a manner consistent with the ICAPM. We derive an interpretation of the estimated risk factors from narratives in the underlying article text.
    </details>

3. [Business News and Business Cycles](../files/BNBC.pdf) (with Bryan Kelly, Asaf Manela, and Dacheng Xiu)\
   Revise and Resubmit at *Journal of Finance*\
   This version: April 2023\
   \[[Paper](../files/BNBC.pdf)\] \[[NBER](https://www.nber.org/papers/w29344)\] \[[SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3446225)\] \[[Data](http://structureofnews.com/)\]
   <details><summary>Abstract</summary>
We propose an approach to measuring the state of the economy via textual analysis of business news. From the full text of 800,000 Wall Street Journal articles for 1984–2017, we estimate a topic model that summarizes business news into interpretable topical themes and quantifies the proportion of news attention allocated to each theme over time. News attention closely tracks a wide range of economic activities and explains 25% of aggregate stock market returns. A text-augmented VAR demonstrates the large incremental role of news text in modeling macroeconomic dynamics. We use this model to retrieve the narratives that underlie business cycle fluctuations.
    </details>

4. [Macro-based Factors for the Cross-Section of Currency Returns](../files/mIPCA.pdf) (with Leandro Gomes and Joao Valente)\
    This version: February 2022\
   \[[Paper](../files/mIPCA.pdf)\] \[[Code](https://github.com/bkelly-lab/ipca)\]
   <details><summary>Abstract</summary>
We use macroeconomic characteristics and exposures to Carry and Dollar as instruments to estimate a latent factor model with time-varying betas with the instrumented principal components analysis (IPCA) method by Kelly et al. (2020). On a pure out-of-sample basis, this model can explain up to 78% of cross-sectional variation of a Global panel of currencies excess returns, compared to only 27.9% for Dollar and Carry and 51% for a static PCA model. The latent factor and time-varying exposures are directly linked to macroeconomic fundamentals. The most relevant are exports exposures to commodities and US trade, credit over GDP, and interest rate differentials. This model, therefore, sheds light on how to incorporate macroeconomic fundamentals to explain time-series and cross-section.
    </details>

5. [Change-point Computation for Large Graphical Models: A Scalable Algorithm for Gaussian Graphical Models with Change-points](https://www.jmlr.org/papers/volume19/17-218/17-218.pdf) (with Yves Atchadé)\
    *Journal of Machine Learning Research*\
    This version: January 2018\
   \[[Paper](https://www.jmlr.org/papers/volume19/17-218/17-218.pdf)\] \[[Code](https://cran.r-project.org/web/packages/changepointsHD/index.html)\]
   <details><summary>Abstract</summary>
Graphical models with change-points are computationally challenging to fit, particularly in cases where the number of observation points and the number of nodes in the graph are large. Focusing on Gaussian graphical models, we introduce an approximate majorize- minimize (MM) algorithm that can be useful for computing change-points in large graphical models. The proposed algorithm is an order of magnitude faster than a brute force search. Under some regularity conditions on the data generating process, we show that with high probability, the algorithm converges to a value that is within statistical error of the true change-point. A fast implementation of the algorithm using Markov Chain Monte Carlo is also introduced. The performances of the proposed algorithms are evaluated on synthetic data sets and the algorithm is also used to analyze structural changes in the S&P 500 over the period 2000-2016.
    </details>
