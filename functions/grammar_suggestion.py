from logging import Logger
from typing import Iterator, List

from slack_bolt import Complete

import spacy
from gramformer import Gramformer
import torch


torch.manual_seed(1212)
gramformer = Gramformer(models=1)
nlp = spacy.load("en")


def grammar_suggestion(event, complete: Complete, logger: Logger):
    try:
        input_text = event["inputs"]["text"]

        logger.info(f"**INPUT** {input_text}")

        suggested_sentences = []
        for sentence in sentence_reader(input_text):
            suggested_sentence = gramformer.correct(sentence, max_candidates=1)

            logger.info(f"**SUGGESTION** {''.join(suggested_sentence)}")

            suggested_sentences.append(" ".join(suggested_sentence))

        suggested_text = " ".join(suggested_sentences)

        complete(
            outputs={
                "suggestion": get_suggestion_mrkdwn(input_text, suggested_text)
            }
        )
    except Exception as e:
        logger.error(e)
        complete(
            error="Unable to provide suggestion for provided text, internal error"
        )
        raise e


def sentence_reader(text: str) -> Iterator[str]:
    for sentence in nlp(text).sents:
        yield sentence.string.strip()


def get_suggestion_mrkdwn(
    original_text: str, suggested_text: str
) -> List[dict]:
    mrkdwn = [":bookmark_tabs: Original"]
    mrkdwn.append(f"> {original_text}")
    mrkdwn.append(":white_check_mark: Suggestion")
    mrkdwn.append(f"> {suggested_text}")
    return "\n".join(mrkdwn)
