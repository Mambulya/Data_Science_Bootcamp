log_template = "{} {} {}"
src_file = "../ex00/data.csv"
log_file = "analytics.log"
res_file = "report"
num_of_steps = 3
num_arg_accepted = 1
report_template = """Report

We have made {} observations from tossing a coin: {} of them were tails and {} of them were heads.
The probabilities are {:.2f}% and {:.2f}%, respectively.
Our forecast is that in the next {} observations we will have: {} tail and {} heads.
"""
success_message = "The report has been successfully created"
fail_message = "The report hasn’t been created due to an error"