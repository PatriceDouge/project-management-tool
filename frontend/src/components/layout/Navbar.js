import React, { Component } from "react";
import { Link } from "react-router-dom";

import '../App.css';


// import '.../styles/Navbar.css';

class Navbar extends Component {
  render() {
    return (
      <div className="navbar-fixed">
        <nav className="z-depth-0">
          <div className="nav-wrapper white">
            <Link
              to="/"
              style={{
                fontFamily: "monospace",
                backgroundColor: "#09192F",
                width: "100%",
              }}
              className="col s5 brand-logo center white-text" 
              >
              {/* <i className="material-icons">code</i> */}
              TRACKR
            </Link>
          </div>
        </nav>
      </div>
    );
  }
}
export default Navbar;