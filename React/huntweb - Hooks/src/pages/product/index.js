import React, { useState, useEffect } from "react";
import api from "../../services/api";
import "./styles.css";

const Product = props => {
  const [product, setProduct] = useState({});

  useEffect(() => {
    const loadProduct = async () => {
      const { id } = props.match.params;

      const response = await api.get(`/products/${id}`);

      setProduct(response.data);
    };
    loadProduct();
  }, []);

  return (
    <div className="product-info">
      <h1>{product.title}</h1>
      <p>{product.description}</p>
      <p>
        {/* eslint-disable-next-line react/jsx-one-expression-per-line */}
        URL: <a href={product.url}>{product.url}</a>
      </p>
    </div>
  );
};

export default Product;
