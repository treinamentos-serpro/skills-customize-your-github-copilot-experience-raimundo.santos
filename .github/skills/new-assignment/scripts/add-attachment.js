const fs = require("fs");
const path = require("path");

const [id, name, filename, type] = process.argv.slice(2);
const rootPath = path.resolve(__dirname, "../../../..");
const configPath = path.join(rootPath, "config.json");

if (!id || !name || !filename || !type) {
  console.error(
    'Usage: node .github/skills/new-assignment/scripts/add-attachment.js <id> "<display-name>" <filename> <type>',
  );
  process.exit(1);
}

const config = JSON.parse(fs.readFileSync(configPath, "utf8"));
const assignment = config.assignments.find((item) => item.id === id);

if (!assignment) {
  console.error(`Assignment "${id}" was not found in config.json`);
  process.exit(1);
}

const filePath = path.join(rootPath, assignment.path, filename);
if (!fs.existsSync(filePath)) {
  console.error(`Attachment file was not found: ${filePath}`);
  process.exit(1);
}

assignment.attachments ??= [];
if (assignment.attachments.some((attachment) => attachment.file === filename)) {
  console.error(`Attachment "${filename}" is already registered`);
  process.exit(1);
}

assignment.attachments.push({ name, file: filename, type });
fs.writeFileSync(configPath, JSON.stringify(config, null, 2) + "\n");
console.log(`Added attachment "${name}" to "${assignment.title}"`);