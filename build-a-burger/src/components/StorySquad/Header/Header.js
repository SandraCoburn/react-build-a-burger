import React from "react";
import city_img from "../../../assets/cityscape.png";
import classes from "./Header.module.css";

const Header = () => {
  return (
    <div className={classes.Toolbar}>
      <h6>Story Squad</h6>
      <img src={city_img} alt="MyCity" />
    </div>
  );
};
export default Header;
