---
layout: page
title: Sentiment via CNN Classifier
keywords: sentiment, classifier
permalink: '/sentiment.html'
nav_order: 4
parent: Neural Pipeline
---

## Description

Sentiment is added to the stanza pipeline by using a CNN classifier.

https://arxiv.org/abs/1408.5882

| Name | Annotator class name | Requirement | Generated Annotation | Description |
| --- | --- | --- | --- | --- |
| sentiment | SentimentProcessor | tokenize | `sentiment` | Adds the `sentiment` annotation to each [`Sentence`](data_objects.md#sentence) in the `Document` |

## Options

| Option name | Type | Default | Description |
| --- | --- | --- | --- |
| 'model_path' | string | depends on the language | Where to load the model. |
| 'pretrain_path' | string | depends on the language | Which set of pretrained word vectors to use. Can be changed for existing models, but this is not recommended, as the models are trained to work specifically with one set of word vectors. |
| 'batch_size' | int | None | If None, run everything at once.  If set to an integer, break processing into chunks of this size |

## Example Usage

The `SentimentProcessor` adds a label for sentiment to each
[`Sentence`](data_objects.md#sentence).  The existing models each
support negative, neutral, and positive, represented by 0, 1, 2
respectively.  Custom models could support any set of labels as long
as you have training data.

### Simple code example

import stanza

```
nlp = stanza.Pipeline(lang='en', processors='tokenize,sentiment')
doc = nlp('I hate that they banned Mox Opal')
for i, sentence in enumerate(doc.sentences):
    print(i, sentence.sentiment)
```

The output produced (aside from logging) will be:

```
0
```

This represents a negative sentiment.

## Available models

There are currently three models available: English, Chinese, and German.

### English

English is trained on the following data sources:

[Stanford Sentiment Treebank](https://github.com/stanfordnlp/sentiment-treebank), including extra training sentences

[MELD](https://github.com/declare-lab/MELD/tree/master/data/MELD), text only

[SLSD](addlinkhere)

[Arguana](addlinkhere)

[Airline Twitter Sentiment](addlinkhere)

The score on this model is not directly comparable to existing SST
models, as this is using a 3 class projection of the 5 class data and
includes several additional data sources (hence the `sstplus`
designation).  However, training this model on 2 class data using
higher dimension word vectors gets close to the 87 score reported in
the original CNN classifier paper.

### Chinese

The Chinese model is trained using the polarity signal from the following 

http://a1-www.is.tokushima-u.ac.jp/member/ren/Ren-CECps1.0/Ren-CECps1.0.html