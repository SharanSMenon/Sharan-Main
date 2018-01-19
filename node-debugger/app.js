const express = require('express');
const app = express();
app.get('/',(req,res) => {
    debugger;
    res.send("It worked")
})
app.listen(8080, () => console.log("Server is up"));