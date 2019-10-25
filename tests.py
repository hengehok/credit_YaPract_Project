# -*- coding: utf-8 -*-
# автотесты

from credit import Credit
import csv
import pytest
import testConstants

test_false_csv_path = "testFileFalse.csv"
test_invalid_csv_path = "testFileInvalid.csv"
test_correct_number_csv_path = "testFileNumbersExample.csv"
expectedResult = []
actualResult = []


def parseFile(test_path):
    actualResult = []
    with open(test_path) as csv_obj:
        reader = csv.DictReader(csv_obj, delimiter=',')
        for line in reader:
            credit = Credit(line)
            result = credit.processСlient()
            actualResult.append(result)
        csv_obj.close()
    return actualResult


actualInvalidFile = parseFile(test_invalid_csv_path)
actualFalseFile = parseFile(test_false_csv_path)
actualCorrectNumFile = parseFile(test_correct_number_csv_path)


@pytest.mark.parametrize('actual', actualInvalidFile)
def test_pass_invalid(actual):
    assert actual.find('Invalid') != -1


@pytest.mark.dependency(depends=['test_pass_invalid'])
@pytest.mark.parametrize('actual', actualFalseFile)
def test_pass_false(actual):
    assert actual.find('False') != -1

@pytest.mark.parametrize('actual', actualCorrectNumFile)
def test_correct_numbers(actual):
    assert actual in testConstants.CORRECT_SUM
