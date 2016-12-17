import React, {Component} from 'react';
import { Link } from 'react-router';
import logo from '../logo.svg';

class Header extends Component {
  render() {
    return (
      <div className="ui fixed inverted menu">
        <div className="ui container">
          <Link to="/" className="header item">
            <img src={logo} className="app-logo" alt="logo"/>
            Example App
          </Link>
          <Link to="/" className="item">Home</Link>
          <Link to="/todo" className="item">Todo</Link>
          <Link to="/remote" className="item">Todo (Remote)</Link>
          <div className="ui simple dropdown item">
            Dropdown <i className="dropdown icon"/>
            <div className="menu">
              <Link className="item">Link Item 1</Link>
              <Link className="item">Link Item 2</Link>
              <div className="divider"/>
              <div className="header">Header Item</div>
              <div className="item">
                <i className="dropdown icon"/>
                Sub Menu
                <div className="menu">
                  <Link className="item">Link Item 1</Link>
                  <Link className="item">Link Item 2</Link>
                </div>
              </div>
              <Link className="item">Link Item</Link>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Header;
