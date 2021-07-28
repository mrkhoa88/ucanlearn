//require dung de goi mot module.
var fs = require("fs"); //module fs co san dung de xu ly file.

var noidung = fs.readFileSync(__dirname + "/danhsach.txt");

console.log(noidung);
console.log(noidung.toString());