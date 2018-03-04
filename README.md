
## Seldon deplyment of a fasttext model that classifies Amazon product reviews by positive or negative sentiment (under dev)

## TLDR: 

Getting started with Seldon is easy. However, ML engineers who want the more advanced functionality like A/B testing and Multi-arm bandits need an understanding of kubernetes json config files. 

### Train model
1. Train and save the fasttext examples model using the provided script
`train_fasttext.py` 

`python train_fasttext.py`

### Wrap model
2. Wrap the fasttext classifier using the core-python-wrapper docker image: 

`docker run -v $(pwd):/model seldonio/core-python-wrapper:0.7 /model fasttext-classifier 0.1 seldonio --force`

### Deploy model through a json configuration file 

