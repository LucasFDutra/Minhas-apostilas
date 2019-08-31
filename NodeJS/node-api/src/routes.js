const express = require("express");
const routes = express.Router();

const ProductController = require("./controllers/ProductController");

// Minhas rotas
routes.get("/products", ProductController.index); //pegar coisas
routes.post("/products", ProductController.store); //adicionar coisas
routes.get("/products/:id", ProductController.show); //ver coisas
routes.put("/products/:id", ProductController.update); //atualiza coisas
routes.delete("/products/:id", ProductController.destroy); //destri coisas

module.exports = routes;
