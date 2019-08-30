const express = require("express");
const mongoose = require("mongoose");
const mongoUrl = require("./credentials.json");
const requireDir = require("require-dir");

// Iniciando o APP
const app = express();

// Iniciando o DB
mongoose.connect(mongoUrl.mongoUrl, {
  useNewUrlParser: true
});

// Puxando os modulos
requireDir("./src/models");

// Iniciando rota
app.use("/api", require("./src/models/routes"));

app.listen(3001);
