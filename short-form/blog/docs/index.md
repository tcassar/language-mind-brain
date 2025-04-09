# How Children (and LLMs) Learn Languages

<p style="text-align: right;">
  {{ reading_stats(page.markdown)['time'] }} · {{ reading_stats(page.markdown)['words'] }}
</p>

Playing with my baby cousin involves listening to lots of gibberish - random
utterances which don't even begin to resemble words. This reminded me of the
completely random output an untrained [Large Language Model](https://www.cloudflare.com/en-gb/learning/ai/what-is-large-language-model/) (LLM) generates in its early rounds of training.

This got me thinking: how do children learn languages, and is it in any way
similar to training an LLM?

<figure style="text-align: center"> <img src="https://imgs.xkcd.com/comics/language_acquisition.png" width="200"> <figcaption><a href="https://xkcd.com/2839/">XKCD 2839: Language Acquistion</a></figcaption> </figure>

Child Language Development theory (CLD) is a branch of linguistics which aims
to answer the first of those questions. CLD has many ongoing debates and
unsolved questions, but one clear thing is that **language is acquired in a
series of key phases**.

## Language is acquired in phases

Children start with _reflexive vocalisations_ - cries, grunts, etc - for the
first two months of their existence. Then, they coo, and at 13 months, they
start _babbling_. This is what I hear my cousin doing when we play.

After around 12-14 months, children start to form recognisable words. As time
goes on, their **mean length of utterance** (a common quantitative measure in
child linguistic studies) increases.

<figure style="text-align: center"> <img src="./img/language-acq.svg" width="500"> <figcaption>A (simplified) diagram showing the key stages of language acquisition.</figcaption> </figure>

Children in the two word stage produce utterances which are **in correct
grammatical order**, which suggests they have **learned** (according to
behaviourists; **have**, if you ask nativists) a clear internal structure.

Interestingly, these typical developmental milestones don't vary across either
language or mode. Signing children will learn to sign in the same recognisable
phases as their speaking counterparts.

<figure style="text-align: center">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/s3gqI_lCXQ0" 
          title="Baby babbling in sign language / signing in ASL" frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
          allowfullscreen></iframe>
  <figcaption>Baby babbling in sign language (ASL).</figcaption>
</figure>

The exception is at the one word stage, with signing children typically
getting their first. This is likely due to better dexterity in one's fingers
vs tongue at that early age.

Clearly, physiology makes a difference in how quickly children can produce
language: muscles need to strengthen, vocal chords need to develop, and so on.
However, **physiology also impacts how children perceive language**.

## Children and their receptive language ability

Children up to a year old are **universal phoneme detectors**, meaning that
they are able to differentiate between sounds from any language. Adults, in
comparsion, are not able to differentiate between some sounds in their
non-native languages.

A common example of this is the voiced alveolar plosive, **/d/**, vs the
voiced dental plosive, **/d̪/**. The former is common in English, whereas the
latter is not found in English but in Hindi.

<figure style="text-align: center"> <img src="./img/head-turn.png" width="500"> <figcaption>A child and their caregiver about to undergo a head turn test.</figcaption> </figure>

Conditional head turn tests show that hearing English infants can
differentiate the two up till a year old. After that, they can't tell a
difference.

This tuning suggests that the stimulus children have when acquiring language
can vary wildly after a year. A key debate in CLD is whether children learn
language only from this stimulus, or if there is some innate machinery that
we all have which predisposes us to learn language.

## Nativism, Behaviourism, and LLMs

Behaviourism was pioneered in psychology in a 1913 paper by John B. Watson.
Behaviourists argue that _the stimulus_ (language input) alone is responsible
for children learning language. That is, we have no "built-in" understanding
of the structure of language and only learn via reinforcement.

Nativists, such as Chomsky, would disagree. They may reference the **poverty
of the stimulus**: the idea that language alone doesn't have enough
information embedded within it for an agent to learn all it's rules. Nativists
often mention that only positive example of language exist: no one tells
infants that something _isn't_ a correct grammatical sentence.

LLMs pose an interesting question for Nativists: working with the same poor
stimulus, LLMs are clearly excellent tools for manipulating language. LLMs
are often trained in a [_weakly supervised_](https://en.wikipedia.org/wiki/Semi-supervised_learning) fashion, meaning that most of their training
involves just "looking" at samples. These samples aren't labelled in any way:
there's no provided information such as "this is grammatically correct" or
not.

<figure style="text-align: center"> <img src="https://i2.wp.com/miro.medium.com/v2/resize:fit:685/1*tnDiRDrL0nwZA8VwWSXuFQ.png?ssl=1&w=1600&resize=1600&ssl=1" width="500"> <figcaption>Vector Embeddings: Taken from <a href="https://towardsai.net/p/machine-learning/a-complete-guide-to-embedding-for-nlp-generative-ai-llm">Towards AI</a>.</figcaption> </figure>

Furthermore, LLMs represent semantics as embeddings in high-dimensional vector
spaces, not as grammar rules, as a Nativist may claim. Does this mean the
existance of ChatGPT proves behaviourism?

## Birds Aren't Aeroplanes

Not quite. I don't think the comparsion between the way LLMs encode language
and humans seem to learn is meaningful. There are definitely clear
similarities, but more differences: not least to say that LLMs have access to more data than a person could process in their lifetime.

I think this article can be summed up nicely in one quote sentence:

> _"One wouldn't start studying an aeroplane to gain understanding about how
> birds fly."_
