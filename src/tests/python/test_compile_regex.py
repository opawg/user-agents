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


def test_ids():
  ids = set()
  no_id_issues = []
  wrong_id_issues = []
  duplicate_issues = []

  # track errors
  for user_agent_item in user_agents:
    primary_regex = user_agent_item['user_agents'][0]
    if ("id" not in user_agent_item):
      no_id_issues.append("no id for \"%s\"..." % primary_regex)
    else:
      id = user_agent_item['id']
      if type(id) != int:
        wrong_id_issues.append("wrong id for \"%s\" where id=\"%s\" (type int expected, %s found)" % (primary_regex, id, type(id)))
      elif id in ids:
        duplicate_issues.append("duplicate id for \"%s\" with id=%s" % (primary_regex, id))
      else:
        ids.add(id)

  next_suggested_id = max(ids or [0]) + 1
  
  # print errors
  for issue in no_id_issues + wrong_id_issues + duplicate_issues:
    logging.error(issue)
  
  if no_id_issues or wrong_id_issues or duplicate_issues:
    logging.error("\nno id issue(s):\t\t%s\nwrong id issue(s):\t%s\nduplicate issue(s):\t%s" % (len(no_id_issues), len(wrong_id_issues), len(duplicate_issues)))
    logging.error("\nnext suggested id:\t%s" % next_suggested_id)
    
  assert not no_id_issues and not wrong_id_issues and not duplicate_issues