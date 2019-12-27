import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import api from '../../services/api';
import './styles.css';

export default class Main extends Component {
  state = {
    products: [],
    productInfo: {},
  };

  componentDidMount() {
    this.loadProducts();
  }

  loadProducts = async (page = 1) => {
    const response = await api.get(`/products?page=${page}`);

    const { docs, ...productInfo } = response.data;

    this.setState({ products: docs, productInfo });
  };

  prevPage = () => {
    const page = parseInt(this.state.productInfo.page);

    if (page === 1) return;

    const pageNumber = page - 1;

    this.loadProducts(pageNumber);
  };

  nextPage = () => {
    const page = parseInt(this.state.productInfo.page);

    if (page === this.state.productInfo.pages) return;

    const pageNumber = page + 1;

    this.loadProducts(pageNumber);
  };

  render() {
    const { products } = this.state;

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
          <button onClick={this.prevPage}>Anterior</button>
          <button onClick={this.nextPage}>Próximo</button>
        </div>
      </div>
    );
  }
}