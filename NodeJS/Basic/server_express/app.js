var express = require("express");
var app = express();

var server = require("http").createServer(app);
server.listen(6666);

app.get("/", function(req,res){
    res.send("<font color=red>KhoaTran.com</font>");
});