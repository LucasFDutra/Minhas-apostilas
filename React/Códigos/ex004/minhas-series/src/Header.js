import React, {useState} from 'react';

import {
    Navbar, // barra
    NavbarBrand, //titulo dentro da barra
    Collapse, //menu sanduiche
    Nav, // navegação
    NavItem, // item de navegação
    NavLink,
    NavbarToggler // liga o menu
  } from 'reactstrap'
import {Link} from 'react-router-dom'

// um componente que no caso é o cabeçalho da aplicação
const Header = () => {
    const [open, setOpen] = useState(false)
    const toggle = () => {
      setOpen(!open)
    }
    return(
      <Navbar color='light' light expand='md'>
          <div className='container'>
            <NavbarBrand tag={Link} to='/'>Minhas Series</NavbarBrand>
            <NavbarToggler onClick={toggle}/>
            <Collapse isOpen={open} navbar>
            <Nav className='ml-auto' navbar>
                <NavItem>
                    <NavLink tag={Link} to='/series'>Séries</NavLink>
                </NavItem>
                <NavItem>
                    <NavLink tag={Link} to='/generos'>Gêneros</NavLink>
                </NavItem>
            </Nav>
            </Collapse>
        </div>
      </Navbar>
    )
}

export default Header