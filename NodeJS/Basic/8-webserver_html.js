var http = require("http");
var fs = require("fs");
http.createServer(function(req, res){ //request al khach hang goi len, res la ket qua tra ve
    res.writeHead(200,{"Content-Type":"text/html"});
    var data = fs.readFileSync(__dirname + "/8-index.html","utf-8");
    data = data.replace("{NAME}", "KhoaTran.Com")
    res.end(data);
}).listen(8888);