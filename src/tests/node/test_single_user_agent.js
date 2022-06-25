/**
 * Use this script to test your new RegEx if it matches your user agent.
 * 
 * Run `node test_single_user_agent.js [user agent]` in your console.
 * If it finds something it replies with the object.
 */

const userAgentDatabase = require('../../user-agents.json');
const userAgent = process.argv[2];

let result;

for(let i = 0; i < userAgentDatabase.length; i++) {
  var regExpStrings = userAgentDatabase[i].user_agents;
  
  for(let j = 0; j < regExpStrings.length; j++){
    var regExp = new RegExp(regExpStrings[j], 'g');

    if(userAgent.match(regExp)){
        result = userAgentDatabase[i];
    }
  }
}

console.log(result ? result : "Nothing found :(");