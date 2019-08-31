const express = require("express");
const mongoose = require("mongoose");
const mongoUrl = require("./credentials.json");
const routes = require("./src/routes");

// Iniciando o APP
const app = express();

// Iniciando o DB
mongoose.connect(mongoUrl.mongoUrl, {
  useNewUrlParser: true
});

// Rotas
app.use("/api", routes);

app.listen(3001);
