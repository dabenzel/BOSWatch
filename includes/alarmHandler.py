#!/usr/bin/python
# -*- coding: cp1252 -*-

import logging

from includes import globals  # Global variables

def processAlarm(typ,freq,data):
	logging.debug("[  ALARM  ]")
	for name, plugin in globals.pluginList.items():
		logging.debug("call Plugin: %s", name)
		plugin.run(typ,freq,data)
		logging.debug("return from: %s", name)
	logging.debug("[END ALARM]")