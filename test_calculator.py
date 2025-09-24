import pytest
from model import CalculatorModel


class TestClear:
    @pytest.mark.parametrize(
        "start_expr, expected_result, expected_expr",
        [
            ("123", "0", ""),   # обычная очистка
            ("", "0", ""),      # если уже пусто
        ]
    )
    def test_clear_expression(self, start_expr, expected_result, expected_expr):
        model = CalculatorModel()
        model.expression = start_expr

        result = model.clear()

        assert result == expected_result
        assert model.expression == expected_expr


class TestBackspace:
    @pytest.mark.parametrize(
        "start_expr, expected_results",
        [
            ("123", ["12", "1", "0", "0"]),  # последовательные backspace
            ("", ["0"]),                     # пустая строка
        ]
    )
    def test_backspace_step_by_step(self, start_expr, expected_results):
        model = CalculatorModel()
        model.expression = start_expr

        results = [model.backspace() for _ in range(len(expected_results))]

        assert results == expected_results


class TestAddToExpression:
    @pytest.mark.parametrize(
        "inputs, expected",
        [
            (["7"], "7"),
            (["7", "+"], "7+"),
            (["7", "+", "3"], "7+3"),
        ]
    )
    def test_add_sequence(self, inputs, expected):
        model = CalculatorModel()

        for val in inputs:
            model.add_to_expression(val)

        assert model.expression == expected


class TestCalculate:
    @pytest.mark.parametrize(
        "expression, expected_result",
        [
            ("2+3", "5"),
            ("10/2", "5.0"),
            ("", "0"),
        ]
    )
    def test_valid_expressions(self, expression, expected_result):
        model = CalculatorModel()
        model.expression = expression

        result = model.calculate()

        assert result == expected_result

    def test_invalid_expression_returns_error_and_clears(self):
        model = CalculatorModel()
        model.expression = "2+"

        result = model.calculate()

        assert result == "Ошибка"
        assert model.expression == ""
