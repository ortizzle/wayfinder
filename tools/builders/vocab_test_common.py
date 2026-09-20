# -*- coding: utf-8 -*-
"""Shared helpers for a Wordly Wise lesson built to River's real test format.

Her Unit 2 Vocabulary Test (Drive, 2026-09-20) has five sections, five marks
each. The app cannot stage a section the way a paper does — pickRound serves
five shuffled questions and each must stand alone — so the SHAPES travel and
the staging does not. One helper per section, so a lesson cannot quietly drift
back to "What does X mean?".

    ctx()   Section 1 — a short passage, and how a word is used inside it
    syn()   Section 2 — synonym / antonym
    fit()   Section 3 — sentence completion: the options are ENDINGS
    pos()   Section 4 — parts of speech, three options (see unit_common)
    assoc() Section 5 — word association: three related words, pick the term
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unit_common import q

PASSAGE_CAP = 45   # check_content.py's own limit; measured, see CLAUDE.md


def ctx(Q, lv, passage, word, text, opts, ans, hint, steps, main, tip):
    """A context-clue item. `word` is the term being asked about, and the
    passage must CONTAIN it — the paper's Section 1 always asks how a term is
    used IN the passage, so a stem that introduces a word the passage never
    uses is a different (easier) question wearing the same clothes. Asserted
    on a stem prefix so that "obscure" in the stem matches "obscured" in the
    passage."""
    words = len(passage.split())
    assert words <= PASSAGE_CAP, 'passage %d words (cap %d): %s' % (
        words, PASSAGE_CAP, passage[:60])
    stem = word.lower()[:5]
    assert stem in passage.lower(), \
        'passage never uses %r: %s' % (word, passage[:70])
    assert stem in text.lower(), 'stem never names %r: %s' % (word, text[:70])
    q(Q, lv, text, opts, ans, hint, steps, main, tip)
    Q[-1]['passage'] = passage


def syn(Q, lv, word, same, opts, ans, hint, steps, main, tip):
    """Synonym or antonym. `same=True` asks for the synonym. The stem never
    glosses the word (v121) — SAME/OPPOSITE is shouted because the real
    paper's own sections are headed that way and mixing them up is free
    marks lost."""
    text = 'Which word means the %s as %s?' % ('SAME', word) if same \
        else 'Which word means the OPPOSITE of %s?' % word
    q(Q, lv, text, opts, ans, hint, steps, main, tip)


def fit(Q, lv, opening, opts, ans, hint, steps, main, tip):
    """Sentence completion. `opening` is the start of the sentence, carrying
    the vocabulary word; every option is an ENDING that continues it."""
    assert opening.rstrip().endswith('...'), 'opening must trail off: ' + opening
    q(Q, lv, opening, opts, ans, hint, steps, main, tip)


def pos(Q, lv, sentence, word, part, hint, steps, main, tip):
    """Parts of speech — three options, the parts of speech themselves."""
    opts = ['noun', 'adjective', 'verb']
    assert part in opts, part
    assert word.lower() in sentence.lower(), '%r not in %r' % (word, sentence)
    q(Q, lv, '%s\n\nWhat part of speech is "%s" in this sentence?' % (sentence, word),
      list(opts), opts.index(part), hint, steps, main, tip)


def assoc(Q, lv, three, opts, ans, hint, steps, main, tip):
    """Word association: three things that all connect to one of the terms."""
    assert len(three) == 3, three
    q(Q, lv, '%s\n\nWhich word connects to all three?' % ', '.join(three),
      opts, ans, hint, steps, main, tip)
