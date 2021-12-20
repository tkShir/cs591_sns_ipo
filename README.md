# CS591 Predicting First-Day Price Signals of IPO Stocks Using  Twitter Sentiments
*Kyle Bryant, Michelle Lee, Takamitsu Shirono*<br/> 
*Boston University, Department of Computer Science*
## Research Question & Ideas
- Is it possible to predict first-day price signal of an IPO stocks using Twitter sentiment of the stock?
- Would Twitter sentiment prediction outperform predictions based on news sentiment or financial analysis?

## Motivation
- Related works show that social media sentiments are a valid predictor for stock price movements.
- Social media serving as a good predictor for price movement + active discussion about IPO stocks on social media  ≟ Social media as a superior predictor for price movement of IPO stocks
- How can we compare the performance of Twitter sentiment?
- Compare to financial and news sentiments as indicators

## Limitation & Narrowing the Problem Space
- Limitations to consider: available time, resources, technical skills
- Accommodating decisions: 
  - Observe only the first-day price signal of the IPO stock
  - Analyze a select, reasonable,  number of stocks (6)
  - Only consider stocks that went public in 2020
- What price signal we consider:
  - From the perspective of retail investors who primarily buy stocks between **9:30AM-3:30PM** EST market hours:
  - ```if (open_price > close_price): price signal = “up”```
  - ```elif open_price < close_price: price signal = “down”```

## Conclusion
- Predictions were correct 83.33% of the time from Twitter sentiment as a first-day price signal.
- Interestingly enough, the accuracy of the model performed best when we made a opposite prediction to the sentiment (i.e. positive sentiment => negative price signal)
- Successful prediction of stocks with little controversy, i.e. products and services that can be measured at surface-level.
  - Helps explain inconsistencies in PLTR prediction due to ICE controversy.
- First-day price signal estimation using Twitter sentiments is a better performing indicator than comparables, and is reliable.

## Project Presentation
![Project Poster Image](https://github.com/tkShir/cs591_sns_ipo/blob/master/Bryant_Lee_Shirono_IPO.png?raw=true)
