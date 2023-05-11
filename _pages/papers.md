---
layout: archive
title: "Papers"
permalink: /papers/
author_profile: true
---

1. [Surveying Generative AI's Economic Expectations](../files/survey_AI.pdf)\
   This version: April 2023\
   \[[Paper](../files/survey_AI.pdf)\] \[[SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4430515)\] \[[ArXiv](https://arxiv.org/abs/2305.02823)\]
   <details><summary>Abstract</summary>
   This paper characterizes the transition dynamics of a continuous-time neoclassical production economy with capital accumulation in which households face idiosyncratic income risk. Insurance companies operating in perfectly competitive markets offer long-term insurance contracts and can commit to future contractual obligations, whereas households cannot. Therefore the equilibrium features imperfect insurance and a non-degenerate cross-sectional consumption distribution. When household labor productivity takes two values, one of which is zero, and the utility function is logarithmic, we show that the transition dynamics induced by unexpected positive or negative technology shocks, including the evolution of the consumption distribution, can be calculated in closed form, as long as the initial deviation from the steady state is not too large. This is in contrast to both the standard representative agent neoclassical growth model as well as Bewley (1986) style models with uninsurable idiosyncratic income risk.  Thus the paper provides an analytically tractable alternative to the standard incomplete markets general equilibrium model developed in Aiyagari (1994) by retaining its physical structure, but substituting the assumed incomplete asset markets structure with one in which limits to consumption insurance emerge endogenously, as in the macroeconomic literature on limited commitment.
   </details>

2. [Narrative Asset Pricing: Interpretable Systematic Risk Factors from News Text](../files/narrative_AP.pdf) (with Bryan Kelly and Yinan Su)\
   Forthcoming at *Review of Financial Studies*\
   This version: May 2023\
   \[[Paper](../files/narrative_AP.pdf)\] \[[SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3895277)\] \[[Code](https://github.com/lbybee/regipca)\]
   <details><summary>Abstract</summary>
We estimate a narrative factor pricing model from news text of The Wall Street Journal. Our empirical method integrates topic modeling (LDA), latent factor analysis (IPCA), and variable selection (group lasso). Narrative factors achieve higher out-of-sample Sharpe ratios and smaller pricing errors than standard characteristic-based factor models and predict future investment opportunities in a manner consistent with the ICAPM. We derive an interpretation of the estimated risk factors from narratives in the underlying article text.
    </details>

3. [Business News and Business Cycles](../files/BNBC.pdf) (with Bryan Kelly, Asaf Manela, and Dacheng Xiu)\
   Revise and Resubmit at *Journal of Finance*\
   This version: April 2023\
   \[[Paper](../files/BNBC.pdf)\] \[[Data](http://structureofnews.com/)\]
   <details><summary>Abstract</summary>
We propose an approach to measuring the state of the economy via textual analysis of business news. From the full text of 800,000 Wall Street Journal articles for 1984–2017, we estimate a topic model that summarizes business news into interpretable topical themes and quantifies the proportion of news attention allocated to each theme over time. News attention closely tracks a wide range of economic activities and explains 25% of aggregate stock market returns. A text-augmented VAR demonstrates the large incremental role of news text in modeling macroeconomic dynamics. We use this model to retrieve the narratives that underlie business cycle fluctuations.
    </details>

4. [Macro-based Factors for the Cross-Section of Currency Returns](../files/mIPCA.pdf) (with Leandro Gomes and Joao Valente)\
    This version: February 2022\
   \[[Paper](../files/mIPCA.pdf)\]
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
