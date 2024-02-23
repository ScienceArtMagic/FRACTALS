# FRACTALS: Fractal Randomness for Aggregate Compression; a Tokenizer Alternative Looping over Seeds

Mike Bybee, Science/Art/Magic

Consider this "paper" to be a living document. If published to a preprint server (e.g. [arXiv](https://arXiv.org)), best efforts will be made to ensure that updated versions are also published at appropriate releases.

## Abstract

The standard in Natural Language Processing/Language Modeling is to process input text (and convert output vectors back to text) via tokenization, wherein words, subwords, or other representations are mapped to numerical IDs. This approach has led to significant improvement in NLP models' understanding of natural language. Still, it comes with notable pitfalls: The vocabulary itself becomes susceptible to spelling and punctuation errors in training corpora, discrepancies in tokenizer and model training corpora can be exploited or otherwise have unintended results, and efficiency suffers as Word Token Embeddings (WTE) must scale quadratically to the size of the vocabulary (tens of thousands on average, and sometimes hundreds of thousands, for Large Language Models), and the embedding dimension

A relative handful of papers (TODO: cite ByT5, MegaByte, MambaByte) have instead turned to byte-level encoding to alleviate the need for large vocabulary and WTE; however, the computational tradeoff is that, without workarounds, each byte must perform a complete pass through the network to predict the next byte during generation.

This project introduces FRACTALS, a tokenizer alternative. Initial inputs are encoded at (and final outputs decoded from) byte level. Once encoded, their combined vectors can be compressed by matching them with segments of vectors generated with various random seeds, which can be discovered through a simple similarity search. These random vectors can be extended to match longer sequences through manipulations such as slicing, repetition, and concatenation of their segments and/or with other similarly initialized and -manipulated vectors. 

Once such seed, splicing, and length parameters are known, they can be predicted as their own, token-like vectors on the fly. Further compression can then be achieved iteratively and recursively by matching sequences of prior seed/splice/length vectors with further similarity search. As generation progresses, this compression applies to new outputs from the LM head.

Because FRACTALS encodes at the byte level, it can support multilingual and even multimodal models. Furthermore, given a local FRACTALS instance and a FRACTALS-aware model behind an API, this recursive compression enables an unprecedented reduction in network transmission between the hosted model and its user.

Code will be made available at https://github.com/ScienceArtMagic/FRACTALS
