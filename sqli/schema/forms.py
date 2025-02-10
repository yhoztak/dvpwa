import bleach
import trafaret as T


EVALUATE_SCHEMA = T.Dict({
    T.Key('points'): T.Int(gte=0, lte=5),
})

def sanitize_input(input_string):
    return bleach.clean(input_string)
REVIEW_SCHEMA = T.Dict({
    T.Key('review_text'): T.String(min_length=1, to_value=sanitize_input),
})

STUDENT_SCHEMA = T.Dict({
    T.Key('name'): T.String(min_length=1, to_value=sanitize_input),
})

COURSE_SCHEMA = T.Dict({
    T.Key('title'): T.String(min_length=1, max_length=127),
    T.Key('description', optional=True): T.String()
})
