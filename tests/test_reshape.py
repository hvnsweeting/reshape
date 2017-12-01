#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `reshape` package."""

import pytest

from click.testing import CliRunner

import reshape
from reshape import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_columns_not_evenly():
    assert reshape.column(range(8), 3) == [(0, 3, 6),
                                           (1, 4, 7),
                                           (2, 5, None)]


def test_columns_evenly():
    assert reshape.column(range(9), 3) == [(0, 3, 6),
                                           (1, 4, 7),
                                           (2, 5, 8)]


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'reshape.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
