const express = require("express");
const mongoose = require("mongoose");
const mongoUrl = require("./credentials.json");
const routes = require("./src/routes");
const cors = require("cors");

// Iniciando o APP
const app = express();

// app.use(express.json());

// Iniciando o DB
mongoose.connect(mongoUrl.mongoUrl, {
  useNewUrlParser: true
});

// Criação
app.use(express.json());

// cors
app.use(cors());

// Rotas
app.use("/api", routes);

app.listen(3001);
