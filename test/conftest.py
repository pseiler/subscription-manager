import os


def pytest_deselected(items):
    """Save deselected tests into config."""
    if not items:
        return

    config = items[0].session.config
    config.deselected = items


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Report deselected tests.

    Adapted from https://stackoverflow.com/a/61026429.
    """
    reports = terminalreporter.getreports('')
    content = os.linesep.join(text for report in reports for secname, text in report.sections)

    deselected = getattr(config, "deselected", [])
    if not deselected:
        return

    terminalreporter.ensure_newline()
    terminalreporter.section('deselected tests', sep='=', yellow=True)
    content = os.linesep.join(item.nodeid for item in deselected)
    terminalreporter.line(content)
