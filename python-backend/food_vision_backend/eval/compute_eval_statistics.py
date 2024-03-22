import json
from os import path
import statistics
import sys

DISH_ID_INDEX = 0
DATA_FIELDNAMES = ["dish_id", "calories", "mass", "fat", "carb", "protein"]

def ReadCsvData(filepath):
  if not path.exists(filepath):
    raise Exception("File %s not found" % path)
  parsed_data = {}
  with open(filepath, "r") as f_in:
    filelines = f_in.readlines()
    for line in filelines:
      data_values = line.strip().split(",")
      parsed_data[data_values[DISH_ID_INDEX]] = data_values
  return parsed_data

if len(sys.argv) != 4:
  raise Exception("Invalid number of arguments\n\n%s" % __doc__)

groundtruth_csv_path = sys.argv[1]
predictions_csv_path = sys.argv[2]
output_path = sys.argv[3]

groundtruth_data = ReadCsvData(groundtruth_csv_path)
prediction_data = ReadCsvData(predictions_csv_path)

groundtruth_values = {}
err_values = {}
residual_sums = {}
total_sums = {}
output_stats = {}

for field in DATA_FIELDNAMES[1:]:
  groundtruth_values[field] = []
  err_values[field] = []
  residual_sums[field] = []
  total_sums[field] = []

mean_groundtruth_values = {}

for field in DATA_FIELDNAMES[1:]:
  mean_groundtruth_values[field] = statistics.mean(
      [float(groundtruth_data[dish_id][i]) for dish_id in groundtruth_data for i in range(1, len(DATA_FIELDNAMES)) if DATA_FIELDNAMES[i] == field])

for dish_id in prediction_data:
  for i in range(1, len(DATA_FIELDNAMES)):
    actual = float(groundtruth_data[dish_id][i])
    predicted = float(prediction_data[dish_id][i])
    groundtruth_values[DATA_FIELDNAMES[i]].append(actual)
    err_values[DATA_FIELDNAMES[i]].append(abs(predicted - actual))
    residual_sums[DATA_FIELDNAMES[i]].append((actual - predicted) ** 2)
    total_sums[DATA_FIELDNAMES[i]].append((actual - mean_groundtruth_values[DATA_FIELDNAMES[i]]) ** 2)

for field in DATA_FIELDNAMES[1:]:
  output_stats[field + "_MAE"] = statistics.mean(err_values[field])
  output_stats[field + "_MAE_%"] = (100 * statistics.mean(err_values[field]) /
                                    statistics.mean(groundtruth_values[field]))
  output_stats[field + "_R^2"] = 1 - sum(residual_sums[field]) / sum(total_sums[field])

with open(output_path, "w") as f_out:
  f_out.write(json.dumps(output_stats))
