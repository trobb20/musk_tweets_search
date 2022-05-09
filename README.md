# Musk Tweets Search

### Quick search engine I built from [this database](https://www.kaggle.com/datasets/ayhmrba/elon-musk-tweets-2010-2021). For EM54 Engineering Leadership final paper.

Required to run:

`Python3, pandas, matplotlib`

Download the repo and run:

`python analyze_elon_tweets -r "your regex here"`

Ex:

`python analyze_elon_tweets -r "(?=.*Tesla)|(?=.*SpaceX)"` gets all SpaceX and Tesla tweets