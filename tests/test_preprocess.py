from dataclasses import dataclass
from unittest.mock import  patch

from _pytest.fixtures import fixture

from preprocess import PreprocessHandler


class TestExtractHandler():
    @fixture
    def result(self):
        @dataclass
        class Result:
            handler: PreprocessHandler =  PreprocessHandler(
                input_path='input_path',
                output_path= 'output_path',
                frame_after_second=2
            )
        return Result()

    def test_init(self,result):
        assert result.handler.input_path == 'input_path'
        assert result.handler.frame_after_second==2

    @patch('preprocess.os')
    def test_extract(self, mock_os,result):
        result.handler.preprocess('some_video','.mp4')
        mock_os.system.assert_called_once()
        mock_os.makedirs.assert_called_once()
