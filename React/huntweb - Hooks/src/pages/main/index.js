import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import api from '../../services/api';
import './styles.css';

const Main = () => {
  const [products, setProducts] = useState([]);
  const [productInfo, setProductInfo] = useState({});

  useEffect(() => {
    loadProducts();
  }, []);

  const loadProducts = async (page = 1) => {
    const response = await api.get(`/products?page=${page}`);

    const { docs, ...productInfo } = response.data;
    setProducts(docs);
    setProductInfo(productInfo);
  };

  const prevPage = () => {
    const page = parseInt(productInfo.page);

    if (page === 1) return;

    const pageNumber = page - 1;

    loadProducts(pageNumber);
  };

  const nextPage = () => {
    const page = parseInt(productInfo.page);
    if (page === productInfo.pages) {
      return;
    }

    const pageNumber = page + 1;
    loadProducts(pageNumber);
  };

  return (
    <div className='product-list'>
      {products.map((product) => (
        <article key={product._id}>
          <strong>{product.title}</strong>
          <p>{product.description}</p>
          <Link to={`/products/${product._id}`}>Acessar</Link>
        </article>
      ))}
      <div className='actions'>
        <button onClick={prevPage}>Anterior</button>
        <button onClick={nextPage}>Próximo</button>
      </div>
    </div>
  );
};

export default Main;
