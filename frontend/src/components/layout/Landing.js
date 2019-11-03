import React, { Component } from "react";
import { Link } from "react-router-dom";

import '../App.css';

class Landing extends Component {
  render() {
    return (
      <div style={{ height: "75vh" }} className="container valign-wrapper">
        <div className="row">
          <div className="col s12 center-align" style={{ maxWidth: "470px" }}>
            <h4>
              Project Management made easy.
            </h4>
            <p className="flow-text grey-text text-darken-1">
              A tool to keep track of your bugs, to-dos, analytics and future improvements for your app. 
            </p>
            <br />
            <div className="col s12 m12 l6 push-l1">
              <Link
                to="/register"
                style={{
                  width: "140px",
                  borderRadius: "3px",
                  letterSpacing: "1.5px",
                  marginBottom: "20px"
                }}
                className="btn btn-large waves-effect waves-light hoverable blue accent-3">
                Register
              </Link>
            </div>
            <div className="col s12 m12 l6 pull-l1">
              <Link
                to="/login"
                style={{
                  width: "140px",
                  borderRadius: "3px",
                  letterSpacing: "1.5px",
                  border: "1px solid #2979FF"
                }}
                className="btn btn-large btn-flat waves-effect white black-text">
                Log In
              </Link>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
export default Landing;