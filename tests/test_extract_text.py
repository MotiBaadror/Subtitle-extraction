from dataclasses import dataclass
from unittest.mock import patch, Mock
from _pytest.fixtures import fixture

from extract_text import ExtractTextHandler

class TestExtractHandler():
    @fixture
    def result(self):
        @dataclass
        class Result:
            handler: ExtractTextHandler =  ExtractTextHandler(
                input_path='input_path',
                output_path= 'output_path',
                # reader = Mock()
            )
        return Result()

    def test_init(self,result):
        assert result.handler.input_path == 'input_path'

    def test_extract(self, result):
        result.handler.reader = Mock()
        result.handler.reader.readtext.return_value = [([],'thanks')]
        out_text = result.handler.extract_text('my_input_path')
        assert out_text==' thanks'



