from logging import Logger
from slack_bolt import Complete

from typing import Iterator, List

import spacy
from gramformer import Gramformer
import torch


torch.manual_seed(1212)
gramformer = Gramformer(models=1)
nlp = spacy.load("en")


def sample_tests(event, complete: Complete, logger: Logger):
    try:
        input_text = event["inputs"]["text"]

        suggested_sentences = []
        for sentence in sentence_reader(input_text):
            suggested_sentence = gramformer.correct(sentence, max_candidates=1)
            suggested_sentences.append(" ".join(suggested_sentence))

        complete(
            outputs={
                "suggestion_msg": get_suggestion_mrkdwn(
                    input_text, " ".join(suggested_sentences)
                )
            }
        )
    except Exception as e:
        logger.error(e)
        complete(error="Unable to execute function, an internal error occurred")
        raise e


def sentence_reader(text: str) -> Iterator[str]:
    for sentence in nlp(text).sents:
        yield sentence.string.strip()


def get_suggestion_mrkdwn(
    original_text: str, suggested_text: str
) -> List[dict]:
    mrkdwn = [":bookmark_tabs: Original text"]
    mrkdwn.append(f"> {original_text}")
    mrkdwn.append(":white_check_mark: Suggested text")
    mrkdwn.append(f"> {suggested_text}")
    return "\n".join(mrkdwn)
