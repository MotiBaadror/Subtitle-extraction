from eval_ocr import char_error_rate


def test_eval_ocr():
    ground_truth = "This is a test string."
    prediction = "This isa test string"  # One character substitution error

    cer = char_error_rate(prediction, ground_truth)
    assert isinstance( cer, float)
    print(f"Character Error Rate (CER): {cer}")