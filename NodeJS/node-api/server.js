const express = require("express");
const mongoose = require("mongoose");
const mongoUrl = require("./credentials.json");

// Iniciando o APP
const app = express();

// Iniciando o DB
mongoose.connect(mongoUrl.mongoUrl, {
  useNewUrlParser: true
});

// Primeira rota
app.get("/", (req, res) => {
  res.send("Hello World");
});

app.listen(3001);
