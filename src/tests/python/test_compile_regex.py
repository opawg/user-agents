import pytest
import re
import json
import os
import logging

root_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
json_path = os.path.join(root_path, "user-agents.json")
with open(json_path, 'r') as f:
  user_agents = json.load(f)

def test_compile_regex():
  wrong_regexes = []
  for user_agent_item in user_agents:
    for regex in user_agent_item['user_agents']:
      try:
        re.compile(regex)
      except:
        wrong_regexes.append(regex)
        logging.error("regex %s could not be compiled" % regex)

  assert not bool(wrong_regexes)
