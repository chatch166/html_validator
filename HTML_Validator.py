#!/bin/python3


def validate_html(html):
    '''
    This function  performs a limited version of html validation
    by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    tags = _extract_tags(html)
    stack = []
    balanced = True
    index = 0
    if len(html) == 0:
        return True
    if not tags:
        return False
    while index < len(tags) and balanced:
        tag = tags[index]
        if "/" not in tag:
            stack.append(tag)
        else:
            if len(stack) == 0:
                balanced = False
            elif ("/" not in stack[-1] and "/" in tag
                    and len(tag) == len(stack[-1]) + 1):
                stack.pop()
            else:
                balanced = False
        index += 1
    if balanced and len(stack) == 0:
        return True
    else:
        return False

    # use the  _extract_tags  function below to generate a
    # list of html tags without any extra text;
    # then process these html tags using the balanced
    # parentheses algorithm from the class/book
    # the main difference between your code and the code from
    # class will be that you will have to keep track of
    # not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are
    not meant to be used directly
    by the user are prefixed with an underscore.

    This function returns a list of all tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    import re
    tags = re.findall(r'<[^>]+>', html)
    return tags
