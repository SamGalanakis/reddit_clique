# reddit_clique


Community visualization project for network science. The idea is to visualize music communities (subreddits) on reddit. The connections between these subreddits are made by the number of common commenters (have commented at least once on both subreddits in a given timespan). The size of the communities is the number of unique commenters. The subreddit lists and classificatiomn by genre is taken from [here](https://www.reddit.com/r/Music/wiki/musicsubreddits) and is parsed by "subreddit_extractor.py". 

The commenters data for each subreddit is collected through the [pushlift api](https://reddit-api.readthedocs.io/en/latest/) in "main.py" and requires credentials stored in "credentials.json" in root.

The network is then created using networkx in "make_network.py" to output [gephi](https://gephi.org/) readable format for further editing.


![Example network grapg](./example_graph_cropped.svg)
