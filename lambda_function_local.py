from yamllint.config import YamlLintConfig
from yamllint import linter

def main():
    config = YamlLintConfig(file="./default_lint.yml")

    has_errors = False
    has_warnings = False

    with open("config_file.yaml", 'r') as contents:
        for problem in linter.run(contents, config):
            print(problem)
            if problem.level == linter.PROBLEM_LEVELS[2]:
                has_errors = True
            elif problem.level == linter.PROBLEM_LEVELS[1]:
                has_warnings = True

    if has_errors:
        raise SystemExit("yammlint issues found")


if __name__ == "__main__":
    main()
