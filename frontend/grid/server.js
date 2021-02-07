const express = require('express');
const app = new express();
const port = 5001;

app.use('/js', express.static(__dirname + '/js'));
app.use('/node_modules', express.static(__dirname + '/node_modules'));

app.get('/', function (request, response) {
    response.sendFile(__dirname + '/css.html');
});


app.listen(port, () =>
    console.log(`Example app listening at http://localhost:${port}`)
);