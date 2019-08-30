const express = require("express");
const routes = express.Router();

// Minha rota
routes.get("/", (req, res) => {
  return res.send("Hello");
});

module.exports = routes;
