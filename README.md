These are the scripts for extracting error-correct pairs from the [NAIST Lang-8 Learner Corpora](https://sites.google.com/site/naistlang8corpora/)
These programs support only python 3.

# How to use
## For the Lang-8 Learner Corpora (raw format) in [NAIST Lang-8 Learner Corpora](https://sites.google.com/site/naistlang8corpora/)
~~~
python extract_err-cor-pair.py -d lang-8-20111007-L1-v2.dat (-l1 [native_language]) (-l2 [learning_language; default: English]) (-tags)
~~~

### Language list
~~~
['Korean', 'English', 'Japanese', 'Mandarin', 'Traditional Chinese', 'Vietnamese', 'German', 'French', 'Other language', 'Spanish', 'Indonesian', 'Russian', 'Arabic', 'Thai', 'Swedish', 'Dutch', 'Hebrew', 'Tagalog', 'Portuguese(Brazil)', 'Cantonese', 'Italian', 'Esperanto', 'Hawaiian', 'Afrikaans', 'Mongolian', 'Hindi', 'Polish', 'Finnish', 'Greek', 'Bihari', 'Farsi', 'Urdu', 'Turkish', 'Portuguese(Portugal)', 'Bulgarian', 'Norwegian', 'Romanian', 'Albanian', 'Ukrainian', 'Catalan', 'Latvian', 'Danish', 'Serbian', 'Slovak', 'Georgian', 'Hungarian', 'Malaysian', 'Icelandic', 'Latin', 'Laotian', 'Croatian', 'Lithuanian', 'Bengali', 'Tongan', 'Slovenian', 'Swahili', 'Irish', 'Czech', 'Estonian', 'Khmer', 'Javanese', 'Sinhalese', 'Sanskrit', 'Armenian', 'Tamil', 'Basque', 'Welsh', 'Bosnian', 'Macedonian', 'Telugu', 'Uzbek', 'Gaelic', 'Azerbaijanian', 'Tibetan', 'Panjabi', 'Marathi', 'Yiddish', 'Ainu', 'Haitian', 'Slavic']
~~~

## For the Lang-8 Corpus of Learner English in [NAIST Lang-8 Learner Corpora](https://sites.google.com/site/naistlang8corpora/)
~~~
python extract_err-cor_pair4en.py entries.train
~~~

## Example of outputs
These outputs are pairs of learner sentence and correct sentence separated by tab character.
If learner sentence and correct sentence are same, the programs output original sentence as correct sentence.
~~~
original sentence written by learners \t sentence corrected by native speakers
And he took in my favorite subject like soccer .        And he took in my favorite subjects like soccer .
It said that was disappointing .        It said that it was disappointing .
~~~
