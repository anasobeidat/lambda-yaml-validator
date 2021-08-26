import io
import base64
from yamllint.config import YamlLintConfig
from yamllint import linter
import logging

logger = logging.getLogger()

def lambda_handler(event, context):
    config = YamlLintConfig(file="./default_lint.yml")
    has_errors = False
    has_warnings = False

    with io.StringIO(base64.b64decode(event['content']).decode('utf-8')) as content:
        for problem in linter.run(content, config):
            if problem.level == linter.PROBLEM_LEVELS[2]:
                logger.error(problem)
                has_errors = True
            elif problem.level == linter.PROBLEM_LEVELS[1]:
                logger.warning(problem)
                has_warnings = True
    
        if has_errors:
            raise SystemExit('Yaml issues found. Check Lambda log for details.')
