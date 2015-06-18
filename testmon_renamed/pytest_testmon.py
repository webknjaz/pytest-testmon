"""testmon has been renamed to pytest-testmon"""

def pytest_report_header():
    return """testmon has been renamed to pytest-testmon, please use the new name!!!
    pip uninstall testmon
    pip install pytest-testmon
    """