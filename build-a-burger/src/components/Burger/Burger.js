import React from "react";
import classes from "./Burger.module.css";
import BurgerIngredients from "./BurgerIngredients/BurgerIngredients";
const Burger = (props) => {
  // we transfor the state object into an array
  let transformedIngredients = Object.keys(props.ingredients)
    .map((igKey) => {
      //to build an array with an array inside that hold the ingredients
      return [...Array(props.ingredients[igKey])].map((_, i) => {
        return <BurgerIngredients key={igKey + 1} type={igKey} />;
      });
    })
    .reduce((arr, el) => {
      //previous value and current value
      return arr.concat(el);
    }, []); //initial value is an empty array
  if (transformedIngredients.length === 0) {
    transformedIngredients = <p>Please start adding ingredients!</p>;
  }
  console.log(transformedIngredients);
  return (
    <div className={classes.Burger}>
      <BurgerIngredients type="bread-top" />
      {transformedIngredients}
      <BurgerIngredients type="bread-bottom" />
    </div>
  );
};
export default Burger;
