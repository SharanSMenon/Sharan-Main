const express = require('express');
app = express();
app.get('/' , (req, res) => {
    res.send("Welcome to my home page")
})
app.listen(3000, () => {
    console.log("Server is ready");
    
});