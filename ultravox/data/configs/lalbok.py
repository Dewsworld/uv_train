from ultravox.data import types

# "Other" is the split that has not yet been reviewed to be validated/invalidated
# "Validated" split is a superset of "train, test, validation."
# We include the "validation" split from some low-resource languages for training.
# In the future, we will create new training splits from the "validated" split.
LB_BASE_CONFIG = types.DatasetConfig(
    name="lalbok-simple",
    path="dewsworld/simple_bn_1",
    subset="default",
    splits=[
        types.DatasetSplitConfig(name="train", num_samples=9000),
        types.DatasetSplitConfig(name="validation", num_samples=1500),
        types.DatasetSplitConfig(name="test", num_samples=1500),
    ],
    transcript_template="{{text_proc.format_asr_text(sentence)}}",
    assistant_template="{{text_proc.format_asr_text(sentence)}}",
)

LB_TRANS_CONFIG = types.DatasetConfig(
    name="lalbok-simple-transcription",
    base="lalbok-simple",
    user_template=types.TRANSCRIPTION_USER_TEMPLATE,
    eval_config=types.EvalConfig(metric="wer", args={"lang_id": "bn"}),
)

LB_CONT_CONFIG = types.DatasetConfig(
    name="lalbok-simple-continuation",
    base="lalbok-simple",
    user_template=types.CONTINUATION_USER_TEMPLATE,
    assistant_template=types.CONTINUATION_ASSISTANT_TEMPLATE,
)

configs = [LB_BASE_CONFIG, LB_TRANS_CONFIG, LB_CONT_CONFIG]