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

// Rotas
app.use("/api", require("./src/routes"));

app.listen(3001);
