# -*- coding: utf-8 -*-
"""
	Saving Estimator
	
	A project to estimate how much money is saved based on your income and expenses.
"""

## -------- COMMAND LINE ARGUMENTS ---------------------------
## https://docs.python.org/3.7/howto/argparse.html
import argparse
CmdLineArgParser = argparse.ArgumentParser()
CmdLineArgParser.add_argument(
	"-v",
	"--verbose",
	help = "display debug messages in console",
	action = "store_true",
)
CmdLineArgs = CmdLineArgParser.parse_args()

## -------- LOGGING INITIALISATION ---------------------------
import misc
misc.MyLoggersObj.SetConsoleVerbosity(ConsoleVerbosity = {True : "DEBUG", False : "INFO"}[CmdLineArgs.verbose])
LOG, handle_retval_and_log = misc.CreateLogger(__name__)

try:
	
	## -------------------------------------------------------
	## THE MAIN PROGRAM STARTS HERE
	## -------------------------------------------------------	

	import time

	saving_est_rate_second = (2507*12)/365.25/24/60/60
	saving_est_rate_month = saving_est_rate_second*60*60*24*(365.25/12)
	print("Estimated saving rate: £{:.2f}/month".format(saving_est_rate_month))
	
	saving_est = 0
	while True:
		print("{:.3f}".format(saving_est), end = '\r')
		saving_est += saving_est_rate_second
		time.sleep(1)

## -------- SOMETHING WENT WRONG -----------------------------	
except:

	import traceback
	LOG.error("Something went wrong! Exception details:\n{}".format(traceback.format_exc()))

## -------- GIVE THE USER A CHANCE TO READ MESSAGES-----------
finally:
	
	input("Press any key to exit ...")
