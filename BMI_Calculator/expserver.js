const express = require("express");
const bodyParser = require("body-parser");
const app = express();

app.use(bodyParser.urlencoded({extended:true}));

app.get("/cal", function(req,res){
    // console.log(__dirname);
    res.sendFile(__dirname + "/index.html");
})

app.post("/cal", function(req,res){
   
    let sum = (Number(req.body.v1)/(Number(req.body.v2)*Number(req.body.v2)))
    
    res.send("The Body Mass Index is : "+sum+"kg/m2 ");
    
})


app.listen(3000, function(req,res){
    console.log("PORT 3000 is Up & Running");
});