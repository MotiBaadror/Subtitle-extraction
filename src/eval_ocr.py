import json
import os
import time


def char_error_rate(pred, ground_truth):
  """
  Calculates the Character Error Rate (CER) between predicted text and ground truth.

  Args:
      pred: The predicted text string.
      ground_truth: The ground truth text string.

  Returns:
      The Character Error Rate (CER) as a float between 0 and 1.
  """
  if not ground_truth:
    return 1.0  # Handle empty ground truth
  errors = sum(c1 != c2 for c1, c2 in zip(pred, ground_truth))
  return errors / float(len(ground_truth))

def process_eval_ocr(config: dict):
  input_path = config.get('input_path')
  output_path = config.get('output_path')
  # # extract_text_handler = ExtractTextHandler(
  #   input_path=config.get('input_path'),
  #   output_path=config.get('output_path'),
  #   ocrtype=ocrtype
  # )

  start_time = time.time()
  for subdir in os.listdir(input_path):
    for file in os.listdir(os.path.join(input_path, subdir)):
      if 'time' in file:
        continue
      with open(os.path.join(os.path.join(input_path, subdir, file)),'r') as f:
        content = json.loads(f.read())
        text = '\n'.join(content['Text'])

    # text_putput = []
    # json_dir = os.path.join(input_path, video_name)
    # output_name = os.path.join(output_path, video_name)
    # for image_name in os.listdir(img_dir):
  #     img = os.path.join(img_dir, image_name)
  #     result = extract_text(img=img)
  #     if result in text_putput:
  #       continue
  #     text_putput.append(result)
  #
  #   with open(output_name + '.json', 'w+') as f:
  #     json.dump({'Text': text_putput}, f, indent=4)
  # time_taken = int(time.time() - start_time)
  # with open(os.path.join(output_path, f'{ocrtype}_time') + '.json', 'w+') as f:
  #   json.dump({'Time': str(time_taken)}, f, indent=4)
