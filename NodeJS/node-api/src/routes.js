const express = require("express");
const routes = express.Router();

const ProductController = require("./controllers/ProductController");

// Minhas rotas
routes.get("/products", ProductController.index); //pegar coisas
routes.post("/products", ProductController.store); //adicionar coisas

module.exports = routes;
