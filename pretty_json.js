const yaml = require('js-yaml');
const fs   = require('fs');

var tempPath = process.argv[2];
var configData = fs.readFileSync(tempPath + '/config.json', 'utf8')

try {
  const doc = yaml.safeLoad(fs.readFileSync(tempPath + '/in.yml', 'utf8'));
  fs.writeFileSync(tempPath + '/out.yml', yaml.safeDump(doc, JSON.parse(configData)));
} catch(error) {
  console.log(error.message);
}
