import React from "react";
import Aux from "../../../hoc/Aux";
import classes from "../Pages/Layout_story.module.css";
import Header from "../Header/Header";

const Layout_story = (props) => (
  <Aux>
    <Header />

    <main className={classes.Content}>{props.children}</main>
  </Aux>
);
export default Layout_story;
